def join_text(string1, string2):
    return string1 + string2

def capitalize_text(string):
    return string.capitalize()

def titlecase_text(string):
    return string.title()

def uppercase_text(string):
    return string.upper()

if __name__ == "__main__":
    print("Joining text:", join_text('py', 'thon'))
    print("Capitalizing text:", capitalize_text('hello there'))
    print("Title case text formatting:", titlecase_text('kentucky fried chicken'))
    print("Uppercase text formatting:", uppercase_text('yeeeeeeeehaw'))