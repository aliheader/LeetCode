Select m.name
from Employee e
    join Employee m on e.managerId = m.id
GROUP BY
    e.managerId
HAVING
    COUNT(e.managerId) >= 5;