from seal import *
import numpy as np

def print_vector(vector):
    print('[ ', end='')
    for i in range(0, min(len(vector), 8)):
        print(vector[i], end=', ')
    print('... ]')

def homomorphic_operations():
    # Setup Encryption Parameters
    parms = EncryptionParameters(scheme_type.BFV)
    poly_modulus_degree = 8192
    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus(CoeffModulus.BFVDefault(poly_modulus_degree))
    parms.set_plain_modulus(PlainModulus.Batching(poly_modulus_degree, 20))
    context = SEALContext(parms)

    # Key Generation
    keygen = KeyGenerator(context)
    secret_key = keygen.secret_key()
    public_key = keygen.create_public_key()
    relin_keys = keygen.create_relin_keys()

    # Encryptor, Evaluator, and Decryptor
    encryptor = Encryptor(context, public_key)
    evaluator = Evaluator(context)
    decryptor = Decryptor(context, secret_key)

    # Batch Encoder
    batch_encoder = BatchEncoder(context)
    slot_count = batch_encoder.slot_count()
    row_size = slot_count // 2
    print(f'Plaintext matrix row size: {row_size}')

    # Encrypt two plaintext matrices
    matrix1 = np.random.randint(0, 100, row_size).tolist()
    matrix2 = np.random.randint(0, 100, row_size).tolist()

    plaintext_matrix1 = batch_encoder.encode(matrix1)
    plaintext_matrix2 = batch_encoder.encode(matrix2)

    encrypted_matrix1 = Ciphertext()
    encrypted_matrix2 = Ciphertext()

    encryptor.encrypt(plaintext_matrix1, encrypted_matrix1)
    encryptor.encrypt(plaintext_matrix2, encrypted_matrix2)

    # Perform addition on encrypted matrices
    encrypted_sum = Ciphertext()
    evaluator.add(encrypted_matrix1, encrypted_matrix2, encrypted_sum)

    # Perform multiplication on encrypted matrices
    encrypted_product = Ciphertext()
    evaluator.multiply(encrypted_matrix1, encrypted_matrix2, encrypted_product)

    # Decrypt and print results
    decrypted_sum = Plaintext()
    decryptor.decrypt(encrypted_sum, decrypted_sum)
    sum_result = batch_encoder.decode(decrypted_sum)

    decrypted_product = Plaintext()
    decryptor.decrypt(encrypted_product, decrypted_product)
    product_result = batch_encoder.decode(decrypted_product)

    print('Matrix 1:')
    print_vector(matrix1)

    print('Matrix 2:')
    print_vector(matrix2)

    print('Encrypted Sum:')
    print_vector(sum_result)

    print('Encrypted Product:')
    print_vector(product_result)


if __name__ == "__main__":
    homomorphic_operations()
