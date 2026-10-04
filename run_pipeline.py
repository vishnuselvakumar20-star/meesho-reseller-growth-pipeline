from pathlib import Path

from part2_engine.engine import (
    load_monthly_revenue,
    group_by_category,
    calculate_mom,
    validate_csv_file,
)

from part4_agent.agent_runner import run_agent, save_json

BASE_DIR = Path(__file__).resolve().parent

INPUT_CSV = BASE_DIR / "part1_sql" / "output" / "monthly_category_revenue.csv"
OUTPUT_JSON = BASE_DIR / "part4_agent" / "agent_output.json"

print("Starting pipeline...")

validation_errors = validate_csv_file(INPUT_CSV)

if validation_errors:
    print("Validation failed.")
    for error in validation_errors:
        print(error)
    raise SystemExit(1)

print("Validation passed.")

rows = load_monthly_revenue(INPUT_CSV)

grouped = group_by_category(rows)

print("Monthly revenue loaded.")
print(f"Categories found: {len(grouped)}")

results = calculate_mom(
    grouped,
    "May",
    "June"
)

print("MoM calculation completed.")
print(f"Results generated: {len(results)}")

agent_result = run_agent(
    validation_errors,
    results
)

print("Agent processing completed.")

save_json(
    agent_result,
    OUTPUT_JSON
)

print(f"Agent output saved to: {OUTPUT_JSON}")
print("Pipeline completed successfully.")