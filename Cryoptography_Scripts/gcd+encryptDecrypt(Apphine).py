def gcd(a,b):
  if(b == 0):
    return abs(a)
  else:
    return gcd(b,a%b)
def encrypt(plaintext, a, b):

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                char_val = ord(char) - ord('A')
                new_char_val = (a * char_val + b) % 26
                new_char = chr(new_char_val + ord('A'))
            else:
                char_val = ord(char) - ord('a')
                new_char_val = (a * char_val + b) % 26
                new_char = chr(new_char_val + ord('a'))
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, a, b):
    """
    Decrypts the given ciphertext using the affine transformation with parameters a and b.
    """
    plaintext = ""
    a_inv = None
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    if a_inv is None:
        return "Error: Invalid value of 'a'."
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                char_val = ord(char) - ord('A')
                new_char_val = (a_inv * (char_val - b)) % 26
                new_char = chr(new_char_val + ord('A'))
            else:
                char_val = ord(char) - ord('a')
                new_char_val = (a_inv * (char_val - b)) % 26
                new_char = chr(new_char_val + ord('a'))
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

print(encrypt("mr. barnes is really cool",7,3))
print(decrypt('adoopldi pq zbgiedxdzl pq uqdglqpx pq pgd pq ijp piedq',9, 19))

print("The GCD is "+ str(gcd(11,5)))