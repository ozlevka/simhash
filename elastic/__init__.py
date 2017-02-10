


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



