import random
import string
from urllib.parse import urlparse

# Função que gera código aleatorio
def generate_code() -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))

# Função que valida urls
def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)