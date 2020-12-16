def greet(name):
    greeting = 'Hello'
    conjunction = 'and'
    print_name = name

    oxford_comma = lambda name_list: len(name_list) > 2

    if isinstance(name, list):
        if False not in map(lambda string: string.isupper(), name):
            greeting = 'HELLO'
            conjunction = 'AND'
        print_name = ', '.join(name[:-1]) + (',' if oxford_comma(name) else '') + ' ' + conjunction + ' ' + name[-1] 

    elif name:
        if name.isupper():
            greeting = 'HELLO'

    else:
        print_name = 'my friend'

    return greeting + ', ' + print_name + '!'
