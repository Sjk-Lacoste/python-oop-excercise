class Person:
    def __init__(self, name, age, gender, interests = []):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    @staticmethod
    def check_interests(interests = []):
        empty_string = ''
        likes = interests
        i = 0
        for interest in likes:
            if not likes[:-1]:
                empty_string += interest + ' '
            else:
                if i == len(likes) - 1:
                    empty_string += 'and ' + interest 
                else: 
                    empty_string += interest + ', '

            i += 1
        return empty_string

    def hello(self):
        my_interest = self.check_interests(self.interests)
        return 'Hello, my name is {} and I am {} years old. My interests are {}'.format(self.name, self.age, my_interest)


# if __name__ == "__main__":
#     person = Person('Tshepo', 45, 'male', ['agile', 'strong willed', 'etc'])
#     greeting = person.hello()
#     print(greeting)
