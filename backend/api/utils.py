from analytics.models import Log


def log_request(data, source):
    status = data.get('status', 'success')
    response = {'message': 'Hello World.'} if status == 'success' else {'message': 'Bye World.'}
    kwargs = {
        'user': data['user_id'],
        'status': status,
        'request': data,
        'response': response,
        'app': source
    }
    Log.objects.create(**kwargs)
    response_code = 200 if status == 'success' else 500
    return response, response_code
