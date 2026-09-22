 -- noqa: Should accept a string instead of a integer
    
    
    
    create table "monitoring"."main_raw"."raw_pipeline_a_runs" ("execution_uuid" varchar,"workflow" varchar,"state" varchar,"start_ts" timestamp,"end_ts" timestamp,"sample" varchar,"credits_used" double,"row_count" bigint,"env" varchar,"err_msg" varchar)
  ;
    -- dbt seed --
    
          COPY "monitoring"."main_raw"."raw_pipeline_a_runs" FROM 'C:\Users\lepar\Desktop\luka\Practical Introduction to Test-Driven Development\dbt\seeds/raw_pipeline_a_runs.csv' (FORMAT CSV, HEADER TRUE, DELIMITER ',')
        

;
  