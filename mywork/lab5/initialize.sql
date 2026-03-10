USE ntq7zt_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    home_state VARCHAR(30),
    age INT
);

CREATE TABLE dinners (
    dinner_id INT PRIMARY KEY,
    student_id INT,
    food VARCHAR(100),
    drink VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO students VALUES
(1,'Stephanie','Virginia',20),
(2,'June','Alaska',21),
(3,'Millie','New York',18),
(4,'Julia','Maine',19),
(5,'Ana','Pennsylvania',23),
(6,'Rachel','Maryland',22),
(7,'Paul','California',18),
(8,'Oliver','North Carolina',21),
(9,'Ivan','Michigan',20),
(10,'Kevin','Maryland',19);

INSERT INTO dinners VALUES
(101,1,'Shrimp Bowl','Peach Juice'),
(102,2,'Pasta','Coke'),
(103,3,'Chili','Orange Juice'),
(104,4,'Pizza','Milk Tea'),
(105,5,'Japchae','Water'),
(106,6,'Steak','Lemonade'),
(107,7,'Mapo Tofu','Orange Juice'),
(108,8,'Salad','Water'),
(109,9,'Curry','Water'),
(110,10,'Bagel','Tea');

