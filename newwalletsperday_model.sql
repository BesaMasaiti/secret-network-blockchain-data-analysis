-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.new_wallets_per_day`,
  kind INCREMENTAL_BY_TIME_RANGE (
    time_column first_appearance_day
  )
);

-- Main Query
WITH walletfirstappearance AS (
  SELECT 
    json_value(event_attributes, '$.sender') AS wallet, 
    MIN(b.block_timestamp) AS first_appearance_timestamp
  FROM 
    `numia-data.secret.secret_message_events` e
  JOIN 
    `numia-data.secret.secret_blocks` b ON e.block_height = b.block_height
  WHERE 
    b.block_timestamp IS NOT NULL
  and e.event_type = 'message'
  and JSON_VALUE(event_attributes, '$.action') = '/secret.compute.v1beta1.MsgExecuteContract'
  GROUP BY 
    wallet
)

SELECT 
  DATE(first_appearance_timestamp) AS first_appearance_day, 
  COUNT(wallet) AS new_wallets
FROM 
  walletfirstappearance
GROUP BY 
  first_appearance_day
ORDER BY 
  first_appearance_day;
