CREATE FUNCTION getNthHighestSalary(N INT) RETURNS 
INT 
BEGIN 
	Set N = N - 1;
	RETURN (
	    Select Distinct salary
	    from Employee
	    order by salary desc
	    limit 1 Offset N
	);
END