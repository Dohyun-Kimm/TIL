-- 테이블 생성하기
CREATE TABLE contacts(
--  이름 데이터 타입, 속성
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
    );

-- 테이블 수정하기
--  1. rename
ALTER TABLE contacts RENAME TO contact2;
--  2. rename column
ALTER TABLE contacts rename COLUMN A TO B;
--  3. add new column
ALTER TABLE contacts add COLUMN column_adition;
--  delete column - 외래키, 고유키, 유니크제약 있는 경우 삭제안됨
ALTER TABLE contacts DROP COLUMN name;

-- DEFAULT 제약조건을 사용하여 테이블 변경 할때 오류 방지 가능
ALTER TABLE new_contracts add COLUMN aa to bb NOT NULL DEFAULT 'no address';


-- 
