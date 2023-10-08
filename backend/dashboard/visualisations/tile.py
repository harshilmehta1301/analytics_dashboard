class Tile:
    def __init__(self, **kwargs):
        self.query_set = kwargs['query_set']

    def generate(self):
        total_calls = self.query_set.count()
        unique_users = self.query_set.values_list('user').distinct().count()
        failed_calls = self.query_set.filter(status='failed').count()
        return [
            {'title': 'Total Calls', 'value': total_calls},
            {'title': 'Unique Users', 'value': unique_users},
            {'title': 'Failed Calls', 'value': failed_calls}
        ]
