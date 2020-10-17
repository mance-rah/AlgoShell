# AlgoShell

AlgoShell is a coding challenge platform similar to LeetCode except it utilizes a terminal interface to submit coding solutions from a file on your computer instead of in the browser. The tech stack is Python Django Web Framework and JavaScript React Web Framework. 

**Please install Docker before going through the intructions to setup the project.**

### Project Setup
With docker installed do the following:
1. Run `./run.sh` to create and run docker containers
2. Run `./stop.sh` to stop and remove docker containers

### Admin Interface
1. Go to `localhost:8000/admin` for the login page
2. Username is `admin` and password is `1234`

### Frontend Interface
React app is visible at `localhost:3000`

### Backend Interface
Backend URLs are visible at `localhost:8000`

### Integration Tests
Run `./test.sh`

### API Endpoints
All the endpoints are implemented in `questions/views.py` and url definitions are implemented in `questions/urls.py`. Here is a list of the ones that are currently implemented.

1. POST request to `questions/<str:function_name>` to run tests on submitted coding solution in request body `{"solution": <str: python_function_definition>}`.
2. GET request to `questions` returns a list of all the questions that are supported and their information.

To see these endpoints in action either run the tests or use postman while referencing the API calls in `tests.py`

Feel free to reach out to me if you have any questions! `andrewroblesdev@gmail.com`
