import csv
import math
import random
from datetime import date, timedelta
from pathlib import Path


random.seed(42)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "ecommerce_performance_2025_2026.csv"

channels = {
    "SEO": {"traffic": 1.25, "cost": 0.18, "conversion": 1.05},
    "SEA": {"traffic": 1.15, "cost": 0.62, "conversion": 1.10},
    "Email": {"traffic": 0.75, "cost": 0.08, "conversion": 1.35},
    "Social Ads": {"traffic": 0.95, "cost": 0.45, "conversion": 0.92},
    "Direct": {"traffic": 0.85, "cost": 0.03, "conversion": 1.20},
    "Affiliation": {"traffic": 0.65, "cost": 0.38, "conversion": 0.98},
}

devices = {
    "Mobile": {"traffic": 1.25, "conversion": 0.92},
    "Desktop": {"traffic": 0.95, "conversion": 1.18},
    "Tablet": {"traffic": 0.35, "conversion": 0.96},
}

countries = {
    "France": 1.00,
    "Belgique": 0.32,
    "Suisse": 0.28,
    "Espagne": 0.42,
    "Italie": 0.36,
}

catalog = [
    ("Mode", "Sneakers urbaines", 79, 0.44),
    ("Mode", "Veste mi-saison", 119, 0.39),
    ("Mode", "Sac bandouliere", 59, 0.46),
    ("Maison", "Lampe de bureau LED", 49, 0.42),
    ("Maison", "Set cuisine bambou", 34, 0.48),
    ("Maison", "Chaise ergonomique", 149, 0.34),
    ("High-Tech", "Casque bluetooth", 89, 0.41),
    ("High-Tech", "Clavier mecanique", 99, 0.38),
    ("High-Tech", "Station de charge", 39, 0.45),
    ("Beaute", "Serum visage", 29, 0.55),
    ("Beaute", "Brosse coiffante", 69, 0.43),
    ("Sport", "Tapis de fitness", 45, 0.47),
    ("Sport", "Montre cardio", 129, 0.36),
    ("Culture", "Livre business", 24, 0.52),
    ("Culture", "Abonnement audio", 12, 0.60),
]


def daterange(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def seasonality(day: date) -> float:
    yearly = 1 + 0.18 * math.sin((day.timetuple().tm_yday / 365) * 2 * math.pi)
    weekend = 1.12 if day.weekday() >= 5 else 1.0
    black_friday = 1.9 if day.month == 11 and 20 <= day.day <= 30 else 1.0
    summer = 1.18 if day.month in (6, 7) else 1.0
    january = 1.15 if day.month == 1 else 1.0
    return yearly * weekend * black_friday * summer * january


rows = []
start = date(2025, 1, 1)
end = date(2026, 3, 31)

for day in daterange(start, end):
    base_day = seasonality(day)
    for category, product, unit_price, gross_margin_rate in catalog:
        category_factor = {
            "Mode": 1.18,
            "Maison": 0.92,
            "High-Tech": 0.78,
            "Beaute": 1.05,
            "Sport": 0.86,
            "Culture": 0.72,
        }[category]

        for channel, channel_cfg in channels.items():
            for device, device_cfg in devices.items():
                country = random.choices(
                    list(countries.keys()),
                    weights=list(countries.values()),
                    k=1,
                )[0]

                base_sessions = random.randint(45, 180)
                sessions = int(
                    base_sessions
                    * base_day
                    * category_factor
                    * channel_cfg["traffic"]
                    * device_cfg["traffic"]
                    * countries[country]
                    * random.uniform(0.75, 1.30)
                )

                sessions = max(sessions, 8)
                product_views = int(sessions * random.uniform(1.25, 2.40))

                add_to_cart_rate = random.uniform(0.08, 0.22)
                checkout_rate = random.uniform(0.42, 0.72)
                order_rate = random.uniform(0.48, 0.78)

                conversion_factor = channel_cfg["conversion"] * device_cfg["conversion"]
                carts = int(product_views * add_to_cart_rate * conversion_factor)
                checkouts = int(carts * checkout_rate)
                orders = int(checkouts * order_rate)

                units = orders + int(orders * random.uniform(0.05, 0.55))
                discount_rate = random.choice([0, 0.05, 0.10, 0.15, 0.20])
                revenue = round(units * unit_price * (1 - discount_rate), 2)
                gross_margin = round(revenue * gross_margin_rate, 2)
                acquisition_cost = round(sessions * channel_cfg["cost"], 2)
                returns = int(orders * random.uniform(0.01, 0.08))

                rows.append(
                    {
                        "date": day.isoformat(),
                        "annee": day.year,
                        "mois": day.strftime("%Y-%m"),
                        "pays": country,
                        "canal_acquisition": channel,
                        "device": device,
                        "categorie": category,
                        "produit": product,
                        "sessions": sessions,
                        "vues_produit": product_views,
                        "ajouts_panier": carts,
                        "passages_checkout": checkouts,
                        "commandes": orders,
                        "unites_vendues": units,
                        "prix_unitaire": unit_price,
                        "taux_remise": discount_rate,
                        "chiffre_affaires": revenue,
                        "marge_brute": gross_margin,
                        "cout_acquisition": acquisition_cost,
                        "retours": returns,
                    }
                )

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} rows -> {OUTPUT}")
