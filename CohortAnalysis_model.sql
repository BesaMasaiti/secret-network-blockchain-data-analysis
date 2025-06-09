-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.cohort_analysis`,
  kind FULL
);

--- Main Query 
WITH first_active_month AS (
  SELECT 
    DATE_TRUNC(MIN(b.block_timestamp), MONTH) AS cohort_month, 
    JSON_VALUE(event_attributes, '$.sender') AS wallet
  FROM `numia-data.secret.secret_message_events` e
  JOIN `numia-data.secret.secret_blocks` b 
    ON e.block_height = b.block_height
  WHERE e.event_type = 'message'
    AND JSON_VALUE(event_attributes, '$.action') = '/secret.compute.v1beta1.MsgExecuteContract'
  GROUP BY wallet
),


active_per_month AS (
  SELECT 
    DATE_TRUNC(b.block_timestamp, MONTH) AS active_month, 
    JSON_VALUE(event_attributes, '$.sender') AS wallet
  FROM `numia-data.secret.secret_message_events` e
  JOIN `numia-data.secret.secret_blocks` b 
    ON e.block_height = b.block_height
  WHERE e.event_type = 'message'
    AND JSON_VALUE(event_attributes, '$.action') = '/secret.compute.v1beta1.MsgExecuteContract'
)


, cohort_sizes AS (
  SELECT 
    cohort_month, 
    COUNT(DISTINCT wallet) AS cohort_size
  FROM first_active_month
  GROUP BY cohort_month
)

SELECT 
  fam.cohort_month, 
  apm.active_month, 
  COUNT(DISTINCT apm.wallet) AS total_users, 
  COUNT(DISTINCT apm.wallet) * 100.0 / cs.cohort_size AS percentage
FROM first_active_month fam
JOIN active_per_month apm 
  ON fam.wallet = apm.wallet
JOIN cohort_sizes cs
  ON fam.cohort_month = cs.cohort_month
GROUP BY fam.cohort_month, apm.active_month, cs.cohort_size
ORDER BY fam.cohort_month, apm.active_month
LIMIT 1000;