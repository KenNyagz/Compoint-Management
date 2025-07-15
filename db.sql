CREATE DATABASE IF NOT EXISTS compoint_db;
USE compoint_db;

CREATE USER IF NOT EXISTS kennyaga IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON compoint_db.* TO kennyaga;
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Product VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL,
    Selling_price DECIMAL(10, 2) NOT NULL,
    Cost_price DECIMAL(10, 2) NOT NULL);

/*INSERT INTO inventory (Product, Category, Quantity, Selling_price, Cost_price)
VALUES(,,,,,);*/