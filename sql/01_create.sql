-- SQLite
INSERT INTO classmates(name, age) VALUES ('홍길동',23);
INSERT INTO classmates VALUES ('홍길동',30,'서울');

SELECT * FROM classmates;

SELECT rowid, * FROM classmates;

DROP TABLE classmates;

CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

