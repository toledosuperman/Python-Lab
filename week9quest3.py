import string
alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
def _encrypt(text,alphabets):
    def shift(alphabet):
        return alphabet[3:] + alphabet[:3]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

def _decrypt(text,alphabets):
    def shift(alphabet):
        return alphabet[:3] + alphabet[3:]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

plaintext=input("Enter your password: ")
print("Your encrypted password is: ")
encrypted = _encrypt(plaintext,alphabets=alphabets)
print(encrypted)
print("Your decrypted password is: ")
decrypted=_decrypt(plaintext,alphabets=alphabets)
print(decrypted)
