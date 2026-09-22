 -- noqa: Should accept a string instead of a integer
    
    
    
    create table "monitoring"."main_raw"."raw_kafka_events" ("event_id" varchar,"execution_id" varchar,"workflow_name" varchar,"event_type" varchar,"event_ts" timestamp,"sample_id" varchar,"environment" varchar,"processed_records" bigint,"error_text" varchar)
  ;
    -- dbt seed --
    
          COPY "monitoring"."main_raw"."raw_kafka_events" FROM 'C:\Users\lepar\Desktop\luka\Practical Introduction to Test-Driven Development\dbt\seeds/raw_kafka_events.csv' (FORMAT CSV, HEADER TRUE, DELIMITER ',')
        

;
  