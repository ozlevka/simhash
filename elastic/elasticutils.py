
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


def analyze_text(text, es_client, analyzer_index='analisis', analazer_name='clear'):
    analyze_client = IndicesClient(client=es_client)
    a_t = {
        'text': text
    }
    res = analyze_client.analyze(index=analyzer_index, analyzer=analazer_name, body=a_t)
    dedup_col = set()
    dedup_add = dedup_col.add
    return [x['token'] for x in res['tokens'] if not (x['token'] in dedup_col or dedup_add(x['token']))]


def get_word_frequency(es_client, word, index='*job*'):
    res = es_client.count(index=index, body={
          "query": {
            "term": {
              "_all": {
                "value": word
              }
            }
          }
        })

    return res['count']


def analyze_text_and_make_freq_pairs(es_client, text, analyzer_index='analisis', analazer_name='clear',
                                     search_index='*job*'):
    results = {}
    analazed = analyze_text(text, es_client, analyzer_index=analyzer_index, analazer_name=analazer_name)
    for word in analazed:
        f = get_word_frequency(es_client, word, index=search_index)
        if f == 0:
            results[word] = f
        else:
            results[word] = 1/f
    return results
