Select s.user_id, ROUND(
        ifnull(
            SUM(c.action = 'confirmed') / COUNT(c.user_id), 0
        ), 2
    ) AS confirmation_rate
from Signups s
    left join Confirmations c on s.user_id = c.user_id
group by
    s.user_id;