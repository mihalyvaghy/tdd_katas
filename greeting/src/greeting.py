def clean_name(name):
    if name[0] == "\"":
        name = name[1:]
    if name[-1] == "\"":
        name = name[:-1]
    return name

def clean_names(names):
    return [clean_name(name) for name in names]

def oxford_comma(names):
    return "," if len(names) > 2 else ""

def join_names(greeting, names, conjunction):
    return greeting + ", " + ", ".join(names[:-1]) + oxford_comma(names) + " " + conjunction + " " + names[-1] + "!"

def greet_lower_name(name):
    return "Hello, " + name + "!"

def greet_upper_name(name):
    return "HELLO, " + name + "!"

def greet_lower_list(names):
    return join_names("Hello", names, "and") if len(names) > 0 else ""

def greet_upper_list(names):
    return join_names("HELLO", names, "AND") if len(names) > 0 else ""

def greet_lower(names):
    if len(names) > 1:
        return greet_lower_list(names)
    elif len(names) == 1:
        return greet_lower_name(names[0])
    else:
        return ""

def greet_upper(names):
    if len(names) > 1:
        return greet_upper_list(names)
    elif len(names) == 1:
        return greet_upper_name(names[0])
    else:
        return ""

def greet_list(names):
    lower_names = [name for name in names if not name.isupper()]
    upper_names = [name for name in names if name.isupper()]
    return greet_lower(lower_names) + (" AND " if len(lower_names) > 0 and len(upper_names) > 0 else "") + greet_upper(upper_names) 

def greet_name(name):
    if name:
        if not name.isupper():
            return "Hello, " + name + "!"
        else:
            return "HELLO, " + name + "!"
    else:
        return "Hello, my friend!"

def greet(names):
    if isinstance(names, list):
        names = clean_names(names)
        return greet_list(names)
    else:
        return greet_name(names)
