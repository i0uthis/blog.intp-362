from seal import *
import random

def print_vector(vector):
    print('[ ', end='')
    for i in range(0, len(vector)):
        print(vector[i], end=', ')
    print('... ]')

def custom_homomorphic_operations():
    #setup SEAL parameters
    parms = EncryptionParameters(scheme_type.bgv)
    poly_modulus_degree = 8192
    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus(CoeffModulus.BFVDefault(poly_modulus_degree))
    parms.set_plain_modulus(PlainModulus.Batching(poly_modulus_degree, 20))
    context = SEALContext(parms)
    
    #generate keys
    keygen = KeyGenerator(context)
    secret_key = keygen.secret_key()
    public_key = keygen.create_public_key()
    relin_keys = keygen.create_relin_keys()

    #
    encryptor = Encryptor(context, public_key)
    evaluator = Evaluator(context)
    decryptor = Decryptor(context, secret_key)

    #
    batch_encoder = BatchEncoder(context)
    slot_count = batch_encoder.slot_count()
    row_size = slot_count / 2
    print(f'Plaintext matrix row size: {row_size}')

    #create plaintext string data to be encrypted
    message = "Hello, This is a secret message."
    
    #convert message into numbers
    matrix1 = convert_message_to_numbers(message, slot_count)
    
    #print original message
    print(f"Original Message: {message}")
    
    #encode and encrypt plaintexts
    plain1 = batch_encoder.encode(matrix1)
    encrypted1 = encryptor.encrypt(plain1)
    
    print(f"Ecryption: {encrypted1}")

    #decrypt the encrypted data
    decrypted_result = decryptor.decrypt(encrypted1)
    pod_result = batch_encoder.decode(decrypted_result)

    #convert the decrypted values back to a string message
    decrypted_message = convert_numbers_to_message(pod_result)

    #print the decrypted message
    print(f"Decrypted Message: {decrypted_message}")

#function to convert string message to numerical numbers using the ord() function
def convert_message_to_numbers(message, slot_count):
    # Convert the message to a numerical representation (plaintext)
    return [ord(char) for char in message]


def convert_numbers_to_message(numbers):
    # Convert numerical representation back to string message
    return ''.join(chr(number) for number in numbers)


if __name__ == "__main__":
    custom_homomorphic_operations()
