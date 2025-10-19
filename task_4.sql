-- task_4.sql
-- This script prints the full description of the 'Books' table
-- from the 'alx_book_store' database
-- You are not allowed to use DESCRIBE or EXPLAIN statements

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'Books';
