import requests
import hashlib

class Passchecker:
    
    def __init__(self, password):
      self.BASE_URL ='https://api.pwnedpasswords.com/range/'
      self.password = password
      
      
    def request_api_data(self, query_char):
        res = requests.get(f'{self.BASE_URL}{query_char}');
        if res.status_code != 200:
            raise RuntimeError(f'Error fetching: ${res.status_code}')
        return res;

    def get_pwd_leaked_count(self, hashes, hash_to_check):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        
        for hash,count in hashes:
            if(hash == hash_to_check):
                return f'{self.password} was found {count} times... Please consider updating your password.'
        return f'Your password seems fine.'

    def pwned_api_check(self):
        #check password if it exits in api response 
        hashed_pwd = hashlib.sha1(self.password.encode('utf-8')).hexdigest().upper();
        first5_char,tail = hashed_pwd[:5], hashed_pwd[5:]
        res = self.request_api_data(first5_char)
        return self.get_pwd_leaked_count(res,tail)