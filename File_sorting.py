def get_category (filename):
    return filename.split("_")[0]

def get_extension (filename):
    return filename.split(".")[-1]