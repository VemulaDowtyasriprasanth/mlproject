def exciting_decorator(func):
    def wrapper():
        print("Starting line of wrapper function ")
        func()
        print("Ending line of wrapper function")
    return wrapper
@exciting_decorator
def say_hi():
    print("Hi!")

say_hi()

multiply=lambda x,y:x*y
print(multiply(2,3))