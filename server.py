import os
from flask import Flask
from elasticsearch import Elasticsearch
from elastic import ElasticOperations

app = Flask(__name__)
host = os.getenv('ELASTIC_HOST')
if host:
    client = Elasticsearch(hosts=[host])
else:
    client = Elasticsearch()

app.run(host='0.0.0.0', port=4050)