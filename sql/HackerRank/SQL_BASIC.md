

![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)



1. Query all columns for all American cities in the **CITY** table with populations larger than `100000`. The **CountryCode** for America is `USA`.

```SQL
SELECT * FROM CITY WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';
```



2. Query the **NAME** field for all American cities in the **CITY** table with populations larger than `120000`. The *CountryCode* for America is `USA`.

```SQL
SELECT NAME FROM CITY WHERE POPULATION >120000 AND COUNTRYCODE = 'USA';
```



3. Query all columns (attributes) for every row in the **CITY** table.

```SQL
SELECT * FROM CITY;
```



4. Query all columns for a city in **CITY** with the *ID* `1661`.

```SQL
SELECT * FROM CITY WHERE ID = '1661';
```



5. Query all attributes of every Japanese city in the **CITY** table. The **COUNTRYCODE** for Japan is `JPN`.

```SQL
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';
```



6. Query the names of all the Japanese cities in the **CITY** table. The **COUNTRYCODE** for Japan is `JPN`.

```SQL
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';
```



7. Query the average population for all cities in **CITY**, rounded *down* to the nearest integer.

```sql
SELECT ROUND(AVG(POPULATION)) FROM CITY;
```



8. Query a *count* of the number of cities in **CITY** having a *Population* larger than 100000

```SQL
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000; 
```



9. Query the total population of all cities in **CITY** where *District* is **California**.

```sql
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California'
```



10. Query the average population of all cities in **CITY** where *District* is **California**.

```sql
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT='California'
```



11. Query the sum of the populations for all Japanese cities in **CITY**. The *COUNTRYCODE* for Japan is **JPN**.

```SQL
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN'
```





![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)



1. Query a list of **CITY** and **STATE** from the **STATION** table.

```SQL
SELECT CITY, STATE FROM STATION;
```



2. Query a list of **CITY** names from **STATION** for cities that have an even **ID** number. Print the results in any order, but exclude duplicates from the answer.

```SQL
SELECT DISTINCT CITY FROM STATION WHERE ID % 2 = 0;
```



3. Find the difference between the total number of **CITY** entries in the table and the number of distinct **CITY** entries in the table.

```SQL
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;
```



4. Query the list of *CITY* names starting with vowels (i.e., `a`, `e`, `i`, `o`, or `u`) from **STATION**. Your result *cannot* contain duplicates.

```sql
SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE 'a%' OR CITY LIKE 'e%' OR CITY LIKE 'i%' OR CITY LIKE 'o%' OR CITY LIKE 'u%';
```



5. Query the list of *CITY* names ending with vowels (a, e, i, o, u) from **STATION**. Your result *cannot* contain duplicates.

```SQL
SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' OR CITY LIKE '%u';
```



6. ★Query the list of *CITY* names from **STATION** which have vowels (i.e., *a*, *e*, *i*, *o*, and *u*) as both their first *and* last characters. Your result cannot contain duplicates.

```SQL
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[aeiou]$' and CITY REGEXP '^[aeiou]';
```

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(city,1) in ('a', 'e', 'i', 'o', 'u') AND RIGHT(city,1) in ('a', 'e', 'i', 'o', 'u')
```



7. Query the list of *CITY* names from **STATION** that *do not start* with vowels. Your result cannot contain duplicates.

```SQL
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT LIKE 'a%' AND CITY NOT LIKE 'e%' AND CITY NOT LIKE 'i%' AND CITY NOT LIKE 'o%' AND CITY NOT LIKE 'u%';
```



8. Query the list of *CITY* names from **STATION** that *do not end* with vowels. Your result cannot contain duplicates.

```SQL
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT LIKE '%a' AND CITY NOT LIKE '%e' AND CITY NOT LIKE '%i' AND CITY NOT LIKE '%o' AND CITY NOT LIKE '%u';
```



9. ★Query the list of *CITY* names from **STATION** that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(city,1) not in ('a', 'e', 'i', 'o', 'u') OR RIGHT(city,1) not in ('a', 'e', 'i', 'o', 'u')
```

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiou]' OR CITY REGEXP '[^aeiou]$'
```



10. Query the list of *CITY* names from **STATION** that *do not start* with vowels and *do not end* with vowels. Your result cannot contain duplicates.

```
SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u') AND RIGHT(CITY,1) NOT IN ('a','e','i','o','u')
```



11. Query the *Western Longitude* (*LONG_W*) for the largest *Northern Latitude* (*LAT_N*) in **STATION** that is less than 137.2345. Round your answer to decimal places.

```sql
SELECT ROUND(LONG_W,4) FROM STATION WHERE LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1
```



12. Query the following two values from the **STATION** table:
    1. The sum of all values in *LAT_N* rounded to a scale of decimal places.
    2. The sum of all values in *LONG_W* rounded to a scale of decimal places.

```SQL
SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2) FROM STATION
```



13. Query the sum of *Northern Latitudes* (*LAT_N*) from **STATION** having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.

```python
SELECT TRUNCATE(SUM(LAT_N),4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345
```



![](https://s3.amazonaws.com/hr-challenge-images/12896/1443815243-94b941f556-1.png)



1. Query the *Name* of any student in **STUDENTS** who scored higher than *Marks*. Order your output by the *last three characters* of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending *ID*.

```SQL
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(NAME,3), ID ASC
```



![](https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png)



1. Write a query that prints a list of employee names (i.e.: the *name* attribute) from the **Employee** table in alphabetical order.

```sql
SELECT NAME FROM Employee ORDER BY NAME
```



2. Write a query that prints a list of employee names (i.e.: the *name* attribute) for employees in **Employee** having a salary greater than per month who have been employees for less than months. Sort your result by ascending *employee_id*.

```SQL
SELECT NAME FROM Employee WHERE SALARY > 2000 AND MONTHS < 10 ORDER BY EMPLOYEE_ID
```



