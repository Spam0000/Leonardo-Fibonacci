def get_valid_input():
    while True:
        try:
            numbers = int(input("Entrez le nombre de termes de la séquence de Fibonacci à générer : "))
            if numbers <= 0:
                print("Veuillez entrer un nombre entier positif supérieur à zéro.")
            else:
                return numbers
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

numbers = get_valid_input()

result = fibonacci(numbers)

print(result)
