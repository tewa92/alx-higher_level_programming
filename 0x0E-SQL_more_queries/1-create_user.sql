-- script that create user 'user_0d_1' with all privileges
-- user_0d_1 password should be set to user_0d_1_pwd
-- script should not fail if user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
