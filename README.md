This is a fully containerized RESTful API created with dgango rest framework. The goal is to build and deploy a microservice api/architecture. 

Steps to run
1. Create virtual env 
2. Install dependencies
3. Run django server

At teh moment you have to log in as Admin in admin panel then check the api

# Here's a breakdown of the API structure
| Endpoit             | GET           |           POST           | PUT      |  DEELETE
| :---:               | :---:                    | :---:         |:---:     | :---: 
| blog/api            | LIst all blogs           | Creates blog  | N/A      | N/A
| :---:               | :---:                    | :---:         |:---:     | :---: 
| blog/api<int:blog_id>|Retrieves with given ID  | N/A           |    Updates      | Deletes


on the api endpoint try posting with this
{
    "blog_title": "This is a blog title",
    "blog_body": ""This is a blog body""
}


Running with Docker
1. Run
docker build . -t todayilearn-v0.0
--> 8181 is host port  || 4000 is container port <--
docker run -d -p 8181:4000 todayilearn-v1.0

## Workflow
# Backend
Models in django populate/handle the db
Serializers get data from db (through/from models) and serializes to json
Views just handles requests

# Frontend
react-router-dom handles navigation
npx create-react-app frontend used to create react app



# Tips
Run:
docker-machine ls
docker inspect todayilearn-v1.0
To check everything is working
