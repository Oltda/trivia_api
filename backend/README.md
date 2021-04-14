# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

API Endpoints and Expected Behavior

GET /categories
General:
Returns a dictionary of category objects and success value
Sample: curl http://127.0.0.1:5000/categories

	{"categories":
	{
	"1":"Science",
	"2":"Art",
	"3":"Geography",
	"4":"History",
	"5":"Entertainment",
	"6":"Sports"},
	"success":true}




GET /questions
General:
This endpoint returns a dictionary of all available categories, list of question objects
success value and total number of questions



GET /categories/{category_id}/questions'
General:
This endpoint shows all the questions in a given category specified by the category_id in the url.
It returns a list of category objects, success value, current category, 
a list of question objects in the current category and its length.

sample: curl http://127.0.0.1:5000/categories/2/questions

	{"categories":[
	{"id":1,
	"type":"Science"
	},	
	{
	"id":2,
	"type":"Art"
	},
	{"id":3,
	"type":"Geography"
	},
	{"id":4,
	"type":"History"
	},
	{"id":5,
	"type":"Entertainment"
	},
	{"id":6,
	"type":"Sports"
	}],
	
	"current_category":"Art",
	
	"questions":[
	{
	"answer":"Escher",
	"category":2,
	"difficulty":1,
	"id":16,
	"question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
	},
	{"answer":"Mona Lisa",
	"category":2,
	"difficulty":3,
	"id":17,
	"question":"La Giaconda is better known as what?"
	},
	{
	"answer":"One",
	"category":2,
	"difficulty":4,
	"id":18,
	"question":"How many paintings did Van Gogh sell in his lifetime?"
	},
	{
	"answer":"Jackson Pollock",
	"category":2,
	"difficulty":2,
	"id":19,
	"question":"Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
	}],
	"success":true,
	"total_questions":4} 


DELETE /questions/{question_id}
General:
This endpoint deletes a question with the id specified in the URL if it exists. 
It returns success value and id of the deleted question
Sample: curl http://127.0.0.1:5000/questions/41 -X DELETE

    {"deleted":41,"success":true}

POST /questions
General:
This endpoint creates a new question.
The required input is: question, answer, difficulty score and category id
Returns the id of the new question and success value

Example: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d'{"question":"What is the capital of Germany?", "answer":"Berlin", "difficult":"1", "category":"3"}'

	{
  	"created":45,
  	"success":true
	}


POST /questions/search
General:
This endpoint handles search requests.
It matches all the questions that contain string typed by the user in the form.
Returns a list of question objects, its length and success value

sample: curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d'{"searchTerm": "who"}'

	{
	"questions":[
	{
	"answer":"George Washington Carver",
	"category":4,
	"difficulty":2,
	"id":12,
	"question":"Who invented Peanut Butter?"
	},
	{"answer":"Alexander Fleming",
	"category":1,
	"difficulty":3,
	"id":21,
	"question":"Who discovered penicillin?"
	}
	],"success":true,
	"total_questions":2
	}

POST /quizzes
General:
This endpoint returns a random question based on
a category and previous question parameters to ensure that questions
do not repeat and success value

sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d'{"quiz_category": { "id": "2", "type":"Art"}, "previous_questions":["18", "19"]}'

	{
	"question":
	{
	"answer":"Escher",
	"category":2,
	"difficulty":1,
	"id":16,
	"question”: “Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
	},
	"success":true}



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```