-- 1. 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요. 
-- 2. 결과는 회원 ID를 기준으로 오름차  순 정렬해주시고 
-- 3. 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.
SELECT user_id, product_id
from online_sale
group by user_id, product_id
HAVING COUNT(*) > 1
order by user_id, product_id desc;

# -- 코드를 입력하세요
# SELECT USER_ID
#      , PRODUCT_ID
# FROM ONLINE_SALE
# GROUP BY USER_ID
#        , PRODUCT_ID
# HAVING COUNT(*) > 1
# ORDER BY USER_ID ASC, PRODUCT_ID DESC
# ;
