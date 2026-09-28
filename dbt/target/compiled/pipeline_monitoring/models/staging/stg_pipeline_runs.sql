

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

),

b_status AS ( -- ovde da se proveri ovo
    SELECT
        CASE WHEN
            b_runs.completed_at IS NOT NULL THEN 'DONE'
            ELSE 'RUNNING'
        END AS status,
    FROM "monitoring"."main_raw"."raw_flow_b_runs" as b_runs
),

run_b AS (
    SELECT 
        b_runs.flow_id AS run_id,
        b_runs.flow_name AS pipeline_name,
        'raw_flow_b_runs' AS source_system,
        CASE 
            WHEN b_runs.initiated_at IS NOT NULL AND b_runs.completed_at IS NOT NULL THEN b_status.b_runs = 'DONE'
            WHEN b_runs.initiated_at NOT NULL AND b_runs.completed_at IS NULL THEN b_status.b_runs ='RUNNING'
            ELSE NULL 
        END AS status,
        
        b_runs.initiated_at AS started_at,
        b_runs.completed_at AS finished_at,
        datediff('seconds',b_runs.initiated_at,b_runs.completed_at) as duration_seconds,
        b_runs.sample_identifier as sample_id,
        CAST(NULL AS VARCHAR) AS error_message,
        CAST(NULL AS DOUBLE) AS compute_cost,
        b_runs.records AS records_processed,
        b_runs.environment AS environment,
        CASE
            WHEN b_runs.completed_at IS NOT NULL THEN TRUE
            ELSE NULL
        END AS is_success

    FROM "monitoring"."main_raw"."raw_flow_b_runs" as b_runs
)

select *
FROM run_a 
UNION ALL
select * 
from run_b