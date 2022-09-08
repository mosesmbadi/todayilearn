# todayilearn
This is a fully containerized RESTful API created with dgango rest framework. React is used to show how the RESTfull API can be consumed.
 The goal is to build and deploy a microservice api/architecture. 

Steps to run
1. Create virtual env 
2. Install dependencies
``` 
pip install requirements.txt
```
3. Run django server
```
python manage.py runserver
```

At teh moment you have to log in as Admin in admin panel then check the api

# Here's a breakdown of the API structure
| Endpoit             | GET           |           POST           | PUT      |  DEELETE
| :---:               | :---:                    | :---:         |:---:     | :---: 
| api/                | LIst all blogs           | Creates blog  | N/A      | N/A
| :---:               | :---:                    | :---:         |:---:     | :---: 
| blog/api<int:blog_id>|Retrieves with given ID  | N/A           |    Updates      | Deletes



Running with Docker
1. Run
docker build . -t todayilearn-v0.0
--> 8181 is host port  || 4000 is container port <--
docker run -d -p 8181:4000 todayilearn-v1.0


# Tips
Run:
docker-machine ls
docker inspect todayilearn-v1.0
To check everything is working
