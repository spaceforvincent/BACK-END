CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번내용');

SELECT rowid, * FROM articles;

ALTER TABLE articles RENAME TO news;
-- NOT NULL 설정없이 추가하기
ALTER TABLE news ADD COLUMN created_at TEXT;

INSERT INTO news values('제목','내용',datetime('now'));

--NOT NULL 설정에서 추가하기
ALTER TABLE news ADD COLUMN subtitle TEXT DEFAULT '소제목';

ALTER TABLE news RENAME COLUMN title TO main_title;

ALTER TABLE news DROP COLUMN subtitle;
