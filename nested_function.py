#main function
def parent():
    print("Print dari parent function.")
    # nested function
    def first_child():
        return "Print dari first_child function."

    def second_child():
        return "Print dari second_child function."

    print(first_child())
    print(second_child())

print(parent())


# if we try to call first_child() function, it will return an error
first_child()