# heißdocs - [heissdocs.com](https://heissdocs.com/)

A document search engine 🔍📄

### Note:
> This is a project at its infancy, so please expect things to break as we move forward.
But the vision of this project is to allow the user to not be locked into an ecosystem, so your data is governed and stored by you - therefore even if the app breaks, your data should be supported and can be accessed using tools already at your disposal.

This project only brings everything into once place, that you can use to make your life easier!

# Pre-requisites
You need the following resources to be able to set up the app without any hassle.
1. AWS resources
    1. dynamodb
    1. s3
1. Auth0

---
## Setting up
Firstly you will create a `.env` file in the root directory and fill up the values according to the `.env.example` file.

These don't need to be changed as long as you are not hosting each of the services yourself. In that case, please follow the docs [here](#).


Similarly, create a `.env` file inside the `backend` and `frontend` folders and fill them according to the instructions in the respective `.env.example` files. 

> Promise I'll make this easier as time goes by!

---

## Running
Please make sure that the credentials that you pasted in the `.env` files have the necessary authorizations to perform operations such as `GET`, `PUT`, `LIST` ... etc.

Once your `.env` files are ready. In the root directory:
> docker compose up --build

Then navigate to `localhost:8080` and log in.

## Settings
Before using the applications, navigate to the `Settings` page by clicking on the left side dashboard button, and fill in the settings.

## Ready!
After your settings are set, you can start using the application!

--
# About the Project

### Vision: 
- Pluggable into various cloud providers
- Bring your own Compute, Storage, & Search providers
- Govern your own data
- Easily deployable to everywhere

## [Work In Progress]

---
## To-Dos for Search
- [ ] Full Text Search (Full Text storage and search)
- [ ] NLP Extractive Summarization Search (Important Text storage and search)
- [ ] Keyword Based Search (Only key words in document search)


## To-Dos for Cloud
- [ ] Add Connectors for major cloud providers (AWS, GCP, Az)
- [ ] Add Connectors for NoSQL DBs
- [ ] Add Connectors for Search Engines (OpenSearch, ElasticSearch)
- [ ] Add generic connectors


---
In progress for the community - by [Krishnasis](https://www.linkedin.com/in/krishnasis/) 👨🏽‍💻

Powered by [FastAPI](https://fastapi.tiangolo.com/) 💗
