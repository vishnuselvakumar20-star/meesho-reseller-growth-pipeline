def mom_growth(previous, current):
    return round((current - previous) / previous * 100, 2)



def is_flagged(mom_pct, threshold=8.0):
    if abs(mom_pct) > threshold:
        return "flagged"
    elif abs(mom_pct) < threshold:
        return "not_flagged"
    else:
        return "escalate_exact_boundary"



def validate_feed(rows):
    errors = []

    for line_no, row in enumerate(rows, start=2):
        month = row.get("month", "")
        category = row.get("category", "")
        revenue = row.get("revenue", "")

        if not category.strip():
            errors.append(
                f"line {line_no}: missing category (month={month})"
            )

        if revenue == "":
            errors.append(
                f"line {line_no}: missing revenue (category={category})"
            )
            continue

        try:
            revenue_value = float(revenue)
        except ValueError:
            errors.append(
                f"line {line_no}: nonnumeric revenue ({revenue}) "
                f"for category={category}"
            )
            continue

        if revenue_value < 0:
            errors.append(
                f"line {line_no}: negative revenue ({revenue_value}) "
                f"for category={category}"
            )

    return errors