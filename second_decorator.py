def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")

# seolah olah nanti just_some_function akan memanggil function my_decorator, bukan direct ke just_some_function
just_some_function = my_decorator(just_some_function)

just_some_function()