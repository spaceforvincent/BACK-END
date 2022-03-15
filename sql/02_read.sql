INSERT INTO classmates(name, age, address) VALUES ('홍길동',23, '서울');

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동',23, '서울'),
('김철수',23, '대전'),
('최혁주',23, '사천'),
('이지연',23, '서울'),
('박명수',23, '서울')

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates WHERE address = '서울';

SELECT DISTINCT age FROM classmates;