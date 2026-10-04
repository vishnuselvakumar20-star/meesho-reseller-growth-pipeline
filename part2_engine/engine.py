from part2_engine.growth_engine import mom_growth, is_flagged
import csv


def load_monthly_revenue(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def group_by_category(rows):
    grouped = {}

    for row in rows:
        category = row["category"]
        month = row["month"]
        revenue = float(row["revenue"])

        if category not in grouped:
            grouped[category] = {}

        grouped[category][month] = revenue

    return grouped


def calculate_mom(grouped, previous_month, current_month):
    results = []

    for category, months in grouped.items():
        previous = months[previous_month]
        current = months[current_month]

        growth = mom_growth(previous, current)
        status = is_flagged(growth)

        results.append({
            "category": category,
            "previous_month": previous_month,
            "current_month": current_month,
            "previous_revenue": previous,
            "current_revenue": current,
            "mom_pct": growth,
            "status": status
        })

    return results

def sort_by_abs_mom(results):
    return sorted(
        results,
        key=lambda result: abs(result["mom_pct"]),
        reverse=True
    )


def get_flagged_categories(results):
    sorted_results = sort_by_abs_mom(results)

    return [
        result
        for result in sorted_results
        if result["status"] == "flagged"
    ]

def get_top_flagged_categories(results, limit=3):
    flagged = get_flagged_categories(results)
    return flagged[:limit]

def get_escalated_categories(results):
    return [
        result
        for result in results
        if result["status"] == "escalate_exact_boundary"
    ]

def save_results(results, path):
    import csv

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "category",
                "previous_month",
                "current_month",
                "previous_revenue",
                "current_revenue",
                "mom_pct",
                "status"
            ]
        )

        writer.writeheader()
        writer.writerows(results)


def save_flagged_results(results, path):
    flagged = get_flagged_categories(results)

    save_results(flagged, path)

def validate_csv_file(path):
    import csv
    from part2_engine.growth_engine import validate_feed

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return validate_feed(rows)