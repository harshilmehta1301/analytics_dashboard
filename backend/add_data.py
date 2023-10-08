import random

import requests


def main():
    for i in range(0, 200):
        data = {
            'status': random.choice(['success']),
            'user_id': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        }
        response = requests.post('http://127.0.0.1:8000/api/v1/', data)
        print(i, '------------->', response.status_code)


if __name__ == '__main__':
    main()
