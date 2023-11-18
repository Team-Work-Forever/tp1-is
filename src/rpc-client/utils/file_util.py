import base64

def encode_file(data):
    return base64.b64encode(data).decode('utf-8')

def decode_file(encoded_data):
    return base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')

def store_file(file_name: str, file_data: str):
    with open("src/rpc-client/vendor/" + file_name, "w") as file:
        file.write(file_data)

__all__ = [encode_file, decode_file, store_file]