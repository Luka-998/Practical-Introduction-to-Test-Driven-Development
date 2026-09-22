-- TODO:
-- Normalize raw event column names.
-- Keep this model event-grain:
-- one row = one Kafka event.
-- Do NOT collapse to one row per pipeline run here.

select *
from {{ source('raw_monitoring', 'raw_kafka_events') }}
where 1 = 0
