import CloudFlare
import urllib.request
import time

if __name__ == '__main__':

    api_key = None
    
    with open('key.key', 'rt') as file:
        api_key = file.read()

    with open('email.key', 'rt') as file:
        email = file.read()
    
    cf = CloudFlare.CloudFlare(email=email, token=api_key)
    zones = cf.zones.get()

    while(True):
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        for zone in zones:
            id = zone['id']
            dns_records = cf.zones.dns_records.get(id)
            for record in dns_records:
                if record['type'] == 'A':
                    if record['content'] != ip:
                        print('Need to update')
                        record['content'] = ip
                        r = cf.zones.dns_records.delete(id, record['id'])
                        r = cf.zones.dns_records.post(id, data=record)
                        print('Updated dns ip to {}'.format(ip))
                    else:
                        print('Nothing to update...')
        time.sleep(5)