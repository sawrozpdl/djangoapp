import random
import string


def genId():
    return ''.join([random.choice(string.ascii_letters
                                  + string.digits) for n in range(10)])
 