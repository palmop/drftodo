# todo app
Simple todo app .

## with docker-compose
Start it with   
    
    `docker-compose up --build` 

## in local machine without docker-compose
create .env environment:

`cp .env.example .env`  

set **DATABASE_URL** to the value for your database.

than 

`pipenv shell`
`pipenv install`
`./init.sh`


## use it
- docs: http://0.0.0.0:8000/
- swagger api : http://0.0.0.0:8000/swagger
- swagger json to import in postman : http://0.0.0.0:8000/swagger
- REST API : http://0.0.0.0:8000/api/todos/

