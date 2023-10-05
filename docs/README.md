# Homomorphic Encryption: The Power of Secure Data Processing
<sub>by John Narte</sub>
<br/><br/>
## Disclaimer: WIP contents subject to change
<br/><br/>
Image here
<br/><br/>
## Introduction
In today's digital age, data is quite literally the lifeblood of businesses and organizations worldwide. The more data we generate and share, the more risks there are to data privacy and security. Organizations require a way to secure the confidentiality of their data. They can use encryption methods that will allow them to encrypt the data and so long as they have the decryption key, they are able to read said data. Which is great but once the data is decrypted the confidentiality of the data disappears because whoever has the decryption key has the means to look into the data. 
<br/><br/>
For example, I encrypted a text file that has my personal information for security reasons and an organization required me to send it in to them. Of course, I have to give them the decryption key so they are able to read it but in doing so I am pretty much letting an organization take my personal data because I don’t know if only one person will see it. This issue can be solved using homomorphic encryption, which allows calculations on encrypted data without decrypting them. 
<br/><br/>
This blog will delve deeper into homomorphic encryption, providing and in-depth understanding of what it is, different types, use cases, and challenges of its implementation.
<br/><br/>
## What is Homomorphic Encryption
A typical encryption method will use a cryptographic algorithm to convert the plaintext form of data into an encrypted form and during that process a cryptographic key or a secret key is created that will convert the encrypted data back into its plaintext form. Homomorphic Encryption differ from this because it allows computations to be performed on the encrypted data without having to use a secret key to decrypt it first. Once the computation on the encrypted data is done, the result does not come out in clear text format as it remains encrypted throughout the whole process. This eliminates the need to process data in clear text form, which can prevent a breach in data confidentiality which is the whole point of having an encryption in the first place. For this to work however there needs to be a relationship between plaintexts and ciphertexts, two ciphertexts should be able to be added or multiplied together and have the result be the same as if the same operation is done on two plaintexts. This relationship needs to be implemented in a way that it’s hidden from an observer because if the mathematical operations on ciphertexts reveals information about the corresponding plaintexts the encryption is broken.
<br/><br/>
## Types of Homomorphic Encryption
The goal of Homomorphic Encryption is to enable an infinite number of additions or multiplications on encrypted data. The problem is designing an encryption algorithm that can do all of that is hard as a result there are a few different types of homomorphic encryption and depending on how it is designed, gets closer to the final goal of the encryption.
### Partially Homomorphic Encryption (PHE)
This algorithm type allows a defined operation, either addition or multiplication, to be performed an infinite number of times. For example, a particular algorithm may be additively homomorphic, meaning adding two ciphertexts together produces the same result as encrypting the sum of the two plaintexts.
Image here<br/><br/>
PHE algorithms are relatively easy to design, in fact common encryption algorithms like the RSA algorithm are partially homomorphic by chance. The RSA algorithm is multiplicatively homomorphic, the reason for this is because the algorithm is based on exponentiation: C = (m^x)(mod n) where m is the message and x is the secret key. The rules of exponentiation say that (a^n)(b^n)=(ab)^n, this means that multiplying two cipher texts encrypted with the same key is equivalent to raising the product of the plaintext to the power of the secret key. Through this RSA algorithm is technically a PHE via multiplication
### Somewhat Homomorphic Encryption (SHE)
The next type of homomorphic encryption is somewhat homomorphic encryption, which allows a finite number of any operation rather than an infinite number of a defined operation. For example, this algorithm may be able to support any combination of up to ten additions or multiplications. If an eleventh operation of any type was to be done it would create an invalid result. This type of algorithm is the final step to achieving a fully homomorphic encryption as it is more difficult to design an algorithm that supports both addition and multiplication, even if there is a defined number of operations, than it is to create one that allows infinite additions or multiplications of ciphertexts.
### Fully Homomorphic Encryption (FHE)
The final goal of Homomorphic Encryption. A fully homomorphic encryption algorithm allows for an infinite number of additions or multiplications of ciphertexts while still producing a valid result. The FHE scheme was first proposed in 1978 and for more than 30 years it was unclear whether the scheme was possible. During that 30-year period only PHEs were created. In 2009, a plausible version of an FHE scheme was proposed by Craig Gentry. His scheme uses an SHE as the base and supports both addition and multiplication operation on ciphertexts, which is the goal of homomorphic encryptions. Since then, other algorithms have been developed that improve upon Craig Gentry’s original algorithm.
<br/><br/>
## Use Cases of Fully Homomorphic Encryption
The FHE algorithm can be used in many different industries and can even be better than some of the more common encryption types. Here are some use cases of FHE:
1. Secure Cloud Computing: could be used to allow businesses to store and process sensitive data on the cloud in a way that does not reveal the data to the cloud provider.
2. Secure Search: could be used to allow organizations to securely search through a large database of sensitive information without revealing the actual contents of the database.
3. Secure Machine Learning: could be used to allow organizations to train machine learning models on sensitive data without revealing the data to the model developers.
4. Secure e-commerce: could be used to allow organizations to securely process sensitive information such as credit card numbers and personal data during transactions.
<br/><br/>
Basically, anything that has something to do with “sensitive” data, homomorphic encryption can be used on it.
<br/><br/>
Some use cases in different industries:
Financial Services: Could be used to improve the security of cloud computing to reduce the risk of data breaches and improve the accuracy and reliability of insights.
Healthcare: Could be used to ensure the confidentiality and privacy of patient data, which can help to protect the reputation and trust of the organization.
Government: Could be used to improve security on citizen data or public records.
<br/><br/>
## Challenges of implementing Homomorphic Encryption
FHEs can solve a variety of major business challenges when it comes to handling sensitive data which means that everyone should be using it. But they aren’t. the problem with FHE is it’s efficiency. Implementation of a PHE is easy because a lot of common encryption algorithms are PHEs by accident. But implementing an FHE needs to meet the requirements of full homomorphism i.e allowing ciphertexts to be added or multiplied an infinite number of times without messing up the result. This means that these algorithms are slow and can have high storage demands.
For example IBM released an improved version of their library for homomorphic encryption in 2018. This version is apparently 25-75 times faster than the previous version, which was 2 million times faster than the original which released around 2015.
The original version performed the mathematical operations about 100 trillion times slower than performing the same operations on the corresponding plaintexts. This means that the newest version is still a million times slower than plaintext operations on average. A calculation that would take a second to perform on plaintexts would take an average of 11.5 days to perform using the 2018 version of IBM’s Homomorphic encryption library. However, a speed up of about 100 million times over 3 years is pretty impressive considering the technology is still in it’s infancy.
<br/><br/>
