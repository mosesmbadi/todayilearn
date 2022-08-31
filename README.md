This is a fully containerized RESTful API created with dgango rest framework. The goal is to build and deploy a microservice api/architecture. 

Steps to run
1. Create virtual env 
2. Install dependencies
3. Run django server


# Here's a breakdown of the API structure
| Endpoit             | GET           |           POST           | PUT      |  DEELETE
| :---:               | :---:                    | :---:         |:---:     | :---: 
| blog/api            | LIst all blogs           | Creates blog  | N/A      | N/A
| :---:               | :---:                    | :---:         |:---:     | :---: 
| blog/api<int:blog_id>|Retrieves with given ID  | N/A           |    Updates      | Deletes