## Endpoints

* **Create Admin Account form CLI**

```bash
$ python manage.py createsuperuser --email youremail@domain.com --username your_username
```

then enter password



1.  **Create user account** (*v1/account/register*)

snd **POST** request to 'http://127.0.0.1:8080/api/v1/account/register'

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

2. **Generate Token **(*v1/token/'*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/token/' with below JSON will generate token

```
{
	"email": "email@example.com",
	"password": "example"
}
```



3. **To get the refresh Token for the user ** (*v1/token/refresh/*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/token/refresh/' with JSON as below

```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCdhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzY0NzM4NiwiaWF0IjoxNjUxMDU1Mzg2LCJqdGkiOiI0ZDIxYjEzNGNlYTk0ZDlfYmI5ZTIyMDk1NjQ0ZDJiYSIsInVzZXJfaWQiOjJ9.wnWxjWBUq4uauFNvxkTkAq-G3g4BfJhZASkSRgneIQc"
}
```



4. **To logout the user** (*v1/account/logout*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/account/logout' with **bearer token**



5. **To know whether user is invited or not ** (*v1/email*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/email' with below JSON will generate token

```
{
  	"email" : "email@example.com"
}
```

6. **To get the user's information** (*v1/users*)

send **GET** request to 'http://127.0.0.1:8080/api/v1/users'  with **bearer token**



7. **To get the information of all the books available** (*v1/books*)

send **GET** request to 'http://127.0.0.1:8080/api/v1/books'  



8. **To post the book details ** (*v1/create/book*)

send **POST** request 'http://127.0.0.1:8080/api/v1/create/book' with **bearer token** and **Multipart Form** as below

```
banme : "book name"
user = ["1"]
author = "author name"
revision = "4th"
publication = "publication name"
category = 	"Bachelors"
subcategory = "CSIT"
image = upload image using FormData
description = "description for the book"

```



9. **To view the profile** (*v1/account/profile*)

send **GET** request to 'http://127.0.0.1:8080/api/v1/account/profile' with **bearer token**



10. **To invite the users** (*v1/invite*)

send **POST** request to 'http://127.0.0.1:8080/api/v1/invite' with **bearer token** and **JSON** as below

```
{
	"email" : "hello@gmail.com"
}
```



11. **To mark book to be sold**  (*v1/flagsold*)

send **POST** request to "http://127.0.0.1:8080/api/v1/flagsold" with **bearer token** and **JSON** as below

```
{
	"bid":2,
	"bflag":1
}
```



12. **To  transfer credit **(*v1/transfer*)

send **POST** request to "http://127.0.0.1:8080/api/v1/transfer" with **bearer token** and **JSON** as below

```
{
	"bowner":1,
	"bid":1
}
```

13. **To  update book** (*v1/account/profile/edit*)

send **POST**  request to "http://127.0.0.1:8080/api/v1/account/profile/edit"  with **bearer token **and **JSON** as below

```
{
	"first_name": "anukul-updated",
	"last_name": "adhikari-updated",
	"phone": 9862327724,
	"note": null
}
```





14. **To get the detail of single book **(*v1/book*)

send **POST** request to "http://127.0.0.1:8080/api/v1/book"  with **bearer token **and **JSON** as below

```
{
		"id": 1
}
```





