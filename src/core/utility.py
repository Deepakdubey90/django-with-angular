import time
import string
import random

def base36encode(number):
        """Converts an integer into a base36 string."""
        ALPHABET = "%s%s" % ("0123456789", string.ascii_lowercase)
        
        if not isinstance(number, int):
            raise TypeError('This function must be called on an integer.')
        
        base36 = ''
        sign = ''
        
        if number < 0:
            sign = '-'
            number = -number
            
        if 0 <= number < len(ALPHABET):
            return sign + ALPHABET[number]
            
        while number != 0:
            number, i = divmod(number, len(ALPHABET))
            base36 = ALPHABET[i] + base36
        
        return sign + base36

def base36decode(number):
    return int(number, 36)

def generate_code():
    return "%s%s%s%s" % (        
        str(base36encode(int(time.time()))),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_lowercase),
    )
