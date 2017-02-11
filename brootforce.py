# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import helpers as eh
from elastic import ElasticOperations
from simhash import Simhash
import json

client = Elasticsearch()

ops = ElasticOperations(client)


all_docs = eh.scan(client, index='*job*')

bulk = []
for doc in all_docs:
    if isinstance(doc['_source']['body'], list):
        text = (' '.join(doc['_source']['body']))
    else:
        text = doc['_source']['body']

    try:
        analyzed = ops.analyze_with_idf(text)
        val = str(Simhash(analyzed).value)
        index_item = {
            '_index': 'comparasion',
            '_type': 'fingerprint',
            '_source': {
                'document': doc['_id'],
                'index': doc['_index'],
                'fingerprint': val,
                'fingerprint_arr': list(val)
            }
        }

        bulk.append(index_item)
        if len(bulk) > 100:
            print(eh.bulk(client, bulk))
            bulk = []
    except Exception as e:
        print(e)
        with open('/home/ozlevka/bigdisk/data/wrong/' + doc['_id'].replace('/', '__') + '.json', mode='w', encoding='UTF-8') as file:
            json.dump(doc,file,ensure_ascii=False)


if len(bulk) > 0:
    print(eh.bulk(client, bulk))
