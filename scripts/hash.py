from core import output

class Brute (object):
    def __init__ (self):
        self.hash_type = raw_input ('Enter hash type: ')

    def run (self, **kwargs):

        import hashlib

        if self.hash_type == 'md5':
            if kwargs ['current_login'] == hashlib.md5(kwargs ['current_password']).hexdigest():
                st_good = 'Hash: ' + kwargs ['current_login'] + ' Unhash: ' + kwargs ['current_password']
                print output.YES + st_good
                exit ()
            else:
                print output.NO + 'Unhash ' + kwargs ['current_password'] + ' is not for hash ' + kwargs ['current_login']
        elif self.hash_type == 'sha1':
            if kwargs ['current_login'] == hashlib.sha1(kwargs ['current_password']).hexdigest():
                st_good = 'Hash: ' + kwargs ['current_login'] + ' Unhash: ' + kwargs ['current_password']
                print output.YES + st_good
                exit()
            else:
                print output.NO + 'Unhash ' + kwargs ['current_password'] + ' is not for hash ' + kwargs ['current_login']
        elif self.hash_type == 'sha224':
            if kwargs ['current_login'] == hashlib.sha224(kwargs ['current_password']).hexdigest():
                st_good = 'Hash: ' + kwargs ['current_login'] + ' Unhash: ' + kwargs ['current_password']
                print output.YES + st_good
                exit()
            else:
                print output.NO + 'Unhash ' + kwargs ['current_password'] + ' is not for hash ' + kwargs ['current_login']
        elif self.hash_type == 'sha256':
            if kwargs ['current_login'] == hashlib.sha256(kwargs ['current_password']).hexdigest():
                st_good = 'Hash: ' + kwargs ['current_login'] + ' Unhash: ' + kwargs ['current_password']
                print output.YES + st_good
                exit()
            else:
                print output.NO + 'Unhash ' + kwargs ['current_password'] + ' is not for hash ' + kwargs ['current_login']
        elif self.hash_type == 'sha384':
            if kwargs ['current_login'] == hashlib.sha384(kwargs ['current_password']).hexdigest():
                st_good = 'Hash: ' + kwargs ['current_login'] + ' Unhash: ' + kwargs ['current_password']
                print output.YES + st_good
                exit()
            else:
                print output.NO + 'Unhash ' + kwargs ['current_password'] + ' is not for hash ' + kwargs ['current_login']
        elif self.hash_type == 'sha512':
            if kwargs ['current_login'] == hashlib.sha512(kwargs ['current_password']).hexdigest():
                st_good = 'Hash: ' + kwargs ['current_login'] + ' Unhash: ' + kwargs ['current_password']
                print output.YES + st_good
                exit()
            else:
                print output.NO + 'Unhash ' + kwargs ['current_password'] + ' is not for hash ' + kwargs ['current_login']