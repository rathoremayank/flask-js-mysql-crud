CREATE DATABASE IF NOT EXISTS flaskcrud;
USE flaskcrud;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
('Aman', 'aman@golmaal.com'),
('Boman', 'boman@golmaal.com');
