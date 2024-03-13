-- script that create database 'hbtn_0d_2'
-- If the database hbtn_0d_2 already exists, the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- script that create user 'user_0d_2'
-- User password should be set to 'user_0d_2_pwd'
-- If the user user_0d_2 already exists, your script should not fail
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
