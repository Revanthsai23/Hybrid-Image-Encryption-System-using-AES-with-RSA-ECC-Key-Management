from RSA.prime_generator import *
from RSA.rsa_utils import *
from RSA.rsa import *
from RSA.rsa_constant import e, KEY_SIZE


def generate_keys():
    p = generate_prime(KEY_SIZE)
    q = generate_prime(KEY_SIZE)

    n = get_n_value(p, q)

    phi = euler_phi(p, q)

    d = get_d_val(e=e, phi=phi)

    public_keys = public_key(e, n)

    private_keys = private_key(d, n)

    return public_keys, private_keys
