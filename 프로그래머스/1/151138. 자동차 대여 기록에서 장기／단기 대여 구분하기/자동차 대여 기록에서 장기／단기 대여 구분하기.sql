-- 코드를 입력하세요
SELECT
history_id, car_id, date_format(start_date, '%Y-%m-%d') as start_date, 
date_format(end_date, '%Y-%m-%d') as end_date,
CASE when DATE_ADD(start_date, interval 29 day) > end_date then '단기 대여'
else '장기 대여'
end as rent_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date like '%2022-09%'
order by history_id desc