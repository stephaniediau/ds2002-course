USE ntq7zt_db;

SELECT
    students.name,
    students.home_state,
    dinners.food,
    dinners.drink
FROM students
JOIN dinners
ON students.student_id = dinners.student_id
WHERE dinners.drink = 'Water';
