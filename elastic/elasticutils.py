
from elasticsearch.client import IndicesClient

STEM_INDEX = 'morphology'
ANALYZER_INDEX = 'analisis'
ANALYZER_NAME = 'clear'


def query_stem_index(tokens, es_client):
    result = []
    for token in tokens:
        search_res = es_client.search(index=STEM_INDEX,doc_type='word', body={
                    "query": {
                      "term": {
                        "word": {
                          "value": token
                        }
                      }
                    }
                })
        if search_res['hits']['total'] > 0:
            result.append(search_res['hits']['hits'][0]['_source']['wordbase'])
        else:
            result.append(token)

    return result


def analyze_text(text, es_client):
    analyze_client = IndicesClient(client=es_client)
    res = analyze_client.analyze(index=ANALYZER_INDEX, analyzer=ANALYZER_NAME, body=text)

    return [x['token'] for x in res['tokens']]
