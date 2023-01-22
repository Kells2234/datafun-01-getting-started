"""
This example illustrates basic Python interactions.

1) Getting input from the user.
2) Showing output to the screen with the print() function.

The terminal is also called the command line, console, or shell.

Statements
----------

Statements are the building blocks of Python programs.
Statements are instructions that tell the computer to do something.
Each line below is a statement.

"""

# print an empty line to the screen
print()

# print a string to the screen
print("Greetings!")

# get input from the user
name = input("What is your name?: Kelly")

# use what you got
print("Hello " + name.capitalize() + "!")
print()

# Let's do some math and show off our skills

triangle_base = 10
triangle_height = 5
triangle_area = triangle_base * triangle_height / 2
print(triangle_area)
print()
print("I just calculated something, but that output is not very useful.")
print("Read the code and I'll try again.")
print()
print("The area of the triangle is " + str(triangle_area))
print()
print("Hmm... that's a bit better.")
print("We used the built-in str() function ")
print("to convert a calculated number to a string")
print("add it to a sentence.")
print()

response = input("Would you like to see all the built-in functions? (y/n)")

if response == "y":
    print()
    print("We could list them ALL with:")
    print()
    print("dir(__builtins__)")
    print()

    print("But we'll just open a web page instead.")
    import webbrowser

    webbrowser.open_new("https://docs.python.org/3/library/functions.html")

    print()
    print("That's a lot of functions!")
    print("We'll learn about them later.")
    print()
