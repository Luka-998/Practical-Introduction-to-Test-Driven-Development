
  
  create view "monitoring"."main"."stg_pipeline_runs__dbt_tmp" as (
    

WITH run_a AS (

    SELECT
        a_runs.execution_uuid AS run_id,
        a_runs.workflow AS pipeline_name,
        'raw_pipeline_a_runs' AS source_system,

        CASE
            WHEN a_runs.state IN ('COMPLETED', 'SUCCEEDED') THEN 'DONE'
            ELSE a_runs.state
        END AS status,

        a_runs.start_ts AS started_at,
        a_runs.end_ts AS finished_at,

        date_diff(
            'second',
            a_runs.start_ts,
            a_runs.end_ts
        ) AS duration_seconds,

        a_runs.sample AS sample_id,
        a_runs.err_msg AS error_message,
        a_runs.credits_used AS compute_cost,
        a_runs.row_count AS records_processed,
        a_runs.env AS environment,

        CASE
            WHEN a_runs.state IN ('SUCCEEDED', 'COMPLETED') THEN TRUE
            WHEN a_runs.state = 'RUNNING' THEN NULL
            WHEN a_runs.state = 'FAILED' THEN FALSE
            ELSE NULL
        END AS is_success

    FROM "monitoring"."main_raw"."raw_pipeline_a_runs" AS a_runs

)

SELECT *
FROM run_a
  );
