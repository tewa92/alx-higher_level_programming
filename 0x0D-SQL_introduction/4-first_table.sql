-- script that creates a tabel first_table in current db
-- if table exists script should not fail
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));
