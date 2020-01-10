import person
import pytest



# Print the greeting
def test_greeting():
    # Instance of Person class
    human = person.Person('Tshepo', 45, 'male', ['agile', 'strong willed', 'etc'])
    greeting = human.hello()
    assert greeting == "Hello, my name is Tshepo and I am 45 years old. My interests are agile, strong willed, and etc"