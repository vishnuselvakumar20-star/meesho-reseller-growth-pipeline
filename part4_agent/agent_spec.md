# Part 4 — Agent Specification

## Agent Goal

Analyze the validated reseller revenue feed, identify significant month-over-month category changes, prioritize the largest changes, generate business narratives for the highest-priority categories, and prepare a structured action summary.

The agent is a guarded mock agent runner. It does not send external messages or perform irreversible actions.

## Tools

The agent uses the following project functions:

- `validate_feed` — validates the Part 1 revenue feed before downstream processing.
- `mom_growth` — calculates month-over-month percentage growth.
- `is_flagged` — classifies a change using the 8% threshold.
- Part 2 sorting and prioritization functions — rank flagged categories by absolute MoM change.
- `generate_narrative` — generates deterministic offline business narratives from verified Part 2 results.
- JSON output — writes the final structured result to `agent_output.json`.

## Memory

The agent retains the state required during the current pipeline run:

- Validation result
- Validation errors
- MoM results
- Flagged categories
- Suppressed categories
- Escalated categories
- Generated narratives

No external memory service, database, API key, or paid service is required.

The final structured JSON output provides a reproducible record of the completed run.

## Planner

The agent follows these ordered subtasks:

1. Validate the input feed.
2. Hard-stop if validation fails.
3. Load the validated monthly revenue data.
4. Compute month-over-month growth.
5. Classify each category using the 8% threshold.
6. Sort flagged categories by absolute MoM change.
7. Select the top 3 flagged categories for detailed review.
8. Generate deterministic Part 3 narratives for the top 3.
9. Suppress remaining flagged categories.
10. Escalate exact-boundary categories separately.
11. Validate the final output structure.
12. Emit the final structured JSON result.

## Feedback and Human Checkpoint

The agent checks the generated result against the required output structure before saving it.

The workflow is designed around a human-review checkpoint:

- Detailed narratives are prepared for the top 3 flagged categories.
- The output records the action taken for human review.
- The mock agent does not automatically send alerts, messages, or external notifications.
- If validation fails, the workflow stops before any narrative or agent action is produced.

## Guardrails

- Do not continue processing after failed validation.
- Do not invent causes for revenue changes.
- Do not invent unsupported business facts or figures.
- Do not expose raw reseller names in narratives.
- Do not send messages or perform external actions.
- Exact `+8%` and `-8%` changes must be escalated separately.
- Changes with absolute MoM greater than 8% are flagged.
- Changes with absolute MoM less than 8% are not flagged.
- Only the top 3 flagged categories receive detailed narratives.
- Remaining flagged categories are suppressed from detailed action.
- Final output must follow the defined JSON structure.

## Stopping Conditions

### Success

The workflow stops successfully when:

- Input validation passes.
- MoM calculations are completed.
- Categories are classified.
- Top flagged categories are selected.
- Required narratives are generated.
- The final output structure is valid.
- `agent_output.json` is written successfully.

### Error

The workflow stops with an error when:

- The input feed contains validation errors.
- Required revenue values are missing or nonnumeric.
- A negative revenue value is detected.
- A required category value is missing.
- Downstream processing cannot safely continue.

When validation fails, the agent returns a failed validation status and does not generate downstream narratives.

## Given–When–Then Specifications

### Specification 1 — Valid Feed

**Given** a valid monthly revenue feed,

**When** the agent runs validation,

**Then** validation passes and MoM processing can continue.

### Specification 2 — Invalid Feed

**Given** a feed containing invalid revenue data,

**When** the agent validates the feed,

**Then** processing stops and the validation errors are returned.

### Specification 3 — Significant Change

**Given** a category with an absolute MoM change greater than 8%,

**When** the category is classified,

**Then** its status is `flagged`.

### Specification 4 — Exact Boundary

**Given** a category with an MoM change of exactly `+8%` or `-8%`,

**When** the category is classified,

**Then** its status is `escalate_exact_boundary` and it is handled separately from normal flagged categories.

### Specification 5 — Prioritization

**Given** multiple flagged categories,

**When** the agent prioritizes them,

**Then** they are sorted by absolute MoM change and only the top 3 receive detailed narratives.

### Specification 6 — Narrative Safety

**Given** a flagged category selected for detailed review,

**When** the Part 3 narrative is generated,

**Then** the narrative uses verified numerical results and does not invent an unsupported cause.

### Specification 7 — External Action Guardrail

**Given** a completed agent run,

**When** the final action is prepared,

**Then** the mock agent records the action in JSON but does not send an external message or notification.