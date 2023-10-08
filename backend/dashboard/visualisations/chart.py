from copy import deepcopy

from dashboard.utils import get_data_from_db, get_sql_query


class Chart:
    def __init__(self, **kwargs):
        self.period = kwargs['period']
        self.filter_range = kwargs['filter_range']

    def get_data(self):
        query = get_sql_query(period=self.period, filter_range=self.filter_range)
        df = get_data_from_db(query)
        return df

    def get_chart_object(self, df):
        base_object = {
            'yAxis': {
                'type': 'value'
            },
            'xAxis': {
                'type': 'category',
                'data': []
            },
            'tooltip': {
                'trigger': 'axis'
            },
            'series': [],
            'legend': {
                'data': [],
                'top': 'bottom'
            },
            # 'color': ["#4E79A7", "#F28E2B", "#E15759", "#86BCB6", "#59A14F"]
            'color': ["#4E79A7", "#59A14F", "#E15759"]
        }
        periods = df['Time'].tolist()
        base_object['xAxis']['data'] = periods
        categories = ['Calls', 'Users', 'Failure']
        base_object['legend']['data'] = categories
        series = []
        for category in categories:
            print(category)
            print(deepcopy(df[category].tolist()))
            series.append(
                {
                    'type': 'line',
                    'name': category,
                    'stack': 'Total',
                    'data': df[category].tolist()
                }
            )
        base_object['series'] = series
        return base_object

    def generate(self):
        df = self.get_data()
        chart = self.get_chart_object(df)
        return chart
