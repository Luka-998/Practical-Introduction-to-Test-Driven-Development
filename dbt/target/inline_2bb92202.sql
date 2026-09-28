SELECT
    SUM(CASE WHEN execution_uuid IS NULL THEN 1 ELSE 0 END) AS execution_uuid_nulls,
    SUM(CASE WHEN state IS NULL THEN 1 ELSE 0 END) AS state_nulls,
    SUM(CASE WHEN start_ts IS NULL THEN 1 ELSE 0 END) AS start_ts_nulls,
    SUM(CASE WHEN end_ts IS NULL THEN 1 ELSE 0 END) AS end_ts_nulls
FROM main_raw.raw_pipeline_a_runs