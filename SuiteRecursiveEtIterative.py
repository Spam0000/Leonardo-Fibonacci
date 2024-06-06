def get_valid_input(prompt, is_positive_int=False):
    while True:
        user_input = input(prompt)
        if is_positive_int:
            try:
                number = int(user_input)
                if number <= 0:
                    print("Veuillez entrer un nombre entier positif supérieur à zéro.")
                    continue
                return number
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
        else:
            return user_input

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    method = get_valid_input("Choisissez une méthode pour générer la séquence (Récursif/Iteratif) : ").lower()
    if method == "récursif":
        fibonacci_func = fibonacci_recursive
    elif method == "itératif":
        fibonacci_func = fibonacci_iterative
    else:
        print("Méthode invalide. Utilisation de la méthode itérative par défaut.")
        fibonacci_func = fibonacci_iterative

    numbers = get_valid_input("Entrez le nombre de termes de la séquence de Fibonacci à générer : ", is_positive_int=True)

    show_full_sequence = get_valid_input("Voulez-vous afficher la séquence complète (Oui/Non) : ").lower() == "oui"

    result = fibonacci_func(numbers)

    if show_full_sequence:
        print("Séquence de Fibonacci complète :")
        print(result)
    else:
        print(f"Dernier terme de la séquence de Fibonacci : {result[-1]}")

if __name__ == "__main__":
    main()
