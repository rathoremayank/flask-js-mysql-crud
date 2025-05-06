# flask-js-mysql-crud
Simple Application using Flask, JavaScript and MySQL 

# how to run this app 
1. Run the SQL container
```
docker run --name my-container-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<your-password> -d mysql
````
3. Run Database and Table Creation Scripts
```
CREATE DATABASE flask_crud;
USE flask_crud;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```
5. Run python application
```
python app.py
```
