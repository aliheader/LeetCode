WITH
    RankedSalaries AS (
        SELECT
            d.name as Department, e.name as Employee, e.salary as Salary, DENSE_RANK() OVER (
                PARTITION BY
                    e.departmentId
                ORDER BY e.salary DESC
            ) AS salary_rank
        FROM Employee e
            JOIN Department d ON e.departmentId = d.id
    )
SELECT Department, Employee, Salary
FROM RankedSalaries
WHERE
    salary_rank <= 3;