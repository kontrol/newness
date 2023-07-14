# Database Schema

# Tables
Brand              CompanyProduct     Product          
Company            Image              ProductIngredient
CompanyBrand       Ingredient         Proxy  

# Brand
CREATE TABLE Brand (
id INTEGER PRIMARY KEY,
name TEXT UNIQUE);

# Company
CREATE TABLE Company (
id INTEGER PRIMARY KEY,
name TEXT,
url TEXT
, brand_list_url TEXT);

# Ingredient
CREATE TABLE Ingredient (
id INTEGER PRIMARY KEY,
name TEXT);

# Product
CREATE TABLE Product (
id INTEGER PRIMARY KEY,
name TEXT,
brand_id INTEGER,
FOREIGN KEY (brand_id) REFERENCES Brand(id)
);

# CompanyBrand
CREATE TABLE CompanyBrand(
id INTEGER PRIMARY KEY,
company_id INTEGER,
brand_id INTEGER,
total_sales REAL,
exclusive BOOLEAN, 
company_brand_url TEXT,
FOREIGN KEY (company_id) REFERENCES Company(id),
FOREIGN KEY (brand_id) REFERENCES Brand(id)
);

# CompanyProduct
CREATE TABLE CompanyProduct(
id INTEGER PRIMARY KEY,
company_id INTEGER,
product_id INTEGER,
price REAL,
quantity INTEGER,
restock_trigger INTEGER,
product_url TEXT,
FOREIGN KEY (company_id) REFERENCES Company(id),
FOREIGN KEY (product_id) REFERENCES Product(id)
);

# ProductIngredient
CREATE TABLE ProductIngredient (
    product_id INTEGER,
    ingredient_id INTEGER,
    PRIMARY KEY (product_id, ingredient_id),
    FOREIGN KEY (product_id) REFERENCES Product(id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(id)
);

# Image
CREATE TABLE Image(
id INTEGER PRIMARY KEY,
product_id INTEGER,
location TEXT,
FOREIGN KEY (product_id) REFERENCES Product(id)
);

# Proxy
CREATE TABLE Proxy(
id INTEGER PRIMARY KEY,
ip_address TEXT,
port INTEGER,
type TEXT CHECK (type in ('Elite', 'Transparent', 'Anonymous')),
ssl BOOLEAN
);