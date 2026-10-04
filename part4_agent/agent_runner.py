import json
from part3_narrative.narrative import generate_narrative

def run_agent(validation_errors, results):
    # 1. Hard stop if validation fails
    if validation_errors:
        return {
            "run_month": "",
            "validation_status": "failed",
            "validation_errors": validation_errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "Processing stopped because validation failed."
        }

    # 2. Separate categories by status
    flagged = [
        result for result in results
        if result["status"] == "flagged"
    ]

    escalated = [
        result for result in results
        if result["status"] == "escalate_exact_boundary"
    ]

    # 3. Sort flagged categories by absolute MoM
    flagged = sorted(
        flagged,
        key=lambda result: abs(result["mom_pct"]),
        reverse=True
    )

    # 4. Keep only top 3 for detailed action
    top_three = flagged[:3]
    for result in top_three:
     result["narrative"] = generate_narrative(result)

    # 5. Suppress remaining flagged categories
    suppressed = flagged[3:]

    # 6. Determine run month
    run_month = results[0]["current_month"] if results else ""

    return {
        "run_month": run_month,
        "validation_status": "passed",
        "validation_errors": [],
        "flagged_categories": top_three,
        "suppressed_categories": suppressed,
        "escalated_categories": escalated,
        "action_taken": "Top 3 flagged categories selected for detailed review."
    }


def save_json(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=2)