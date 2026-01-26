deck:: [[SQL]]

- What is the key mistake to avoid when building a CTE?
	- #card
		- Always include the keyword "AS" after the CTE name; correct syntax is:
		  ```sql
		  WITH cte_name AS (SELECT...) 
		  ```
		- Incorrect syntax would be:
		  ```sql
		  WITH cte_name (SELECT...)
		  ```
- How should window functions be used without a PARTITION BY clause?
	- #card
		- Window functions can be used without PARTITION BY when you want to apply the function across the entire result set
		- Example:
		  ```sql
		  SELECT *, ROW_NUMBER() OVER () FROM src_dest_distance
		  ```
- What is the proper way to use the SUM function with window functions and GROUP BY?
	- #card
		- When using SUM in a subquery with window functions, first group the data:
		  ```sql
		  SELECT seller_id 
		  FROM (
		  SELECT seller_id, 
		     DENSE_RANK() OVER (ORDER BY sum(price) DESC) AS rnk 
		  FROM sales 
		  GROUP BY seller_id
		  ) b 
		  WHERE b.rnk = 1
		  ```
- What is the correct syntax for a HAVING clause?
	- #card
		- HAVING always follows GROUP BY and filters grouped results:
		  ```sql
		  SELECT COUNT(CustomerID), Country 
		  FROM Customers 
		  GROUP BY Country 
		  HAVING COUNT(CustomerID) > 5;
		  ```
- What are the key differences between UNION and UNION ALL?
	- #card
		- UNION removes duplicates and returns distinct values (requiring more processing resources)
		- UNION ALL includes all rows including duplicates (better performance) and doesn't sort the result set by default
		  ```sql
		  SELECT column1 FROM table1
		  UNION
		  SELECT column1 FROM tablue2;  -- removes duplicates
		  
		  SELECT column1 FROM table1
		  UNION ALL
		  SELECT column1 FROM table2;  -- keeps all rows
		  ```
- What is the correct syntax for COALESCE and what alternative can be used?
	- #card
		- COALESCE returns the first non-null value:
		  ```sql
		  COALESCE(NULL, 'A', 'B', NULL)  -- returns 'A'
		  ```
		- Check spelling "COALESCE" (not "COALSCE")
		- IFNULL can be used as an alternative in some databases:
		  ```sql
		  IFNULL(column_name, 'default_value')
		  ```
- What is the syntax for the LEAD function?
	- #card
		- LEAD returns the value from a subsequent row:
		  ```sql
		  
		  		  LEAD(expression [, offset [, default_value]]) OVER (
		  [PARTITION BY partition_expression, ... ]
		  ORDER BY sort_expression [ASC | DESC], ...
		  )
		  SELECT month, sales, 
		    LEAD(sales, 1, 'NA') OVER (ORDER BY month) AS next_month_sales 
		  FROM yearly_sales;
		  ```
- What is the syntax for the LAG function?
	- #card
		- LAG returns the value from a previous row:
		  ```sql
		  LAG(expression [, offset [, default_value]]) OVER (
		  [PARTITION BY partition_expression, ... ]
		  ORDER BY sort_expression [ASC | DESC], ...
		  )
		  
		  SELECT *, 
		    LAG(age, 1 , "NA") OVER (ORDER BY age ASC) AS previous_age 
		  FROM Users;
		  ```
- What is the syntax for DATE_ADD and DATE_SUB?
	- #card
		- DATE_ADD:
		  ```sql
		  SELECT DATE_ADD('2017-06-15', INTERVAL 10 DAY);
		  ```
		- DATE_SUB:
		  ```sql
		  DATE_SUB(period_state, INTERVAL 1 DAY)
		  ```
- What is the ANSI vs. non-ANSI JOIN syntax difference?
	- #card
		- ANSI syntax:
		  ```sql
		  /*Always Note SQL Interoperability.*/
		  SELECT e.employee_name, d.department_name 
		  FROM employees e 
		  INNER JOIN departments d ON e.department_id = d.department_id 
		  WHERE e.hire_date > '2020-01-01';
		  ```
		- Non-ANSI syntax:
		  ```sql
		  /*old*/
		  SELECT e.employee_name, d.department_name 
		  FROM employees e, departments d 
		  WHERE e.department_id = d.department_id 
		  AND e.hire_date > '2020-01-01';
		  ```
- What's the difference between WHERE and ON for joins and when does it matter?
	- #card
		- ON conditions are applied during the join process
		- WHERE conditions are applied after the join
		- In OUTER JOINS, conditions in ON preserve non-matching rows:
		  ```sql
		  -- Preserves rows with NULL departments
		  SELECT * FROM employees LEFT JOIN departments 
		  ON employees.dept_id = departments.id AND departments.budget > 100000;
		  
		  -- Filters out rows with NULL departments
		  SELECT * FROM employees LEFT JOIN departments 
		  ON employees.dept_id = departments.id 
		  WHERE departments.budget > 100000;
		  ```
- What is the correct syntax for using SUM with CASE statement for  "Atleast/ Atmost / exactly N" (sql pattern question)?
	-
	- #card
		- ```sql
		  Syntax 
		  
		  -- At least N occurrences
		  HAVING SUM(CASE WHEN <condition> THEN 1 ELSE 0 END) >= N
		  
		  -- Buyers who bought at least 2 S8 phones
		  SELECT buyer_id
		  FROM Sales s
		  INNER JOIN Product p ON s.product_id = p.product_id
		  GROUP BY buyer_id
		  HAVING SUM(CASE WHEN p.product_name = 'S8' THEN 1 ELSE 0 END) >= 2;
		  
		  
		  
		  -- At most N occurrences
		  HAVING SUM(CASE WHEN <condition> THEN 1 ELSE 0 END) <= N
		  -- Buyers who bought at most 1 iPhone
		  SELECT buyer_id
		  FROM Sales s
		  INNER JOIN Product p ON s.product_id = p.product_id
		  GROUP BY buyer_id
		  HAVING SUM(CASE WHEN p.product_name = 'iPhone' THEN 1 ELSE 0 END) <= 1;
		  
		  
		  
		  -- Exactly N occurrences
		  HAVING SUM(CASE WHEN <condition> THEN 1 ELSE 0 END) = N
		  
		  -- Buyers who bought exactly 3 Galaxy phones
		  SELECT buyer_id
		  FROM Sales s
		  INNER JOIN Product p ON s.product_id = p.product_id
		  GROUP BY buyer_id
		  HAVING SUM(CASE WHEN p.product_name = 'Galaxy' THEN 1 ELSE 0 END) = 3;
		  
		  
		  ------------------------------------------------------------------------------------
		  example 2 
		  
		  -- Select buyers who bought **at least one S8** and **never bought an iPhone**.
		  SELECT s.buyer_id 
		  FROM Sales AS s 
		  INNER JOIN Product AS p ON s.product_id = p.product_id 
		  GROUP BY s.buyer_id 
		  HAVING SUM(CASE WHEN p.product_name = 'S8' THEN 1 ELSE 0 END) > 0 
		  AND SUM(CASE WHEN p.product_name = 'iPhone' THEN 1 ELSE 0 END) = 0
		  
		  
		  
		  ```
- How should range conditions be written in SQL?
	- #card
		- Don't use mathematical notation:
		  ```sql
		  -- Incorrect
		  999 < max_salary < 10001
		  ```
		- Use proper SQL syntax:
		  ```sql
		  -- Correct with BETWEEN
		  max_salary BETWEEN 999 AND 10001
		  
		  -- Correct with AND
		  max_salary > 999 AND max_salary < 10001
		  ```
- What is the syntax for a recursive CTE?
  collapsed:: true
	- #card
		- RECURSIVE CTE ?
		  ```sql
		  WITH RECURSIVE cte_name AS (
		  -- Initial query
		  SELECT initial_columns 
		  FROM initial_table 
		  WHERE initial_conditions
		  
		  UNION ALL
		  
		  -- Recursive query
		  SELECT recursive_columns 
		  FROM some_table 
		  JOIN cte_name ON join_condition 
		  WHERE recursive_conditions
		  ) 
		  SELECT * FROM cte_name;
		  
		  -------------------------------
		  implemention=>
		  
		  WITH RECURSIVE number_sequence AS (
		      -- Base case
		      SELECT 1 AS n
		  
		      UNION ALL
		  
		      -- Recursive step
		      SELECT n + 1
		      FROM number_sequence
		      WHERE n < 10
		  )
		  SELECT n
		  FROM number_sequence;
		  
		  ```
- What's the difference between a Semi Join vs Left Join vs Anti join?
  collapsed:: true
	- #card
		- **When to Use:**
			- **Semi Join:** When you want to filter based on existence ("Show me customers WHO HAVE orders") without duplicates or right table data
			- **Left Join:** When you need data from both tables, want all left table rows, or need to identify rows without matches
			- example
				- ```sql
				  -- INPUT TABLES:
				  -- Customers:
				  -- customer_id | name
				  -- 1           | Alice
				  -- 2           | Bob
				  -- 3           | Carol
				  
				  -- Orders:
				  -- customer_id | order_id
				  -- 1           | 101
				  -- 1           | 102
				  -- 1           | 103
				  -- 2           | 104
				  
				  -- Semi Join (customers who HAVE orders)
				  SELECT *
				  FROM customers c
				  WHERE EXISTS (
				  SELECT 1
				  FROM orders o
				  WHERE o.customer_id = c.customer_id
				  );
				  -- Result:
				  -- customer_id | name
				  -- 1           | Alice    ← appears once despite 3 orders
				  -- 2           | Bob      ← Carol excluded (no orders)
				  
				  -- Anti-Semi Join (customers WITHOUT orders)
				  SELECT *
				  FROM customers c
				  WHERE NOT EXISTS (
				  SELECT 1
				  FROM orders o
				  WHERE o.customer_id = c.customer_id
				  );
				  -- Result:
				  -- customer_id | name
				  -- 3           | Carol    ← only customers with NO orders
				  
				  -- Left Join (all customers with their orders)
				  SELECT c.*, o.order_id
				  FROM customers c
				  LEFT JOIN orders o ON c.customer_id = o.customer_id;
				  -- Result:
				  -- customer_id | name  | order_id
				  -- 1           | Alice | 101      ← Alice repeated 3 times
				  -- 1           | Alice | 102
				  -- 1           | Alice | 103
				  -- 2           | Bob   | 104
				  -- 3           | Carol | NULL     ← Carol included with NULL
				  ```
- SQL NULL Behavior - When you join using a column and if it has nulls
  collapsed:: true
	- #card
	  
	  ```
	  NULL comparisons return NULL (which evaluates as FALSE in WHERE clauses)
	  NULL = NULL  -- Returns NULL (treated as FALSE in conditions)
	  NULL != NULL -- Returns NULL (also treated as FALSE)
	  		
	  		-- Example with JOINs:
	  		-- INPUT TABLES:
	  		-- Table A: id | name          Table B: id | status
	  		--          1  | Alice                1  | Active
	  		--          2  | Bob                  NULL | Pending
	  		--          NULL | Charlie             3  | Inactive
	  		
	  		-- INNER JOIN with NULL values
	  		SELECT a.name, b.status
	  		FROM table_a a
	  		INNER JOIN table_b b ON a.id = b.id;
	  		-- Result: Only Alice (id=1) appears
	  		-- Rows with NULL ids are excluded because NULL = NULL is FALSE
	  		
	  		-- To check for NULL, use IS NULL or IS NOT NULL
	  		WHERE column_name IS NULL      -- Correct way
	  		WHERE column_name = NULL       -- Wrong! Always returns no results
	          
	  
	  ```
- Outer join with exclusion
	- #card\
		- ```sql
		  Common Use => OUTER JOIN with Exclusion
		  
		  -- Find records in source system but NOT in target system (after migration)
		  SELECT 
		      src.record_id,
		      src.record_type,
		      src.created_date
		  FROM SourceSystem src
		  LEFT OUTER JOIN TargetSystem tgt
		    ON src.record_id = tgt.record_id
		  WHERE tgt.record_id IS NULL;
		  ```
