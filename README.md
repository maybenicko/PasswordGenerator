# PasswordGenerator

This Python script generates secure passwords using random letters, numbers, and symbols.

# Requirements

Before running this script, ensure that Python is installed on your system. This script does not have any additional dependencies.

# Usage

- Run the script using Python
- Input the desired password length when prompted
- The script will generate a random password with the specified length
- The password will be printed to the console

# Functionality

The 'gen_password' function accepts an integer argument 'length' which specifies the length of the password to be generated. The function generates a password by concatenating letters, numbers, and symbols, and then selecting random characters from the concatenated string using the 'random.choice()' function. The password is returned as a string.

The script prompts the user to input the desired password length, and then calls the 'gen_password' function with the specified length. The generated password is then printed to the console.

# Disclaimer

While this script generates random passwords, it is important to note that the security of the password also depends on factors such as the length of the password, the randomness of the generator, and the strength of the underlying hashing algorithm. Therefore, this script should be used as a starting point for generating passwords, and additional security measures may be necessary depending on the intended use case.
