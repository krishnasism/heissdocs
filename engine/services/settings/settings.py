import logging


class Settings:
    _instance = None
    aws_access_key = ""
    aws_secret = ""
    aws_region = ""
    no_sql_provider = ""
    document_table_name = ""
    parsing_api_key = ""
    buckets_list = ""
    document_table_name = ""
    scan_bucket = ""
    elastic_search_index = ""
    elastic_search_host = ""
    elastic_search_port = ""
    elastic_search_api_key = ""
    search_document_db = False
    search_elastic_search = False
    store_logs_in_db = False
    mongo_db_database = ""
    mongo_db_username = ""
    mongo_db_password = ""
    mongo_db_host = ""
    openai_api_key = ""
    hugging_face_api_key = ""
    qdrant_api_key = ""
    qdrant_host = ""
    qdrant_port = ""
    qdrant_collection_name = ""

    def __init__(self):
        if Settings._instance is not None:
            raise Exception("Settings class is a singleton!")
        else:
            Settings._instance = self

    def update_settings(self, settings: dict):
        if len(settings) == 0:
            logging.error("[Queue - Settings] Settings not yet set, passing...")
            return None
        # TODO : Remove dup settings
        self.aws_access_key = settings.get("awsAccessKey")
        self.aws_secret = settings.get("awsSecret")
        self.aws_region = settings.get("awsRegion")
        self.no_sql_provider = settings.get("noSqlProvider")
        self.document_table_name = settings.get("documentTableName")
        self.parsing_api_key = settings.get("parsingApiKey")
        self.buckets_list = settings.get("bucketsList")
        self.scan_bucket = settings.get("scanBucket")
        self.elastic_search_index = settings.get("elasticSearchIndex")
        self.elastic_search_host = settings.get("elasticSearchHost")
        self.elastic_search_port = settings.get("elasticSearchPort")
        self.elastic_search_api_key = settings.get("elasticSearchApiKey")
        self.search_elastic_search = settings.get("searchElasticSearch")
        self.search_document_db = settings.get("searchDocumentDb")
        self.store_logs_in_db = settings.get("storeLogsInDb")
        self.mongo_db_database = settings.get("mongoDbDatabase")
        self.mongo_db_username = settings.get("mongoDbUsername")
        self.mongo_db_password = settings.get("mongoDbPassword")
        self.mongo_db_host = settings.get("mongoDbHost")
        self.openai_api_key = settings.get("openaiApiKey")
        self.hugging_face_api_key = settings.get("huggingFaceApiKey")
        self.qdrant_api_key = settings.get("qdrantApiKey")
        self.qdrant_host = settings.get("qdrantHost")
        self.qdrant_port = settings.get("qdrantPort")
        self.qdrant_collection_name = settings.get("qdrantCollectionName")
        self.cloud_provider = settings.get("cloudProvider")
        self.azure_blob_connection_string = settings.get("azureBlobConnectionString")
        self.cosmos_db_host = settings.get("cosmosDbHost")
        self.cosmos_db_container = settings.get("cosmosDbContainer")
        self.cosmos_db_container = settings.get("cosmosDbDatabase")
        self.cosmos_db_key = settings.get("cosmosDbKey")
        self.cosmos_db_database = settings.get("cosmosDbDatabase")
        self.gcp_key_file_content = settings.get("gcpKeyFileContent")
        self.open_ai_type = settings.get("openAiType")
        self.open_ai_base = settings.get("openAiBase")
        self.open_ai_deployment_name = settings.get("openAiDeploymentName")
        self.open_ai_api_version = settings.get("openAiApiVersion")
        self.open_ai_model_name = settings.get("openAiModelName")

    @classmethod
    def get_settings(cls):
        if cls._instance is None:
            cls._instance = Settings()
        return cls._instance
