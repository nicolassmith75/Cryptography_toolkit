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


## Week 3 - Toolkit v0.3

### Added
- Security module that checks security levels and brute-force cost

### Security Lesson
Security is more ambigous than imagined, there has to be many pieces of the puzzle refined and processed in order to trully have a system that works and is functional. Learning that encryptions are not ever impossible just they have requirements that at the current time people are not able to crack them is a interesting concept. It makes me interested more in super computers and how much money people spend making them, and they are still not able to crack these passwords, and how someone might make one that is able to crack all of the encryption techniques, than there will be new security systems that will be created.

### Reflection
The claim that we make when saying a cryptographic system is secure, is that we determined that the time that it would take for someone to crack the system is not possible. This requires a amount of computing power, financial resources, and time, that for example adversaries are currently able to do. The key generation in order to complete those requirements we ensure that they are truly coming from a sufficient long term truly random source, and not anything that can be predicted. We also are assuming in certain scenarios that the environment is secure and no other side-channel leaks are possible or have been updated. The likelihood that an attacker has all of these avenues cleared is very unlikely, so when people say cryptographic system is secure, they are actually saying that the system has a long term key, key generation is truly random, there are no underlying vulnerabiliites, and any other risks have been assessed and determined that there is anything that has been recognized as a possible threat.