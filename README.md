# Meesho Reseller Growth & Alert Intelligence Pipeline

An end-to-end reseller growth-monitoring pipeline that combines SQL analysis, a Python growth-detection engine, deterministic business narratives, and a guarded mock agent runner.

## Project Overview

The pipeline analyzes monthly reseller revenue by category and identifies significant month-over-month movements using an 8% threshold.

The project is divided into four connected Parts:

1. **Part 1 — SQL Business Query Engine**
   - Generates the seeded reseller/order dataset.
   - Runs SQL business queries.
   - Produces the monthly category revenue CSV used by later Parts.

2. **Part 2 — Python Guardrail & Growth-Detection Engine**
   - Validates the Part 1 feed.
   - Calculates month-over-month revenue growth.
   - Classifies significant changes using the 8% threshold.
   - Sorts and prioritizes flagged categories.

3. **Part 3 — Narrative Layer**
   - Converts verified numerical results into concise business narratives.
   - Uses deterministic offline templates.
   - Avoids inventing unsupported causes or figures.

4. **Part 4 — Agentic Workflow & Mock Agent Runner**
   - Validates the feed before processing.
   - Uses the Part 2 results and Part 3 narratives.
   - Selects the top 3 flagged categories.
   - Suppresses remaining flagged categories.
   - Produces structured JSON output.

## Dataset Regeneration

The dataset is generated with a fixed random seed so that the expected results remain reproducible.

From the project root, run:

```powershell
python data/generate_dataset.py

## How to run Part 1

### 1. Generate the dataset

from the project root:

***powershell
python dat/generate_database.py

## Part 1 — Important SQL Note

The zero-order reseller query uses a `LEFT JOIN`.

For the reseller with no matching orders:

- `COUNT(*)` returns `1` because the `LEFT JOIN` still produces one row with `NULL` order columns.
- `COUNT(order_id)` returns `0` because `order_id` is `NULL` for the unmatched row.

Therefore, `COUNT(order_id) = 0` is used to identify resellers with no orders.

## Part 2 — Python Growth-Detection Engine

Part 2 consumes:

```text




```markdown
### Run Part 2

From the project root:

```powershell
python -m part2_engine.test_growth_engine
part1_sql/output/monthly_category_revenue.csv 


## Part 3 — Narrative Layer

Part 3 uses the verified results from Part 2 to create deterministic, offline business narratives.

The narrative layer:

- Identifies the category and months involved.
- States the observed revenue movement and MoM percentage.
- Explains the business implication without inventing a cause.
- Suggests a practical next step.
- Uses only verified values from the pipeline.

### Part 3 Files

```text
part3_narrative/
├── prompt_pack.md
├── worked_narratives.md
├── chart_decisions.md
├── masking.py
├── narrative.py
└── test_masking.py

## Part 4 — Agentic Workflow & Mock Agent Runner

Part 4 connects the validated Part 2 results with the Part 3 narrative layer.

The agent workflow:

1. Validates the input feed.
2. Stops processing if validation fails.
3. Uses the Part 2 MoM results and threshold classifications.
4. Sorts flagged categories by absolute MoM change.
5. Generates narratives for the top 3 flagged categories using Part 3.
6. Suppresses remaining flagged categories.
7. Separates exact-boundary cases for escalation.
8. Writes the final structured JSON output.

### Run Part 4

From the project root:

```powershell
python -m part4_agent.test_agent_runner


## Run the Complete Pipeline

The integrated pipeline runs the connected workflow from the Part 1 output through Part 2, Part 3, and Part 4.

From the project root:

```powershell
python run_pipeline.py

## Documentation References

Official Python standard-library documentation consulted during implementation:

- Python `csv` module
- Python `sqlite3` module
- Python `json` module
- Python `pathlib` module

The project does not require any paid service, API key, or external hosted service. The narrative generation is implemented as a deterministic offline template. 