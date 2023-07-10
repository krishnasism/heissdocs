# heißdocs - [heissdocs.com](https://heissdocs.com/)

# ## UNDER ACTIVE DEVELOPMENT ## ##

A Document Search Engine 🔍📄

Add a searchable layer on top of your PDFs!

Fully open-source and ready to be deployed.
You store, own, and control the data. 100% private!
![image](https://github.com/krishnasism/heissdocs/assets/21293324/84d4fd21-f480-4e65-a43d-4addad1b34a9)

### Note:
> This is a project at its infancy, so please expect things to break as it moves forward.
But the vision of this project is to allow the user to NOT be locked into an ecosystem, so your data is governed and stored by you - therefore even if the app breaks, your data should be supported and can be accessed using tools already at your disposal.

# Usage
## What is the purpose of this project?

Well it is to allow an user or an organization to keep track of their PDF files. The complicated thing about PDFs are that they aren't searchable by content.

**heißdocs** aims to solve this problem by creating a search layer for your PDFs, down to the exact page (Working on pointing to the exact word!),

1. Set up according to the instructions under `Setup`
1. Upload a file on the Dashboard
1. Start searching!

Keep an eye on the `Vision` tab to take a look at what is in stock for the future!

---
# Setup
## Pre-requisites
You need the following resources to be able to set up the app without any hassle.
1. AWS resources
    1. DynamoDB
    1. S3
1. Auth0:
1. Elasticsearch (+ local elasticsearch support available)

For Auth0 you will need to get the following values from the [Auth0 portal](https://manage.auth0.com/) and paste them accordingly in the `.env` file.

    ```
    AUTH0_DOMAIN=
    AUTH0_API_AUDIENCE=http://localhost:8000
    AUTH0_ALGORITHMS=RS256
    AUTH0_ISSUER=
    AUTH0_CLIENT_ID=
    AUTH0_CLIENT_SECRET=
    ```

---
## Setting up
Start by creating a `.env` file in the root directory and fill in the values according to the `.env.example` file.

These can remain unchanged unless you are planning on hosting each of the services individually.
In that case, please follow the documentation [here](#).


Similarly, create a `.env` file inside the `backend`, `frontend` and `engine` folders and fill them in following the instructions in the respective `.env.example` files. 

Most of the values except private keys can be left as is!

> Promise I'll make this easier!

---

## Running
Ensure that the credentials that you pasted in the `.env` files have the necessary authorizations for operations such as `GET`, `PUT`, `LIST` ... etc.

Once your `.env` files are ready, navigate to the root directory and run:
> docker compose up --build

Then go to `localhost:8080` and log in.

---
[Optional]
*In case you want hot-reload on your `frontend`, you can choose to run the services separately*

Run the `backend` services:
> docker compose -f .\docker-compose.yaml up --build

Run the `frontend`:
```
cd frontend
npm run dev -- --port 8080
```

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
- Add ChatGPT support (preferably something like [privateGPT](https://github.com/imartinez/privateGPT))

---
In progress for the community - by [Krishnasis](https://www.linkedin.com/in/krishnasis/) 👨🏽‍💻

Powered by [FastAPI](https://fastapi.tiangolo.com/) 💗
