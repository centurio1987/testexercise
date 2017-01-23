class Person:
    identity = 'Person'

    def __init__(self, age=10, name='kim'):
        self.age = age
        self.name = name

    def hello(self):
        greeting = 'hand shaking'
        print(greeting)

if __name__ == '__main__':
    p = Person()
    p.hello()
