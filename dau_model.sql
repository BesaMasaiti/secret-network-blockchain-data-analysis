-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.daily_active_users`,
  kind INCREMENTAL_BY_TIME_RANGE (
    time_column day
  )
);

-- Main Query
select date(b.block_timestamp) as day, count(distinct(json_value(event_attributes, '$.sender'))) as users
from `numia-data.secret.secret_message_events` e
join `numia-data.secret.secret_blocks` b ON e.block_height = b.block_height
where e.event_type = 'message'
and JSON_VALUE(event_attributes, '$.action') = '/secret.compute.v1beta1.MsgExecuteContract'
group by day;

 


