'''This script will retrieve the current public ip address on a dynamic connection and 
then check the godaddy record for each domain listed in the domains variable. If the target
ip is different than the current public ip, the target ip will be changed to the current
public ip'''

from godaddypy import Client, Account
import urllib.request
import time

domains = ['calebhuck.me', 'atthetable.community']

#get the current public ip
ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#create godaddy object used for retrieving dns info and updating
account = Account(api_key='dLYcRuj5Jvon_C9Gz81S14bbA4k9SzAdVYU', api_secret='XUjWPZWz9wQeTkrEoxL1JV')
client = Client(account)

#infinite loop to check if the dynamic ip has changed, and if so then update dns records
while True:
    for domain in domains:
        record = client.get_records(domain, record_type='A', name='@')
        current_ip = record[0].get('data')
        if current_ip != ip:
            result = client.update_record_ip(ip, domain, '@', 'A')
            if result:
                print('Update successful!')
            else:
                print('error')
        else:
            print('nothing to update')
    time.sleep(5)




