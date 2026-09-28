WITH finished_at AS ( SELECT (COALESCE(execution_id),NULL), event_ts FROM main_raw.raw_kafka_events WHERE event_type LIKE 

'%FINISHED%' OR event_type LIKE '%FAILED%'
)