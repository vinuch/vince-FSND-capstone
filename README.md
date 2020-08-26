# Casting Agency Full Stack

## Full Stack Nano -  Capstone Project


BACKSTORY: Sony Studios a small movie casting agency has decided to take the management of their agency including their actors and movies produced online to make things easier for them in the long run, but it has to restrict who can do what on their platform. this is a solution to help cover their needs.

The application :

1) Displays cards an image an some metadata of actors and movies in their respective routes 
2) On sign up assign users the role of casting assistant
2) Allow Casting Assitants to view actors and movies.
3) Allow the Casting Directors add, and delete actors from the database and edit both actors and movies
4) Allow the Executive Producer to add and delete movies from the database


## About the Stack


### Backend

The `./backend` directory contains a Flask server that uses SQLAlchemy to interact with a postgress database, and integrates Auth0 for authentication and Role Based Access Control RBAC for protected endpoints.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Vuejs frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/.env) to reflect the Auth0 configuration details set up for the backend app. 

[View the README.md within ./frontend for more details.](./frontend/README.md)
