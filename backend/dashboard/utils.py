from copy import deepcopy

import pandas as pd
import psycopg2
from django.conf import settings


def get_data_from_db(query):
    print(query)
    db_cred = settings.SECRETS_ENV["DATABASE"]
    conn = psycopg2.connect(
        dbname=db_cred["NAME"],
        user=db_cred["USER"],
        password=db_cred["PASSWORD"],
        host=db_cred["HOST"],
        port=db_cred["PORT"],
        options='-c timezone=UTC'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    column_names = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    df = pd.DataFrame(results, columns=column_names)
    return df


def get_sql_query(period, filter_range):
    period_mapper = {
        'hours': 'HH24:MI',
        'days': 'DD-MM-YYYY'
    }
    select_query = f'''
            SELECT
            to_char("created", '{period_mapper[period]}') AS "Time",
            COUNT("user") AS "Calls",
            COUNT(DISTINCT "user") AS "Users",
            COUNT(CASE WHEN "status" = 'failed' THEN 1 END) AS "Failure"
    '''
    from_query = ' FROM analytics_log'
    group_by = ' GROUP BY "Time"'
    order_by = ' ORDER BY "Time" ASC'

    sub_select_query = 'SELECT "Time", SUM("Calls") AS "Calls", SUM("Users") AS "Users", SUM("Failure") AS "Failure"'
    filter_query = f'''
        where "created" >= '{filter_range[0]}' and  "created" <= '{filter_range[1]}'
    '''
    sub_from_query = f'from ({select_query} {from_query} {filter_query} {group_by}) AS "BASE"'

    query = f'''
        {sub_select_query} {sub_from_query} {group_by} {order_by};
    '''
    return query


def get_chart_df(period, filter_range):
    query = get_sql_query(period, filter_range)
    df = get_data_from_db(query)
    return df


def get_chart_object(df):
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


def get_chart(period, filter_range):
    df = get_chart_df(period, filter_range)
    chart = get_chart_object(df)
    return chart
