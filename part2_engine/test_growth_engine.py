from part2_engine.engine import (
    validate_csv_file,
    load_monthly_revenue,
    group_by_category,
    calculate_mom,
    get_top_flagged_categories,
    save_results,
    save_flagged_results
)


input_file = "part1_sql/output/monthly_category_revenue.csv"

# 1. Validate input
errors = validate_csv_file(input_file)

if errors:
    print("Validation failed:")
    for error in errors:
        print(error)

else:
    print("Validation passed.")

    # 2. Load and group data
    rows = load_monthly_revenue(input_file)
    grouped = group_by_category(rows)

    # 3. Calculate May -> June growth
    results = calculate_mom(grouped, "May", "June")

    # 4. Save outputs
    save_results(results, "part2_output.csv")
    save_flagged_results(results, "flagged_results.csv")

    # 5. Display top 3 flagged categories
    top_three = get_top_flagged_categories(results)

    print("\nTop 3 flagged categories:")

    for result in top_three:
        print(
            result["category"],
            result["mom_pct"],
            result["status"]
        )

    print("\nPart 2 pipeline completed successfully.")