from cs50 import SQL
db = SQL("sqlite:///dataset.db")

db.execute('''CREATE TABLE dataset (ID INT, Age INT, BusinessTravel VARCHAR(17), Department VARCHAR(22), DistanceFromHome INT, Education INT, EducationField VARCHAR(16), Gender VARCHAR(6), JobRole VARCHAR(25), JobSatisfaction INT, MaritalStatus VARCHAR(8), MonthlyIncome INT, NumCompaniesWorked INT, OverTime VARCHAR(3), PercentSalaryHike INT, YearsInCurrentRole INT, YearsSinceLastPromotion INT)''')

db.execute('''INSERT INTO dataset VALUES
    (0,30,'Travel_Rarely','Research & Development',9,2,'Medical','Male','Laboratory Technician',3,'Single',2206,1,'No',13,0,1),
    (1,39,'Travel_Rarely','Sales',5,3,'Technical Degree','Male','Sales Representative',4,'Married',2086,3,'No',14,0,0),
    (2,24,'Travel_Rarely','Sales',3,2,'Other','Female','Sales Executive',3,'Married',4999,0,'No',21,2,0),
    (3,25,'Travel_Rarely','Sales',5,3,'Marketing','Male','Sales Executive',3,'Single',5744,1,'Yes',11,4,0),
    (4,51,'Travel_Rarely','Research & Development',6,3,'Life Sciences','Male','Research Director',3,'Single',19537,7,'No',13,18,15),
    (5,37,'Travel_Frequently','Sales',4,4,'Marketing','Male','Sales Representative',4,'Divorced',2793,4,'No',17,8,5),
    (6,28,'Travel_Rarely','Research & Development',9,3,'Medical','Male','Research Scientist',4,'Married',2070,1,'No',23,2,0),
    (7,33,'Travel_Frequently','Sales',10,3,'Marketing','Male','Sales Executive',4,'Single',4682,3,'No',14,7,0),
    (8,57,'Travel_Rarely','Research & Development',1,4,'Medical','Male','Healthcare Representative',3,'Married',6755,2,'No',11,2,1),
    (9,46,'Non-Travel','Research & Development',7,4,'Medical','Female','Manufacturing Director',3,'Married',5258,2,'No',14,0,0),
    (10,56,'Travel_Frequently','Sales',6,3,'Life Sciences','Female','Sales Executive',1,'Married',13212,9,'No',11,7,7),
    (11,39,'Travel_Rarely','Human Resources',3,3,'Human Resources','Female','Human Resources',2,'Married',6389,9,'No',15,3,3),
    (12,33,'Travel_Rarely','Research & Development',7,3,'Medical','Male','Research Director',3,'Married',11691,0,'No',11,9,3),
    (13,33,'Travel_Rarely','Sales',16,3,'Marketing','Female','Sales Executive',1,'Single',5324,5,'No',15,2,0),
    (14,32,'Travel_Rarely','Sales',13,4,'Life Sciences','Male','Sales Executive',4,'Divorced',4403,2,'No',11,2,0),
    (15,37,'Travel_Rarely','Research & Development',11,2,'Medical','Female','Healthcare Representative',2,'Married',4777,5,'No',15,0,0),
    (16,37,'Travel_Rarely','Research & Development',25,2,'Medical','Female','Healthcare Representative',4,'Divorced',5731,7,'No',13,2,1),
    (17,56,'Travel_Rarely','Research & Development',4,4,'Technical Degree','Female','Manager',1,'Divorced',19943,4,'No',13,2,4),
    (18,20,'Travel_Rarely','Sales',21,3,'Marketing','Male','Sales Representative',4,'Single',2678,1,'No',17,1,2),
    (19,25,'Travel_Rarely','Sales',10,4,'Life Sciences','Male','Sales Executive',4,'Single',4950,0,'No',14,3,1),
    (20,31,'Non-Travel','Sales',2,4,'Life Sciences','Female','Sales Executive',3,'Divorced',9852,1,'Yes',19,8,9),
    (21,51,'Travel_Rarely','Research & Development',11,2,'Technical Degree','Female','Manufacturing Director',2,'Single',13142,3,'No',16,2,0),
    (22,51,'Travel_Frequently','Sales',2,3,'Marketing','Male','Sales Executive',2,'Married',10596,2,'No',11,2,3),
    (23,26,'Travel_Rarely','Research & Development',2,1,'Medical','Male','Research Scientist',4,'Single',3904,0,'No',12,3,1),
    (24,45,'Travel_Rarely','Research & Development',28,3,'Technical Degree','Male','Research Scientist',4,'Married',2132,4,'No',20,4,0),
    (25,23,'Travel_Rarely','Sales',7,3,'Life Sciences','Male','Sales Representative',4,'Divorced',2275,1,'Yes',21,2,0),
    (26,38,'Travel_Rarely','Sales',2,4,'Marketing','Female','Sales Representative',4,'Married',5405,2,'Yes',20,2,0),
    (27,44,'Travel_Rarely','Research & Development',1,4,'Life Sciences','Male','Healthcare Representative',1,'Married',5033,2,'No',15,0,2),
    (28,28,'Travel_Rarely','Research & Development',17,3,'Technical Degree','Male','Laboratory Technician',4,'Divorced',2367,5,'No',12,1,0),
    (29,34,'Travel_Rarely','Research & Development',8,3,'Medical','Male','Laboratory Technician',3,'Married',4404,2,'No',12,3,1)''')

rows = db.execute("SELECT * FROM dataset")
for row in rows:
    print(row)
