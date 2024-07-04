
CREATE TABLE Customers(
ID INT,
Gender VARCHAR(20),
Ever_Married VARCHAR (5),
Age int,
Graduated varchar (5), 
Profession varchar (30),
Work_Experience float,
Spending_Score varchar (20),
Family_Size float,
Var_1 varchar (20)
)

BULK INSERT Customers
	FROM 'C:\Users\weronika00\Downloads\archive (1)\Test.csv'
	WITH
		(FIRSTROW=2,
		FIELDTERMINATOR = ',',
		ROWTERMINATOR = '\n');
GO

SELECT *
FROM Customers

SELECT DISTINCT *
FROM Customers

ALTER TABLE Customers DROP COLUMN Var_1

--grouping customers by their professions
SELECT Profession, Spending_Score
FROM Customers 
WHERE Profession IS NOT NULL
GROUP BY Profession, Spending_Score
ORDER BY Spending_Score
--which profession has the highest spending score? 
SELECT Profession, Spending_Score
FROM Customers 
WHERE Profession IS NOT NULL AND Spending_Score= 'High'
GROUP BY Profession, Spending_Score

--giving age group for all customers
SELECT Spending_Score, 
CASE
	WHEN Age <25 then 'below 25'
	WHEN Age BETWEEN 25 AND 36 then '25-36'
	WHEN Age BETWEEN 37 AND 46 then  '37-46'
	ELSE '>46'
END AS AgeGroup
FROM Customers
ORDER BY AgeGroup DESC


-- do people in marriage spend more?
SELECT COUNT(ID) as PeopleCount, Ever_Married, Spending_Score 
FROM Customers
WHERE Ever_Married IS NOT NULL
GROUP BY Ever_Married, Spending_Score
ORDER BY PeopleCount desc
--all people in low spending_score are not married 
--conclusion: people in marriage are better potential clients, because they spend more


--which profession buys most often, which group of client's professions are NOT in marriage?
SELECT COUNT(ID) as PeopleCount, Ever_Married, Profession
FROM Customers
WHERE Ever_Married IS NOT NULL AND Profession IS NOT NULL
GROUP BY Ever_Married, Profession
ORDER BY PeopleCount desc
--Artists buy more often + they have high Spending_Score
--People in Healthcare are the largest group without marriage, 
--so the could be "worse" potential clients because of the previous analysis and conclusion


--which profession group is mostly graduated?
SELECT COUNT(ID) as PeopleCount, Profession, Graduated
FROM Customers
WHERE Profession IS NOT NULL AND Graduated IS NOT NULL
GROUP BY Profession, Graduated
ORDER BY PeopleCount DESC
--Artists are mostly graduated


--who are better potential clients, women or men? 
SELECT Count(Gender) as GenderCount, Gender, Spending_Score
FROM Customers
GROUP BY Gender, Spending_Score
ORDER BY GenderCount desc
--Men are higher in each Spending_Score category, more "Beauty" products could increase sale in women section


--Average age, work expierence and family size for all customers
SELECT AVG(Age) as AgeAvg, ROUND(AVG(Work_Experience),2) as WorkExpAvg, ROUND(AVG(Family_Size),2) as FamilySizeAvg
FROM Customers

-- do people with big family spend more?
SELECT Family_Size, COUNT(Spending_Score) as SpendCount, Spending_Score
FROM Customers
WHERE Family_Size>3
GROUP BY Family_Size, Spending_Score
ORDER BY Family_Size desc
--almost in each family size low spending score has the most people



















