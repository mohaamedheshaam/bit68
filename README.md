
Step 1 :  Install dependencies by running these commands  in the project directory 

 -pipenv install django 
 
-pipenv install mysqlclient 

-pipenv install djangorestframework


Step 2:  run comment ‘pipenv shell’ 


Step 3 : In  bit68_task/settings line 83 enter  database password


Steps 4 :  Create database by running in a SQL file  command => CREATE DATABASE bit68_database;



Step 5:  Run command  ‘python manage.py migrate’   in the project directory 


Step 6 : python manage.py createsuperuser  and type your username, email, and password. 


-Now you can login and access  the admin page from  ‘http://127.0.0.1:8000/admin'  which you can create and view products


-After creating products you can access the products created in the database from   ‘http://127.0.0.1:8000/api/products'

	
- Also there is an endpoint to search on a specific product from example : http://127.0.0.1:8000/api/products/jeans’


Step 7: python manage.py createsuperuser  and type your username, email, and password. 


-Users  can register from endpoint   ‘http://127.0.0.1:8000/api/register' and request body example : {"username":"user3","email":"user3@gmail.com","password":"12345678","first_name":"user3","last_name":"user3" }


-Users  can register from endpoint     ‘http://127.0.0.1:8000/api/login' and request body example : {"username":"user3","password":"12345678"}


-Users  also can logout from endpoint     ‘http://127.0.0.1:8000/api/logout'  



-Now if you are logged in as a user you can add to cart and get your cart  by   ‘http://127.0.0.1:8000/api/cart/'  and request body example :  {"pid": "1", "quantity": "1"}



- If you have items in cart you can make order by  ‘http://127.0.0.1:8000/api/order/' if your cart have items 
