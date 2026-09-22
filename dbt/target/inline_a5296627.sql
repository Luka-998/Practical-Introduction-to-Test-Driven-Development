select
    count(*) as total_rows,
    count(distinct event_id) as unique_events,
    count(distinct execution_id) as unique_pipeline_runs
from main_raw.raw_kafka_events group by execution_id