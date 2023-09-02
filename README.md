**heißdocs** - A Document Query Application 🔍📄

[Official Documentation](https://docs.heissdocs.com/)
## # Under Active Development # ##

Add a searchable layer on top of your PDFs!

Fully open-source and ready to be deployed.
You store, own, and control the data.

<a href="https://www.producthunt.com/posts/heissdocs?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-heissdocs" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=411357&theme=light" alt="hei&#0223;docs - Open&#0032;Source&#0032;&#0038;&#0032;Self&#0032;Hosted&#0032;Document&#0032;Query&#0032;Engine | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

Demo:
![Recording-2023-08-26-211554](https://github.com/krishnasism/heissdocs/assets/21293324/680286c6-2c0d-4230-8397-571b4085fd69)

### Note:
> This is a project in progress, so please expect things to break as it moves forward.
But the vision of this project is to allow the user to NOT be locked into an ecosystem, so your data is governed and stored by you - therefore even if the app breaks, your data should be supported and can be accessed using tools already at your disposal.

# Usage
## What is the purpose of this project?

It is to allow a user or an organization to keep track of their PDF files. The complicated thing about PDFs is that they aren't searchable by content.
Simply upload a scanned or normal PDF and start searching for content in it with the undisputed power of Elasticsearch (or a NoSQL database)!

**heißdocs** creates a search layer for your PDFs, down to the exact page (Working on pointing to the exact word!),

1. Set up according to the instructions under `Setup`
1. Upload a file on the Dashboard
1. Start searching!

# Features
- ☁️ Multi-cloud support (AWS, GCP, Azure)
- 💬 Semantic search (Langchain + OpenAI)
- 💿 Multiple Storage Options
- 🔍 Powerful Search + Versatile Storage
- 📄 View source documents
- 🔒 Full ownership of data
- 🆓 Completely open-source
- 💻 Self-hosted
- ... more things to come + feel free to add in requests!


---
# Setup
## Pre-requisites
Please set up the required services before starting the application.
You can follow [the documentation](https://docs.heissdocs.com/) to configure all services.
1. Auth0 - required even before startup:
    1. For Auth0 you will need to get the required values from the [Auth0 portal](https://manage.auth0.com/) and paste them accordingly in the `.env` files in `frontend` and `app`. This needs to be configured even before building the application.

## Setting up
Start by creating a `.env` file in the root directory and fill in the values according to the `.env.example` file.

Before startup, only the Auth0 values need to be set up.
Please follow the [documentation](https://docs.heissdocs.com/) for the full guide.

```bash
cp .env.example .env
```

The values in the root `.env` file can remain unchanged unless you are planning on hosting each of the services individually.


Similarly, create a `.env` file inside the `app`, `frontend`, and `engine` folders and fill them in following the instructions in the respective `.env.example` files. 

```bash
cp frontend/.env.example frontend/.env
cp app/.env.example app/.env
cp engine/.env.example engine/.env
```

All the keys except Auth0 keys, can be left untouched. 
Everything else is settable in settings.

---

## Running
Ensure that the credentials that you pasted in the `.env` files have the necessary authorizations for operations such as `GET`, `PUT`, `LIST` ... etc.

Once your `.env` files are ready, navigate to the root directory and run:
```bash
docker compose up --build
```

Then go to `localhost:8080` and log in.

---
[Optional]
*In case you want hot-reload on your `frontend`, you can choose to run the services separately*

Run the `backend` services:
```bash
docker compose -f docker-compose.yaml up --build
```

If you want elasticsearch locally running as well, you can include the `docker-compose.elasticsearch.override.yaml` file as well in the `docker compose` command.

```bash
docker compose -f docker-compose.yaml -f docker-compose.elasticsearch.override.yaml up --build
```

Run the `frontend`:
```bash
cd frontend
npm install
npm run dev -- --port 8080
```

## Settings
Before using the application, navigate to the `Settings` page by clicking on the left-side dashboard button, and configure the settings.

## Ready!
You are all set!

## Overview
Here's a quick overview of the project

Ingestion Flow
![Technical Diagrams - Frame 1](https://github.com/krishnasism/heissdocs/assets/21293324/2b34c722-8766-45f3-a5ef-0da343631aa1)

Query Flow
![Technical Diagrams - Frame 2](https://github.com/krishnasism/heissdocs/assets/21293324/8a8a8f57-62b3-4e55-9e65-f1cb6882d464)


---
In progress for the community - by [Krishnasis](https://www.linkedin.com/in/krishnasis/) 👨🏽‍💻

Powered by [FastAPI](https://fastapi.tiangolo.com/) 💗
