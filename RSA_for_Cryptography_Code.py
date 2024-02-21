import random

#function to the gcd of 2 numbers
def gcd(a, b):
    remainder = 0
    while(1):
        remainder = a % b
        if (remainder == 0):
            return b
        a = b
        b = remainder

#function to do extended ecuclidean for gcd, x and y which are coefficients for linear combination
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_euclidean(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

#function to find the modular inverse
def mod_inverse(e, t):
    gcd, x, y = extended_euclidean(e, t)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist since 'e' and 't' are not coprime.")
    return x % t

if __name__ == '__main__':
    #intialize values for prime numbers p, q, calculate n and t and set initial value for e
    p = 124070563
    q = 334003807
    n = p * q
    e = 2
    t = (p - 1) * (q - 1)

    #find e which is co-prime with t
    while(1):
        if gcd(e, t) == 1:
            break
        else:
            e = random.randint(2, t-1)

    #calculate d as the modular inverse of e modulo t
    d = mod_inverse(e, t)

    #message to be encrypted
    message = 12
    print("")
    print("Original message data = ", message, end="\n\n")

    #encrypt the message
    ciphertext = pow(message, e, n)
    print("+ Encryption:")
    print("Encrypted message data (ciphertext) = ", ciphertext)
    print(f"Using: \nn = {n} \ne = {e}", end = "\n\n")

    #decrypt the message
    decrypted_message = pow(ciphertext, d, n)
    print("+ Decryption:")
    print("Decrypted message data (orginal) = ", decrypted_message)
    print(f"Using: \nn = {n} \nd = {d}", end = "\n\n")
