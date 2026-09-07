# Engineering Log

## Week 1 - Toolkit v0.1

### Added
- Caesar cipher educational implementation
- Brute force demonstration
- Frequency analysis helper

### Security Lesson
Classical ciphers are useful for learning, but they should never be used to protect real data.

### Reflection
I was able to get a better idea with hands on learning as well as teaching on how much we should rely on already built systems and be able to continue to implement on those instead of building a unsecure encryption. I learned about key spaces, brute force pros, ciphers, how to code and implement different ways of ciphers and caesar ciphers to decrypt and encrypt.



## Week 2 - Toolkit v0.2

### Added
- GCD and modular inverse utilities
- Educational modular arithmetic utilities
- Security-focused randomness helpers

### Security Lesson
In Encryptions you want to ensure that the mathmaical equations that are responsible for the calculations are correct, if not, it can be definetly decrypted or even not work, or even worse, you are not able to reverse the encryption.

### Reflection
1. Which modules did you add?
Modular Arthmetic Module, GCD & Inverses Module, and Randomness Utilities Module.
2. Which mathematical function was most difficult to understand?
Extended_gcd was the most difficult to understand, being able to keep track of all of the coefficients requires more insurance that you didn't forget a coefficient when computing.
3. What is one way randomness can fail in a cryptographic system?
Randomness can fail in cryptographic system is how you apply modulo 10 for example the modulo bias byte % 10 in the notebook, the graph shows how there is going to be a certain amount of numbers that are going to show more staticially. If the number is not divisible such as the example, it will skew the numbers on the output, and that is shown on the graph on Part 7.
4. What is one rule you will follow when generating random values in future projects?
Being able to eliminate the modulo bias is important, use a vetted cryptographic library, such as secrets module, and .randbelow() that have built in range bounded functions already. 
