-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.cumulative_newwallets_per_day`,
  kind FULL
);

-- Main Query
with first_appearance as (
  select 
    json_value(event_attributes, '$.sender') as wallet,
    date(min(b.block_timestamp)) as first_appearance_date
  from
    `numia-data.secret.secret_message_events` e
  join
    `numia-data.secret.secret_blocks` b on e.block_height = b.block_height
  where
    b.block_timestamp is not null
  and e.event_type = 'message'
  and JSON_VALUE(event_attributes, '$.action') = '/secret.compute.v1beta1.MsgExecuteContract'
  group by
    json_value(event_attributes, '$.sender')
),
daily_new_wallets as (
  select
    first_appearance_date,
    count(*) as new_wallets
  from
    first_appearance
  group by
    first_appearance_date
)
select
  first_appearance_date,
  sum(new_wallets) over (order by first_appearance_date) as cumulative_new_wallets
from
  daily_new_wallets
order by
  first_appearance_date;

