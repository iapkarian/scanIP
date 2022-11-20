import requests


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'https://ipinfo.io/{ip}').json()
        print(response)
        data = {
            '[IP]': response.get('ip'),
            '[City]': response.get('city'),
            '[Name]': response.get('org')
        }
        print(data)
    except requests.exceptions.ConnectionError:
        print('Please, check our connection!')


def main():
    # ip = input('Please enter a target IP: ')
    get_info_by_ip(ip='213.110.149.65')


if __name__ == '__main__':
    main()
