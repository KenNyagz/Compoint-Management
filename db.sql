CREATE DATABASE IF NOT EXISTS compoint_db;
USE compoint_db;

CREATE USER IF NOT EXISTS kennyaga IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON compoint_db.* TO kennyaga;
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Product VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL DEFAULT 1,
    Specifications TEXT NOT NULL,
    Buying_price DECIMAL(10, 2) NOT NULL,
    Selling_price DECIMAL(10, 2) NOT NULL);

/*INSERT INTO inventory (Product, Category, Quantity, Specifications, Buying_price, Selling_price)
VALUES('Laptop', 'Electronics', 10, '15-inch display, 16GB RAM', 1000.00, 1200.00),
      ('Smartphone', 'Electronics', 50, '6-inch display, 128GB storage', 300.00, 400.00),
      ('Headphones', 'Accessories', 100, 'Noise-cancelling, wireless', 50.00, 80.00),
      ('Monitor', 'Electronics', 20, '24-inch, Full HD', 200.00, 250.00),
      ('Keyboard', 'Accessories', 150, 'Mechanical, RGB backlit', 70.00, 100.00);*/