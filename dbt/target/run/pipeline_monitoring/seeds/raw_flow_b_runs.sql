 -- noqa: Should accept a string instead of a integer
    
    
    
    create table "monitoring"."main_raw"."raw_flow_b_runs" ("flow_id" varchar,"flow_name" varchar,"initiated_at" timestamp,"completed_at" timestamp,"sample_identifier" varchar,"records" bigint,"environment" varchar)
  ;
    -- dbt seed --
    
          COPY "monitoring"."main_raw"."raw_flow_b_runs" FROM 'C:\Users\lepar\Desktop\luka\Practical Introduction to Test-Driven Development\dbt\seeds/raw_flow_b_runs.csv' (FORMAT CSV, HEADER TRUE, DELIMITER ',')
        

;
  