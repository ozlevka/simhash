
from elastic.elasticutils import *

class ElasticOperations():
    '''
    Class used for run operations with elasticsearch cluster
    '''
    def __init__(self, client):
        '''
        As constructor parameter class receive initialized elasticsearch client
        :param client: Elasticsearch client for make operations with cluster
        '''
        self.client = client

    def stem_hebrew_tokens(self, tokens):
        '''
        Send all hebrew word to special index for convert to base word
        :param tokens: List of hebrew words
        :return: List of hebrew base words
        '''
        tokens_list = []
        if isinstance(tokens, list):
            tokens_list = tokens
        else:
            tokens_list.append(tokens)

        return query_stem_index(tokens, self.client)

    def tokenize_text(self, text):
        '''
        Send text to special elastic index for tokenize
        :param text: Unicode text
        :return: List of tokens
        '''
        return analyze_text(text, self.client)

    def setup_analytics_indexes(self, es_client):
        pass
