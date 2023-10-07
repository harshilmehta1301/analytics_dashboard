from analytics.models import Log


def log_request(user, data, source):
    status = data.get('status', 'success')
    response = {'message': 'Success response.'} if status == 'success' else {'message': 'Error while processing data.'}
    kwargs = {
        'user': user,
        'status': status,
        'request': data,
        'response': response,
        'app': source
    }
    Log.objects.create(**kwargs)
    response_code = 200 if status == 'success' else 500
    return response, response_code
