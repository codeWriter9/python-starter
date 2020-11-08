from algorithms import algoutil

def fibonacci(term):
    if term == 1:
        return 1;
    elif term == 2:
        return 1;
    else :
        return (fibonacci(term - 1) + fibonacci(term - 2));