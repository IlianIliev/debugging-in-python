# Debugging in Python


## Contents

This repo contains two main pieces:
 - A single broken python script in the `demo` folder for demonstration purposes. 
 - A broken Django application that needs to be fixed as part of the exercise.

The project is tested with Python 3.11.4

The presentation from the workshop is available [https://bit.ly/debugging-in-python](https://bit.ly/debugging-in-python)


## How to start:
- Create a virtual environment with `python3 -m venv venv`
- Install the requirements with `pip install -r requirements.txt`
- Run the migrations with `python manage.py migrate`
- Run the server with `python manage.py runserver`
- Open http://127.0.0.1:8000/ in the browser and follow the instructions


### Guidelines
 - There are multiple issues with the project. Some can be solved just by good observation, for other you will have to do a proper debugging
 - All broken code is inside this repo, do not debug beyond the scope of this project
 - Knowing Django helps, but you should be able to solve the projects without any Django knowledge just by looking at the code
 - A branch with solutions and hints is available under the name `solutions`, but try to solve the project without it first
 - Play, experiment, and have fun!

### Warnings:

- The project code is for educational/debugging purposes only.
- Most of the technical decisions made in the project are not optimal and should not be used in production.

