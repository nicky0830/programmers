-- 코드를 입력하세요
SELECT B.BOOK_ID, 
A.AUTHOR_NAME, 
DATE_FORMAT(B.published_date, '%Y-%m-%d') as published_date
FROM BOOK B
JOIN AUTHOR A
ON B.author_id = A.author_id
WHERE B.category = '경제'
ORDER BY published_date