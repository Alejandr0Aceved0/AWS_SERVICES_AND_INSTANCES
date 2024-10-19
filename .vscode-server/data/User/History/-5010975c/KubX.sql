CREATE DATABASE db_users;
USE db_users;

CREATE TABLE users(
    id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20),
    birthday DATE
)

ALTER TABLE users;
ADD PRIMARY KEY (id);

SELECT * FROM users

INSERT INTO user(id, name, last_name, birthday) VALUES (456, 'CARLOS', 'ACEVEDO', '1998-29-08');