CREATE TABLE countries (
room_num TEXT,
check_in TEXT, 
check_out TEXT,
grade TEXT, 
price INTEGER
);

INSERT INTO countries VALUES
('B203','2019-12-31','2020-01-03','suite',900),
('1102','2020-01-04','2020-01-08','suite',850),
('303','2020-01-01','2020-01-03','deluxe',500),
('807','2020-01-04','2020-01-07','superior',300);

SELECT rowid, * FROM countries;

ALTER TABLE countries RENAME TO hotels;

SELECT room_num,price FROM hotels ORDER BY price DESC LIMIT 2;

SELECT grade, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;

SELECT * FROM hotels WHERE (room_num LIKE 'B%') OR (grade = 'deluxe');

SELECT * FROM hotels WHERE (room_num NOT LIKE 'B%') and (check_in = '2020-01-04') ORDER BY price ASC;

CREATE TABLE classmate (
name TEXT,
age INT,
address TEXT
);

INSERT INTO classmate values (address='seoul', age=20, name='홍길동');
INSERT INTO classmate (address, age, name) values('seoul',20,'홍길동');
