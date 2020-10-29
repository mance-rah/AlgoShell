# AlgoShell User Guide

AlgoShell is a coding challenge platform similar to LeetCode except it does not require internet access to validate solutions.

Please follow these steps to setup the coding challenge questions:
1. Download `AlgoShell`
2. Move file to `Desktop`
3. Unzip the file
3. Open a terminal window
4. Navigate to file with `cd Desktop/AlgoShell`
6. If using a Mac, run `chmod +x AlgoShell.sh`
7. Follow the instructions in `CodingQuestions.md` to do coding questions

---

### Start Frontend
1. Install Docker
2. Run `./start.sh`
3. Go to `localhost:3000` in the browser

To stop, run `./stop.sh`

---

## Start Backend
1. Run database migrations
```bash
docker-compose run web python manage.py migrate
```
2. Start the server
```bash
docker-compose up --build
```
3. Create an administrator account
```bash
docker-compose run web python manage.py create superuser
```

4. Go to `localhost:8000`
5. Sign in using the username and password you provided

---

Happy coding! 

Feel free to let me know if you have any questions `andrewroblesdev@gmail.com`
