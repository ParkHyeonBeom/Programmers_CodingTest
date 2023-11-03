# 식당을 이용한 손님중 리뷰를 많이 남긴 손님의 내용을 출력해라.
# 이를 위해서는 식당을 이용한 손님과 그 손님이 남긴 리뷰의 내용이 포함된 새로운 테이블이 필요하다.
# 그 새로운 테이블에서 리뷰를 가장 많이 남긴 손님(MEMBER_ID)을 찾아 출력하면 된다.
# 리뷰를 가장 많이 남긴 손님은 REST_REVIEW 테이블에서 찾을수 있다.
# 리뷰를 가장 많이 손님은 손님이 남긴 리뷰의 개수를 기준으로 내림차순으로 정리하여 찾을 수 있다.
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(B.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE A JOIN REST_REVIEW B
ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID=(SELECT MEMBER_ID
FROM REST_REVIEW
GROUP BY MEMBER_ID
ORDER BY COUNT(REVIEW_TEXT) DESC LIMIT 1)
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC;
