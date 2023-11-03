select TITLE, A.BOARD_ID, B.REPLY_ID , B.WRITER_ID , B.CONTENTS, DATE_FORMAT(B.CREATEd_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD A join USED_GOODS_REPLY B on A.board_id = B.board_id
WHERE A.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY CREATED_DATE ASC, TITLE ASC;