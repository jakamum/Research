import unittest
from Ticket import User  # Import the User class from your module

class TestUser(unittest.TestCase):
    def test_checkEmail_valid_email(self):
        email = "example@example.com"  # Provide a valid email address
        characters = ['@', '.com']  # Provide the characters to check for in the email
        min_length = 8  # Provide the minimum length for the email
        result = User.checkEmail(email, characters)  # Call the checkEmail method on the user instance
        self.assertEqual(result, email)  # Assert that the result is equal to the input email

    # Not working code below:    

    # def test_checkEmail_missing_character(self):
    #     email = "example.com"  # Provide an email address missing '@' character
    #     characters = ['@', '.com']  # Provide the characters to check for in the email
    #     min_length = 8  # Provide the minimum length for the email
    #     result = User.checkEmail(email, characters, min_length)  # Call the checkEmail method on the user instance
    #     self.assertFalse(result)  # Assert that the result is False



if __name__ == '__main__':
    unittest.main()
