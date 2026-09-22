-- FINAL MART CONTRACT: exactly these 13 columns
--
--  1. run_id
--  2. pipeline_name
--  3. source_system
--  4. status
--  5. started_at
--  6. finished_at
--  7. duration_seconds
--  8. sample_id
--  9. error_message
-- 10. compute_cost
-- 11. records_processed
-- 12. environment
-- 13. is_success
--
-- Target grain:
-- one row = one pipeline run
--
-- TODO:
-- Combine normalized run-level records from:
--   Pattern A source
--   Pattern B source
--   Pattern C / Kafka-derived runs
--
-- Hint: after each branch has the SAME schema and compatible types,
-- UNION ALL becomes a natural option.

select *
from {{ ref('stg_pipeline_a_runs') }}
where 1 = 0
