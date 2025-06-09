-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.top_100pop_smartcontracts`,
  kind FULL
);

-- Main Query
select distinct json_value(event_attributes , '$.contract_address') as smartcontract, count(s.tx_hash) as totaltransactions
from `numia-data.secret.secret_message_events` s
where event_type = 'execute'
group by json_value(event_attributes , '$.contract_address') 
order by totaltransactions desc
limit 100;