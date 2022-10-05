
-- CREATE TABLE zoo (
--   name TEXT NOT NULL,
--   eat TEXT NOT NULL,
--   weight INT NOT NULL,
--   height INT,
--   age INT
-- );

-- 1) 
-- INSERT INTO zoo VALUES 
-- (5, 180, 210, 'gorilla', 'omnivore');
--  입력하려는 값 의 data type이 다르기 때문에 오류가 난다.
-- 해결방법
INSERT INTO zoo
VALUES ('gorilla', 'omnivore', 180,210,5);

-- 2)

INSERT INTO zoo (rowid, name, eat, weight, age) 
VALUES(10,'dolphin', 'carnivore', 210, 3),
(11, 'alligator', 'carnivore', 250, 50);
-- rowid가 중복되기 떄문에 오류가 발생한다. values 중 두번쨰의 rowid를 11로 바꾼다.

-- 3)
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 80);
-- NOT NULL 값이 디폴트인 wieght 필드의 값이 없기떄문에 오류가 난다. weight 값을 추가해준다.
