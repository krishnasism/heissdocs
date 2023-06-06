# heißdocs - [heissdocs.com](https://heissdocs.com/)

A Document Search Engine 🔍📄

### Note:
> This is a project at its infancy, so please expect things to break as it moves forward.
But the vision of this project is to allow the user to NOT be locked into an ecosystem, so your data is governed and stored by you - therefore even if the app breaks, your data should be supported and can be accessed using tools already at your disposal.


# Pre-requisites
You need the following resources to be able to set up the app without any hassle.
1. AWS resources
    1. DynamoDB
    1. S3
1. Auth0

---
## Setting up
Start by creating a `.env` file in the root directory and fill in the values according to the `.env.example` file.

These can remain unchanged unless you are planning on hosting each of the services individually.
In that case, please follow the documentation [here](#).


Similarly, create a `.env` file inside the `backend` and `frontend` folders and fill them in following the instructions in the respective `.env.example` files. 

> Promise I'll make this easier!

---

## Running
Ensure that the credentials that you pasted in the `.env` files have the necessary authorizations for operations such as `GET`, `PUT`, `LIST` ... etc.

Once your `.env` files are ready, navigate to the root directory and run:
> docker compose up --build

Then go to `localhost:8080` and log in.

## Settings
Before using the application, navigate to the `Settings` page by clicking on the left-side dashboard button, and configure the settings.

## Ready!
You are all set!

---
# About the Project:

## Vision: 
- Pluggable into various cloud providers
- Bring your own Compute, Storage, & Search providers
- Govern your own data
- Easily deployable to everywhere

---
In progress for the community - by [Krishnasis](https://www.linkedin.com/in/krishnasis/) 👨🏽‍💻

Powered by [FastAPI](https://fastapi.tiangolo.com/) 💗
