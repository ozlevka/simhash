
from elasticsearch.client import IndicesClient


def query_stem_index(tokens, es_client, stem_index='morphology'):
    result = []
    for token in tokens:
        search_res = es_client.search(index=stem_index,doc_type='word', body={
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


def analyze_text(text, es_client, analyzer_index='analisis', analazer_name='clean'):
    analyze_client = IndicesClient(client=es_client)
    res = analyze_client.analyze(index=analyzer_index, analyzer=analazer_name, body=text)

    return [x['token'] for x in res['tokens']]
