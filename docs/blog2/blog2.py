from seal import *
import random
    
def customHE():
        #setup SEAL parameters
        parms = EncryptionParameters(scheme_type.bgv)
        polyModDeg = 8192
        parms.set_poly_modulus_degree(polyModDeg)
        parms.set_coeff_modulus(CoeffModulus.BFVDefault(polyModDeg))
        parms.set_plain_modulus(PlainModulus.Batching(polyModDeg, 20))
        context = SEALContext(parms)
    
        #generate keys
        keygen = KeyGenerator(context)
        secretKey = keygen.secret_key()
        publicKey = keygen.create_public_key()
        relinKeys = keygen.create_relin_keys()

        #initiallize encrytor and decryptor
        encryptor = Encryptor(context, publicKey)
        evaluator = Evaluator(context)
        decryptor = Decryptor(context, secretKey)

        #initiallize batch encoding for encryption
        batchEncode = BatchEncoder(context)
        slotCount = batchEncode.slot_count()
        rowSize = slotCount / 2
        print(f'Plaintext matrix row size: {rowSize}\n')

        #create plaintext string data to be encrypted
        msg = ["Hello", "this is a secret message", "you should not have the secret key", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin tempor, leo a condimentum cursus, odio augue malesuada est, dapibus interdum dui mi et lectus. Vivamus pharetra erat orci. Nunc congue dolor non dolor ultrices tempor. Sed a velit lacinia leo porta dictum nec malesuada justo. Morbi sollicitudin quam sit amet enim lobortis, nec pretium ligula gravida. Ut odio ante, mattis et ante quis, laoreet ornare augue. Morbi ut lacus lacus. Etiam nec est luctus, gravida elit a, fermentum nibh. Vestibulum aliquam nisi non eros lobortis tristique. Maecenas iaculis ex sed eros feugiat sollicitudin. Ut convallis dolor quis leo tempor egestas. Quisque hendrerit odio vitae erat egestas egestas. Sed in commodo risus, nec elementum neque."]
    
        concMsg = ' '.join(msg)
        
        #convert message into numbers
        matrix = convMsgtoNum(concMsg, slotCount)
    
        #print original message
        print(f"Original Messages: {msg}\n")
    
        #encode messages
        plain1 = batchEncode.encode(matrix)
    
        #encrypt messages
        encrypted1 = encryptor.encrypt(plain1)

        #decrypt the encrypted data
        decrypted_result = decryptor.decrypt(encrypted1)
        podResult = batchEncode.decode(decrypted_result)
        
        #print the decrypted message
        print(f"Decrypted Message: {convNumtoMsg(podResult)}\n")
        
        #show characteristics of the ciphertext
        noise = decryptor.invariant_noise_budget(encrypted1)
        print(f"Noise budget of ciphertext: {noise} bits\n")
        size = encrypted1.size()
        print(f"Size of ciphertext: {2} polynomials\n")
        params = encrypted1.parms_id()
        print(f"Encryption parameters of ciphertext: {params}\n")

#function to convert string message to numerical numbers using the ord() function
def convMsgtoNum(message, slotCount):
        # Convert the message to a numerical representation (plaintext)
        return [ord(char) for char in message]


def convNumtoMsg(numbers):
        # Convert numerical representation back to string message
        return ''.join(chr(number) for number in numbers)


if __name__ == "__main__":
        customHE()
