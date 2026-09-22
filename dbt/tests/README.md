# Custom dbt tests to write

Create at least these two singular SQL tests yourself:

1. `assert_finished_runs_have_finished_at.sql`
   - Return rows that violate the rule.
   - DONE and FAILED runs should have `finished_at`.
   - RUNNING runs may have `finished_at = NULL`.

2. `assert_duration_non_negative.sql`
   - Return rows where `duration_seconds < 0`.

Optional:
3. FAILED rows should have an error_message.
4. DONE rows should have `is_success = true`.
5. RUNNING rows should have `is_success = false` or NULL, depending on your chosen contract.
