PRAGMA foreigen_keys = ON;

CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary INTEGER,
    department_id INTEGER,
    age INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);


CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    quantity INTEGER,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
	
);


CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    grade_id INTEGER,
    age INTEGER,
    city TEXT,
    FOREIGN KEY (grade_id) REFERENCES grades(id)
	
);

CREATE TABLE IF NOT EXISTS orders(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product TEXT,
	price INTEGER,
	quantity INTEGER,
	status_id TEXT,
	FOREIGN KEY (status_id) REFERENCES status(id)

);


CREATE TABLE IF NOT EXISTS movies(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT,
	year INTEGER,
	rating_id REAL,
	genre INTEGER,
	FOREIGN KEY (rating_id) REFERENCES rating(id)

);


CREATE TABLE IF NOT EXISTS car(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	brand TEXT,
	madel TEXT,
	year_id INTEGER,
	price INTEGER,
	FOREIGN KEY (year_id) REFERENCES year(id)

);

