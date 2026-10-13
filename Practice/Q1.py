''' Newton’s Method for approximating square roots performs an iterative
computation that converges on the correct value. The equation :- new_guess=1/2 * (old_guess+n)/old_guess'''

'''takes a value n and repeatedly guesses the square root by making each new_guess the
old_guess in the subsequent iteration.'''

def square_root(n):
    root= n/2        # To slice the possiblity we first half the inital guess
    for i in range(20):
        root=1/2 * (root+(n/root))
    return root
number = float(input("Please enter your number: "))
print("The square root is:", square_root(number))

