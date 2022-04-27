## Endpoints

* **Create Admin Account form CLI**

```bash
$ python manage.py createsuperuser --email youremail@domain.com --username your_username
```

then enter password



* **Create user account** (*v1/account/register*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/account/register'

```
{
	"email" : "email@example.com",
	"user_name":"username",
	"password":"example",
	"password2":"example",
	"first_name":"Richard",
	"last_name":"Hendricks"
}
```

* **Generate Token **(*v1/token/'*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/token/' with below JSON will generate token 

```
{
	"email": "email@example.com",
	"password": "example"
}
```



* **To get the refresh Token for the user ** (*v1/token/refresh/*)

  send **POST** request to 'http://127.0.0.1:8080/api/v1/token/refresh/' with JSON as below

  ```
  {
  	"refresh": "eyJ0eXAiOiJKV1QiLCdhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzY0NzM4NiwiaWF0IjoxNjUxMDU1Mzg2LCJqdGkiOiI0ZDIxYjEzNGNlYTk0ZDlfYmI5ZTIyMDk1NjQ0ZDJiYSIsInVzZXJfaWQiOjJ9.wnWxjWBUq4uauFNvxkTkAq-G3g4BfJhZASkSRgneIQc"
  }
  ```

  

* **To logout the user** (*v1/account/logout*)

  send **POST** request to 'http://127.0.0.1:8080/api/v1/account/logout' with **bearer token**






* **To know whether user is invited or not ** (*v1/email*)

  send **POST** request to 'http://127.0.0.1:8080/api/v1/email' with below JSON will generate token 

  ```
  {
  	"email" : "email@example.com"
  }
  ```






* **To get the user's information** (*v1/users*)

  send **GET** request to 'http://127.0.0.1:8080/api/v1/users'  with **bearer token** 







* **To get the information of all the books available** (*v1/books*)

  send **GET** request to 'http://127.0.0.1:8080/api/v1/books'  





* **To post the book details ** (*v1/create/book*)

​		send **POST** request 'http://127.0.0.1:8080/api/v1/create/book' with **bearer token** and **JSON** as below

```
{
	"bname": "PROLOG for artifical intelligence",
	"author": "Mr fucking gilfoyel ",
	"revision": "4th",
	"publication": " the Nepal publication ",
	"category": [" hello world lekhne "]
}
```







* **To view the profile** (*v1/account/profile*)

send **GET** request to 'http://127.0.0.1:8080/api/v1/account/profile' with **bearer token** 





* **To invite the users** (*v1/invite*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/invite' with **bearer token** and **JSON** as below

```
{
	"email" : "hello@gmail.com"
}
```

