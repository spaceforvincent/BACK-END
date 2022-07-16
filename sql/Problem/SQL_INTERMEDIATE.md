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

