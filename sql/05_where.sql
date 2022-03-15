CREATE TABLE users(
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

DROP TABLE users;

SELECT * FROM users WHERE age >= 30;

SELECT first_name FROM users WHERE  age>=30;

SELECT age, first_name FROM users WHERE age >= 30 and last_name = '김';
