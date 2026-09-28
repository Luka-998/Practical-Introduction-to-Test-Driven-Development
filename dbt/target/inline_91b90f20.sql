WITH finished_at AS ( SELECT execution_id, ( CASE WHEN event_type IN ('PIPELINE_FINISHED','PIPELINE_FAILED') FROM raw_main.raw_kafka_events)
