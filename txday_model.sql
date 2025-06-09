-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.transactions_per_day`,
  kind FULL
);

-- Main Query
SELECT
  DATE(b.block_timestamp) AS day,
  COUNT(tx_id) AS transactions_per_day
FROM
  `numia-data.secret.secret_transactions` t
JOIN
  `numia-data.secret.secret_blocks` b ON t.block_height = b.block_height
GROUP BY
  day
ORDER BY
  day
LIMIT
  1000;
