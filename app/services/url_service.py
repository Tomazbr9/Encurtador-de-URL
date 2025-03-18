import random
import string

def generate_code() -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))
