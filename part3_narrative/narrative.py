def generate_narrative(result):
    category = result["category"]
    previous_month = result["previous_month"]
    current_month = result["current_month"]
    previous_revenue = result["previous_revenue"]
    current_revenue = result["current_revenue"]
    mom_pct = result["mom_pct"]

    direction = "increased" if mom_pct > 0 else "decreased"

    return (
        f"{category} revenue {direction} from "
        f"₹{previous_revenue:,.2f} in {previous_month} to "
        f"₹{current_revenue:,.2f} in {current_month}. "
        f"The month-over-month revenue change was {mom_pct:+.2f}%. "
        f"This represents a substantial month-over-month revenue movement "
        f"and should receive business attention. "
        f"The available data confirms the revenue movement but does not "
        f"establish a specific cause. "
        f"Review the {current_month} {category} performance to identify "
        f"measurable changes in order volume, pricing, or other relevant factors."
    )