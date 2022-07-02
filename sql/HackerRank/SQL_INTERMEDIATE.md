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

