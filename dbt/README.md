# dbt Pipeline Monitoring Exercise

## Scenario

You are building a generic monitoring connector for several bioinformatics pipelines.

Three ingestion patterns currently exist:

- Pattern A: a run-level table with useful metadata, but inconsistent source column names/status labels.
- Pattern B: a flow table that only exposes completed processing. It has no real cost value.
- Pattern C: Kafka-style event data ingested into the warehouse. It supports near-real-time state, but the raw table is event-grain rather than run-grain.

Your job is to normalize these sources into one canonical mart.

## Final mart contract

The final model `fct_pipeline_monitoring` must contain exactly these 13 columns:

1. run_id
2. pipeline_name
3. source_system
4. status
5. started_at
6. finished_at
7. duration_seconds
8. sample_id
9. error_message
10. compute_cost
11. records_processed
12. environment
13. is_success

Grain: **one row = one pipeline run**.

Canonical statuses: `RUNNING`, `DONE`, `FAILED`.

## Suggested workflow

1. Create a Python environment.
2. Install dbt-core plus the DuckDB adapter.
3. Copy `profiles.yml.example` to your dbt profiles directory as `profiles.yml`.
4. Run `dbt seed`.
5. Inspect the raw relations.
6. Implement the three staging models.
7. Implement `int_kafka_pipeline_runs`.
8. Build the final mart.
9. Add generic tests to `models/marts/schema.yml`.
10. Add custom singular tests to `/tests`.
11. Run `dbt build`.

## Rules

- Do not change the seed CSV files.
- Do not solve schema inconsistency by renaming the raw columns.
- Preserve the grain of staging models.
- `stg_kafka_events` must remain event-grain.
- `fct_pipeline_monitoring` must be run-grain.
- Decide explicitly whether unavailable cost in Pattern B should be `0` or `NULL`, and be ready to justify it.
- Do not silently treat an unknown value as a known zero unless that is the business contract.

## Questions you should be able to answer afterward

1. Why did you use UNION ALL rather than JOIN when combining run-level sources?
2. Why does the Kafka source need an intermediate model?
3. What is the difference between an event and the current state of a run?
4. Which mart columns are direct, derived, normalized, or unavailable?
5. What assumptions did you make about Pattern B?
6. Which tests protect the mart's grain?
7. Which test protects status semantics?
8. What would change if duplicate Kafka events arrived?
