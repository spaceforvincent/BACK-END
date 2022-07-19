![](https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png)

1. Write a query to find the *maximum total earnings* for all employees as well as the total number of employees who have maximum total earnings.

```sql
/*
1. salary * months = earnings
2. 각 earning 별로 몇 명이 그만큼 벌었는지 계산(Group by)
3. earning 중에 가장 큰 값을 가져온다
*/

SELECT salary * months as earnings, count(*)
FROM employee
GROUP BY earnings
ORDER BY earnings DESC 
LIMIT 1
```



![](https://s3.amazonaws.com/hr-challenge-images/12887/1443815827-cbfc1ca12b-2.png)

1. Write a query identifying the *type* of each record in the **TRIANGLES** table using its three side lengths. 

```sql
select case when (a = b and b = c) then 'Equilateral'
            when a + b <= c or a + c <= b or b + c <= a then 'Not A Triangle'
            when (a = b and b!= c) or (a = c and b!= c) or (b = c and a!= c) then 'Isosceles'
            when a != b and a!= c and b != c then 'Scalene'   
       end
from triangles
```





```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
```

1. Write an SQL query to reformat the table such that there is a department id column and a revenue column **for each month**.

```sql
select id, 
    sum(case when month = 'Jan' then revenue else null end) as Jan_Revenue,
    sum(case when month = 'Feb' then revenue else null end) as Feb_Revenue,
    sum(case when month = 'Mar' then revenue else null end) as Mar_Revenue,
    sum(case when month = 'Apr' then revenue else null end) as Apr_Revenue,
    sum(case when month = 'May' then revenue else null end) as May_Revenue,
    sum(case when month = 'Jun' then revenue else null end) as Jun_Revenue,
    sum(case when month = 'Jul' then revenue else null end) as Jul_Revenue,
    sum(case when month = 'Aug' then revenue else null end) as Aug_Revenue,
    sum(case when month = 'Sep' then revenue else null end) as Sep_Revenue,
    sum(case when month = 'Oct' then revenue else null end) as Oct_Revenue,
    sum(case when month = 'Nov' then revenue else null end) as Nov_Revenue,
    sum(case when month = 'Dec' then revenue else null end) as Dec_Revenue
from department group by id
```

![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

![](https://s3.amazonaws.com/hr-challenge-images/8342/1449769013-e54ce90480-Country.jpg)

1. Given the **CITY** and **COUNTRY** tables, query the names of all cities where the *CONTINENT* is *'Africa'*. 

   **Note:** *CITY.CountryCode* and *COUNTRY.Code* are matching key columns.

```sql
SELECT CITY.NAME
FROM CITY INNER JOIN COUNTRY on CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = 'Africa'
```

2. Given the **CITY** and **COUNTRY** tables, query the sum of the populations of all cities where the *CONTINENT* is *'Asia'*.

```sql
select sum(city.population)
from city inner join country on city.countrycode=country.code
where country.continent='Asia'
```

3. Given the **CITY** and **COUNTRY** tables, query the names of all the continents (*COUNTRY.Continent*) and their respective average city populations (*CITY.Population*) rounded *down* to the nearest integer.

```sql
select country.continent, floor(avg(city.population))
from city inner join country on city.countrycode = country.code
group by country.continent
```



```

//customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

//orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
```

1. Write an SQL query to report all customers who never order anything.

```sql
select customers.name as Customers
from customers left join orders on customers.id = orders.customerid
where orders.id is null
```



```
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
```

1. Write an SQL query to find the employees who earn more than their managers.

```sql
select employee.name as Employee
from employee inner join employee as manager on employee.managerid = manager.id
where employee.salary > manager.salary 
```





```
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
```



1. Write an SQL query to find all dates' `Id` with higher temperatures compared to its previous dates (yesterday).

```sql
select today.id
from weather as today inner join weather as yesterday on today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
where today.temperature > yesterday.temperature
```



![](https://s3.amazonaws.com/hr-challenge-images/12892/1443818693-b384c24e35-2.png)

1. Two pairs *(X1, Y1)* and *(X2, Y2)* are said to be *symmetric* *pairs* if *X1 = Y2* and *X2 = Y1*.

   Write a query to output all such *symmetric* *pairs* in ascending order by the value of *X*. List the rows such that *X1 ≤ Y1*.

```sql
select x,y
from functions
where x = y
group by x, y
having count(*) = 2

UNION 

select x_functions.x, x_functions.y
from functions as x_functions inner join functions as y_functions on x_functions.y = y_functions.x and x_functions.x = y_functions.y
where x_functions.x < x_functions.y
order by x
```

