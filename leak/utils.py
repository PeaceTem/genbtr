import uuid

def generate_ref_code():
    # add slugify, add additional integers if the slug is not unique -2234sfdh the str should be generated at random using while loop to check if not unique
    code = str(uuid.uuid4()).replace("-", "")
    return code

