-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.total_transactions`,
  kind FULL
);

-- Main Query
select count(distinct t.tx_id) as total_transactions
from `numia-data.secret.secret_transactions` t;



