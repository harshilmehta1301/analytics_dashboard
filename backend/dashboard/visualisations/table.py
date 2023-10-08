from analytics.serializer import LogSerializer


class Table:
    def __init__(self, **kwargs):
        self.query_set = kwargs['query_set']

    def generate(self):
        data = LogSerializer(self.query_set, many=True).data
        columns = ['ID', 'User ID', 'Timestamp', 'Status', 'Error Message', 'Request', 'Response']
        keys = []
        if data:
            keys = data[0].keys()
        return {'columns': columns, 'keys': keys, 'data': data}
