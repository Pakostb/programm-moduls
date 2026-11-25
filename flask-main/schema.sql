-- Выполни один раз в MySQL

CREATE DATABASE IF NOT EXISTS flask_auth;
USE flask_auth;

CREATE TABLE IF NOT EXISTS users (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    user_name     VARCHAR(64)  NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL
);

-- Тестовый пользователь
INSERT INTO users (user_name, user_password)
VALUES ('test', '12345')
ON DUPLICATE KEY UPDATE user_password = VALUES(user_password);
