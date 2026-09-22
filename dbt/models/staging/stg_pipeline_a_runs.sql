-- TODO:
-- 1. Read from {{ source('raw_monitoring', 'raw_pipeline_a_runs') }}
-- 2. Normalize column names toward the mart contract.
-- 3. Normalize source statuses:
--      COMPLETED / SUCCEEDED -> DONE
--      FAILED               -> FAILED
--      RUNNING              -> RUNNING
-- 4. Do not calculate every mart metric here unless it naturally belongs in staging.

select *
from {{ source('raw_monitoring', 'raw_pipeline_a_runs') }}
where 1 = 0
