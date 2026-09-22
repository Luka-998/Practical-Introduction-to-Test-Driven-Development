-- TODO:
-- Pattern B simulation.
-- The source contains only completed flows.
-- Decide how you will represent status and unavailable cost.
-- Important design question: does missing cost mean 0 or NULL?

select *
from {{ source('raw_monitoring', 'raw_flow_b_runs') }}
where 1 = 0
