# Configurations

Note: This is an AI generated document, so just be mindful. I will update it!

## Auth0 Configuration

heißdocs uses Auth0 for authentication (will update in the future). 
There are several configuration values you'll often need to set up the applications. Here's a step-by-step guide to retrieve them:

### Prerequisites

- You should have an Auth0 account.
- You must have an application already set up on Auth0. If not, you'll need to create one.

### Steps

1. **Login to Auth0**
   
   Navigate to the [Auth0 login page](https://auth0.com/login) and sign in to your account.

2. **Access the Dashboard**

   Once logged in, you'll land on your Auth0 Dashboard.

3. **Navigate to Applications**

   On the left sidebar of your Dashboard, click on the `Applications` menu.

4. **Select your Application**

   In the `Applications` section, you will see a list of all your Auth0 applications. Click on the name of the application for which you want to retrieve the necessary values.

5. **Retrieve the Values**

   - `AUTH0_DOMAIN`: Found in the `Domain` field.
   - `AUTH0_CLIENT_ID`: Located in the `Client ID` field.
   - `AUTH0_CLIENT_SECRET`: Found in the `Client Secret` field. Treat this value as sensitive; never expose it in client-side code or public repositories.

6. **Setting Up Configurations**

   Replace the placeholders with the values you've just retrieved:

   ```plaintext
   # Authentication specific - Only update these from https://manage.auth0.com/
   AUTH0_DOMAIN="Your Auth0 Domain"
   AUTH0_ISSUER="Your Auth0 Domain"
   AUTH0_CLIENT_ID="Your Auth0 Client ID"
   AUTH0_CLIENT_SECRET="Your Auth0 Client Secret"
   AUTH0_API_AUDIENCE=http://localhost:8000
   AUTH0_ALGORITHMS=RS256
   ```

## Postgres Settings
The POSTGRES_* settings can be left alone and don't need to be changed if you are not hosting the SQL database yourself.

In that case please update the values accordingly.

```plaintext
POSTGRES_USERNAME="user"
POSTGRES_PASSWORD="password"
POSTGRES_ENDPOINT="db:5432/heissdocs"
STORE_LOGS_IN_DB="true"
```
---

### For the next values, you don't need to modify the `.env` file. You can directly change these values in the Settings page of the Dashboard.
![image](https://github.com/krishnasism/heissdocs/assets/21293324/3c818fdc-21cd-42f7-974d-f651412eb9a8)

## AWS Configuration Retrieval

When configuring the application with AWS services, several values need to be set, especially when integrating services like DynamoDB.

### AWS Access Key & Secret

The AWS Access Key and Secret are credentials that grant the application access to AWS services.

1. **Navigate to AWS Management Console**

   Sign in to your AWS account at [AWS Management Console](https://aws.amazon.com/console/).

2. **Access IAM (Identity and Access Management)**

   Find and click on the `IAM` service, typically under `Security, Identity, & Compliance`.

3. **Go to Users**

   On the left sidebar, click on `Users`.

4. **Select the desired user or create one**

   If you've already created a user for your application, click on their name. If not, you may need to create a new user and grant them the necessary permissions.

5. **Retrieve `AWS_ACCESS_KEY` and `AWS_SECRET`**

   In the `Security credentials` tab, you can find the `Access Key ID` (your `AWS_ACCESS_KEY`) and the `Secret access key` (your `AWS_SECRET`). If you haven't created an access key for the user yet, you can do so here.

### AWS Region

Your `AWS_REGION` is the geographical area where your AWS resources are hosted. AWS has multiple regions, and you typically select the one closest to your user base or with specific services you need.

- You can find the list of AWS regions and their codes in the [official AWS documentation](https://docs.aws.amazon.com/general/latest/gr/rande.html).

### AWS Search Table Name (DynamoDB)

If you're using DynamoDB to store parsed PDFs, you should know the table's name:

1. **Go to DynamoDB**

   From the AWS Management Console, navigate to the `DynamoDB` service.

2. **Locate your Table**

   In the `Tables` section, find the table storing the parsed PDFs. This table's name is your `AWS_SEARCH_TABLE_NAME`.

### Setting Up Configurations

You can then set these values directly in your application frontend.:


## MongoDB Configuration Retrieval

For applications utilizing MongoDB as their database, there are several essential configurations that you may need to set in your backend or application configuration layer.

### MongoDB Database and Collection Name

The database name (`MONGODB_DB_NAME`) and collection name (`MONGODB_COLLECTION_NAME`) are foundational elements of how data is organized in MongoDB.

1. **Access MongoDB Atlas or Your Local MongoDB Instance**

   - If you're using MongoDB Atlas, navigate to [MongoDB Atlas login page](https://account.mongodb.com/account/login) and sign in.
   - If you're running MongoDB locally, access your MongoDB management tool or CLI.

2. **Navigate to Clusters (For MongoDB Atlas)**

   Click on `Clusters` on the left sidebar.

3. **Access your Database**

   - For Atlas, click on the `Collections` button for your cluster.
   - For local, navigate to your database using your tool or CLI.

4. **Retrieve Database and Collection Names**

   You should now see a list of your databases and their collections. Identify your desired database and collection, and note down their names for `MONGODB_DB_NAME` and `MONGODB_COLLECTION_NAME` respectively.

### MongoDB Connection Details


1. **Find Connection String (For MongoDB Atlas)**

   - Go back to `Clusters` and click on the `CONNECT` button for your cluster.
   - Choose `Connect your application`.
   - Here, you'll see the connection string. It will look something like this:
     ```
     mongodb+srv://user:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
     ```
   - The endpoint after `@` and before `/` is your `MONGO_DB_HOST`.
   - `user` is your `MONGO_DB_USERNAME`.
   - Replace `<password>` with your actual password for `MONGO_DB_PASSWORD`.

2. **For Local MongoDB Instances**

   If you've set up MongoDB locally, your connection details might be simpler, and you might not have set a username or password. If you have, remember where you stored them or refer to your MongoDB configuration files.

### Setting Up Configurations

Once you've gathered all the necessary information, you can set these values from the application's frontend.

---

The `Infra specific` and `MiniIO` values don't need to be changed.
The application is not set up to be distributed yet. This will follow in a later version.

---

## Elasticsearch Configuration Retrieval

When integrating Elasticsearch into your application, certain configuration values are essential to ensure smooth communication and proper data indexing. Below is a guide to help you identify and set these configurations.

### Elasticsearch Index Name

The index name is a unique identifier that Elasticsearch uses to store and retrieve documents. This is similar to a database name in traditional databases.

1. **Access Kibana or Elasticsearch Instance**

   - If you're using the Kibana interface (often used with Elasticsearch for visualization and management), log in to your Kibana dashboard.
   - If you're directly accessing Elasticsearch, navigate to your Elasticsearch instance using a browser or API tool.

2. **Locate the Index**

   In Kibana:
   - Go to the `Management` section.
   - Under `Index Management`, you will see a list of all indices.
   - Find your desired index and note its name for `ELASTIC_SEARCH_INDEX`.

### Elasticsearch Host and Port

The host and port are essential for connecting to your Elasticsearch instance.

1. **Access Elasticsearch**

   - Navigate to your Elasticsearch instance, whether it's hosted on a service like Elastic Cloud, on a virtual machine, or locally.
   
2. **Retrieve Host and Port Details**

   - The host (`ELASTIC_SEARCH_HOST`) would typically be the domain name or IP address of your Elasticsearch server. If you're running it locally, it might simply be `localhost`.
   - The default port for Elasticsearch (`ELASTIC_SEARCH_PORT`) is `9200`, but this can change based on your configuration. Ensure you have the correct port.

### Elasticsearch API Key

API Keys in Elasticsearch are used for request authentication.

1. **Access Kibana**

   Log in to your Kibana dashboard.

2. **Generate or Retrieve API Key**

   - Go to `Stack Management`.
   - Under `Security`, click on `API keys`.
   - Here, you can create a new API key or view existing ones (if you have the necessary permissions). Note the API key for `ELASTIC_SEARCH_API_KEY`.

### Setting Up Configurations

Once you've gathered all the necessary information, you can set these values in the frontend.

## Configuration Retrieval for OpenAI and QDrantCloud

This guide will provide you with the steps to obtain the required configuration details for integrating with OpenAI and QDrantCloud services.

### OpenAI API Key

OpenAI provides an API key to authenticate and access their services.

1. **Access OpenAI Portal**

   - Navigate to the [OpenAI Dashboard](https://platform.openai.com/).
   - Sign in to your OpenAI account.

2. **Locate Your API Key**

   - Once logged in, go to the `API Keys` section.
   - Here, you will find your active API keys. If you haven't generated one yet, you can create a new API key.
   - Note the API key for `OPENAI_API_KEY`.

### QDrantCloud Configuration

QDrantCloud requires an API key for authentication and other configuration details to interface with their service.

1. **Access QDrantCloud Dashboard (if using the cloud version)**

   - Navigate to the QDrantCloud login or dashboard page.
   - Sign in to your QDrantCloud account.

2. **Retrieve Your API Key**

   - In the dashboard, go to the API or credentials section (the exact navigation might vary based on the UI updates).
   - Here, you'll find the `QDRANT_API_KEY`. If you're using a local instance of QDrant, you might not need an API key, and you can leave it blank.

3. **Other Configurations**

   - `QDRANT_HOST`: This would typically be the domain name or IP address of your QDrant server. For local instances, it's usually `http://localhost`.
   - `QDRANT_PORT`: Default port might be `6333`, but ensure it's the correct one based on your setup.
   - `QDRANT_COLLECTION_NAME`: If you've already set up a collection in QDrant, note its name. In this case, it's given as `heissdocs`.

### Setting Up Configurations

After obtaining the necessary details, you can set these values in the frontend.

