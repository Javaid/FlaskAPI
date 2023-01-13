# FlaskAPI
This is a simple Flask based API that demonstrates how to build a RESTful API in Python using the Flask web framework.

# Requirements
Python 3.x <br />
Flask <br />
Flask-RESTful <br />
Flask-SQLAlchemy (if using a database) <br />
# Installation
Clone the repository: git clone https://github.com/javaid/flask-api.git
Install the required packages: pip install -r requirements.txt  <br />
# Usage
Run the application: python app.py <br />
Test the API using a tool such as Postman or curl. <br />
# Endpoints
The following endpoints are available: <br />

GET /: Returns a simple message to check if the API is up and running <br />
GET /items: Returns a list of items <br />
GET /items/<id>: Returns a specific item by id <br />
POST /items: Creates a new item <br />
PUT /items/<id>: Updates an existing item by id <br />
DELETE /items/<id>: Deletes an existing item by id <br />
  
# Examples
**Retrieve a list of items:**  <br />
  curl -X GET http://localhost:5000/items <br />
**Retrieve a specific item by id:** <br />

curl -X GET http://localhost:5000/items/1 <br />
**Create a new item:** <br />

curl -X POST -H "Content-Type: application/json" -d '{"name":"item name", "description":"item description"}' http://localhost:5000/items <br />
**Update an existing item by id:** <br />

curl -X PUT -H "Content-Type: application/json" -d '{"name":"updated item name", "description":"updated item description"}' http://localhost:5000/items/1 <br />
**Delete an existing item by id:** <br />

curl -X DELETE http://localhost:5000/items/1 <br />
