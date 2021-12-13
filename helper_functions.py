
import secrets
import string


def makeId(N):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                                  for i in range(N))


