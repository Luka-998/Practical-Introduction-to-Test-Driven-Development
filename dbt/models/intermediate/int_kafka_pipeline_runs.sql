-- TODO:
-- Convert event-grain data from stg_kafka_events into run-grain data.
--
-- Questions to solve:
-- 1. How do you determine started_at?
-- 2. How do you determine the CURRENT status?
-- 3. How do you determine finished_at?
-- 4. What happens for a run that has STARTED but no terminal event?
-- 5. Which processed_records value should represent the run?
--
-- Target grain:
-- one row = one execution_id / pipeline run

select *
from {{ ref('stg_kafka_events') }}
where 1 = 0
