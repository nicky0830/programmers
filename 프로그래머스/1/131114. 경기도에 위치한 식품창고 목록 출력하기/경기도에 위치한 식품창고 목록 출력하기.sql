-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, NVL(FREEZER_YN, 'N') as FREEZER_YN
from food_warehouse
where address like '경기도%'
order by warehouse_id asc