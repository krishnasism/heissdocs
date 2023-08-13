**heißdocs** - A Document Query Application 🔍📄
## # Under Active Development # ##

Add a searchable layer on top of your PDFs!

Fully open-source and ready to be deployed.
You store, own, and control the data.

![Recording-2023-08-12-202607](https://github.com/krishnasism/heissdocs/assets/21293324/c39b3e5e-e152-4234-aaea-79d0e35c6e1a)

### Note:
> This is a project in its infancy, so please expect things to break as it moves forward.
But the vision of this project is to allow the user to NOT be locked into an ecosystem, so your data is governed and stored by you - therefore even if the app breaks, your data should be supported and can be accessed using tools already at your disposal.

# Usage
## What is the purpose of this project?

It is to allow a user or an organization to keep track of their PDF files. The complicated thing about PDFs is that they aren't searchable by content.
Simply upload a scanned or normal PDF and start searching for content in it with the undisputed power of Elasticsearch (or a Nosql database)!

**heißdocs** creates search layer for your PDFs, down to the exact page (Working on pointing to the exact word!),

1. Set up according to the instructions under `Setup`
1. Upload a file on the Dashboard
1. Start searching!

Keep an eye on the `Vision` tab to take a look at what is in stock for the future!

---
# Setup
## Pre-requisites
You need the following resources to be able to set up the app without any hassle.
You can follow this [document](https://github.com/krishnasism/heissdocs/blob/main/docs/doc.md) to fetch the required values.
1. Auth0:
    1. For Auth0 you will need to get the required values from the [Auth0 portal](https://manage.auth0.com/) and paste them accordingly in the `.env` files in `frontend` and `app`. This needs to be configured even before building the application.
1. AWS resources
    1. DynamoDB
    1. S3
1. Elasticsearch
1. MongoDB

For LLM Support. Both of the following services need to be configured together:
1. **Qdrant**: A vector database required for semantic searching. [Qdrant](https://qdrant.tech/)
2. **OpenAI API**: Needed to generate embeddings for the search functionality. [OpenAI API](https://openai.com/blog/openai-api)

## Setting up
Start by creating a `.env` file in the root directory and fill in the values according to the `.env.example` file.

```bash
cp .env.example .env
```

The values in the root `.env` file can remain unchanged unless you are planning on hosting each of the services individually.


Similarly, create an `.env` file inside the `app`, `frontend`, and `engine` folders and fill them in following the instructions in the respective `.env.example` files. 

```bash
cp frontend/.env.example frontend/.env
cp app/.env.example app/.env
cp engine/.env.example engine/.env
```

Most of the values except private keys can be left as is!
Follow my comments in the files!
> Promise I'll make this easier!

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
# About the Project:

## Vision: 
- Pluggable into various cloud providers
- Bring your own Compute, Storage, & Search providers
- Govern your own data
- Easily deployable to everywhere
- Add private LLM support

---
In progress for the community - by [Krishnasis](https://www.linkedin.com/in/krishnasis/) 👨🏽‍💻

Powered by [FastAPI](https://fastapi.tiangolo.com/) 💗
