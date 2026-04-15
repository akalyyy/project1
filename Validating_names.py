import re
pattern = r"^[a-z]+_\d{4}-\d{2}-\d{2}_[a-z-]+\.[a-z]+$"

def validation (filename):
    if re.fullmatch(pattern, filename):
        return True
    else:
        return False
