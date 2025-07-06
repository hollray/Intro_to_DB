-- This SQL script prints the full description of the 'Books' table
-- from the 'alx_book_store' database using INFORMATION_SCHEMA.
-- The database name will be passed as an argument of the mysql command.

SELECT
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    IS_NULLABLE AS `Null`, 
    COLUMN_KEY AS `Key`,   
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS Extra
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
