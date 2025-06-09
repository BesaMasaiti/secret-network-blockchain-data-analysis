-- Model Metadata
MODEL (
  name `bachkaxyz.final_tables.total_gasused_perday`,
  kind INCREMENTAL_BY_TIME_RANGE (
    time_column day -- Assuming `day` is the column representing the date
  )
);

-- Main Query
SELECT
  DATE(b.block_timestamp) AS day,
  SUM(t.gas_used) AS total_gas_used_per_day
FROM
  `numia-data.secret.secret_transactions` t
JOIN
  `numia-data.secret.secret_blocks` b ON t.block_height = b.block_height
WHERE
  t.gas_used IS NOT NULL
GROUP BY
  day

LIMIT
  1000;
