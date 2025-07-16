from ECC.sha256 import *
from ECC.sha512 import *
from ECC.AES import *
from ECC.curve import *
from ECC.ecc import *
from user_constant import *
from user_encrypter import *
from user_decrypter import *

import numpy as np
from encrypt import AES_encryption
from decrypt import AES_decryption
import cv2
from key_generator import KeyGenerator
import time

masterkey_generator = KeyGenerator()
key = masterkey_generator.generate_key()
master_key = np.frombuffer(key, dtype=np.uint8)
master_key = list(master_key)
print(master_key)
image_data = cv2.imread(
    "C:\\Users\\hp\\Downloads\\Hanuman1.jpg", cv2.IMREAD_GRAYSCALE)


def generate_keys():
    curve = Secp521r1()
    alice = Curve(curve)
    bob = Curve(curve)

    alice.get_prikey()
    bob.get_prikey()

    alice.get_pubkey()
    bob.get_pubkey()

    return alice, bob


alice, bob = generate_keys()

ciphertext, tag, signature = alice_encrypts(master_key, alice, bob)

master_key = np.array(master_key).reshape((4, 8))

aes_cipher = AES_encryption(image_data, master_key)

encrypted_image, metadata = aes_cipher.aes_encryption()


master_key, verify_tag, verify_sign, recovered_a_pubk = alice_decrypts(
    ciphertext=ciphertext, tag=tag, signature=signature, alice=alice, bob=bob)


if verify_tag and verify_sign:
    master_key = np.array(master_key).reshape((4, 8))
    aes_final = AES_decryption(encrypted_image, master_key, metadata)
    decrypt = aes_final.aes_decryption()


cv2.imshow('Encrypted Image', encrypted_image)
cv2.waitKey(0)

cv2.imshow('Decrypted Image', decrypt)
cv2.waitKey(0)

cv2.destroyAllWindows()
