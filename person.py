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
        
        for count,ele in enumerate(likes):
            if count == len(likes) - 2:
                empty_string += ele + ' and '
            elif count == len(likes) -1:
                empty_string += ele + ''
            else:
                empty_string += ele + ', '
        return empty_string

    def hello(self):
        my_interest = self.check_interests(self.interests)
        return 'Hello, my name is {} and I am {} years old. My interests are {}'.format(self.name, self.age, my_interest)


# if __name__ == "__main__":
#     person = Person('Tshepo', 45, 'male', ['agile', 'strong willed', 'coding'])
#     greeting = person.hello()
#     print(greeting)
