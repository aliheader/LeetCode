Select distinct
    Max(salary) as SecondHighestSalary
from Employee
where
    salary < (
        Select distinct
            Max(Salary)
        from Employee
    );