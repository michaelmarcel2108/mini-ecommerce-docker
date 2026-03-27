CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    weight FLOAT NOT NULL,
    category VARCHAR(100) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO products (name, price, weight, category, stock) VALUES
('Laptop', 1000, 2.0, 'Elektronik', 5),
('Phone', 500, 1.0, 'Elektronik', 20),
('Meja Belajar', 150, 15.0, 'Furnitur', 2);