import smtplib
import string
import config
from functions import is_on

def email_alert(socket,components):

    if not is_on(socket, config.owner):
        send_alert(components, config.owner_email)


def send_alert(component, to_address):
    sender = component['sender']
    channel = component['action_args'][0]
    message = component['arguments']

    msg = 'From: {0}\r\nTo: {1}\r\n\r\n{2}({3}) said:\r\n{4}'.format(
            config.from_email_address, to_address, sender, channel, message)

    try:
        server = smtplib.SMTP(config.smtp_server, config.smtp_port, timeout=2)
    except smtplib.SMTPException as e:
        print e
        server.quit()
        return False
    except IOError as e:
        print e
        return False

    try:
        server.sendmail(config.from_email_address, to_address, msg)
    except smtplib.SMTPException as e:
        print e
        server.quit()

        return False

    server.quit()
    return True
