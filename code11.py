import base64
class Base64EnDe:
    def encode(self, data: str) -> str:
        encoded_bytes = base64.b64encode(data.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
        return encoded_str

    def decode(self, data: str) -> str:
        decoded_bytes = base64.b64decode(data.encode('utf-8'))
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    

en_de = Base64EnDe()
original_str = "TH1s 1S 4 T3st Str1ng!"
encoded_str = en_de.encode(original_str)
decoded_str = en_de.decode(encoded_str)
    
print(f"Original String: {original_str}")
print(f"Encoded String: {encoded_str}")
print(f"Decoded String: {decoded_str}")
