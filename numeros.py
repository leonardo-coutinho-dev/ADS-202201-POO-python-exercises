# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: leonardo.coutinho@aluno.faculdadeimpacta.com.br

# Exercício 1

n = int(input("\n Vamos verificar se um número é primo. Primeiramente, digite um número inteiro maior ou igual a 2: \n\n"))

if n >= 2:
    print("\n Okay, o número digitado é maior ou igual a dois, continuemos! \n")
    list_of_numbers_divisible = []
    list_of_numbers_non_divisible = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            list_of_numbers_divisible.append(i)
        else:
            list_of_numbers_non_divisible.append(i)
else:
    print("\n Por favor, digite novamente o número, dessa vez usando um número maior ou igual a 2! \n")

print("\n [números] da divisão com resto zero: \n\n",
      list_of_numbers_divisible)
print("\n [números] da divisão com resto diferente de zero: \n\n",
      list_of_numbers_non_divisible)

if len(list_of_numbers_divisible) == 2:
    print("\n O número digitado é primo!")
else:
    print("\n O número digitado não é primo!")

# Exercício 2

n = int(input("\n Vamos fazer uma listagem de números primos. Primeiramente, digite um número inteiro maior ou igual a 2: \n\n"))

if n >= 2:
    list_of_numbers_divisible_2 = []
    list_of_numbers_non_divisible_2 = []
    list_of_primes = []
    print("\n Okay, o número digitado é maior ou igual a dois, continuemos! \n")
    for i in range(1, n + 1):
        for x in range(1, i + 1):
            if (i % x) == 0:
                list_of_numbers_divisible_2.append(x)
                if list_of_numbers_divisible_2 == 2:
                    list_of_primes.append(i)
            else:
                list_of_numbers_non_divisible_2.append(x)
else:
    print("\n Por favor, digite novamente o número, dessa vez usando um número maior ou igual a 2! \n")

print(list_of_primes)


def eh_primo(n):

    pass


def lista_primos(n):

    pass


def conta_primos(s):

    pass


def eh_armstrong(n):

    pass


def eh_quase_armstrong(n):

    pass


def lista_armstrong(n):

    pass


def eh_perfeito(n):

    pass


def lista_perfeitos(n):

    pass
