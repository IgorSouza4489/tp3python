import os

def listar_diretorios_arquivos(path):
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"Diretório: {item_path}")
                listar_diretorios_arquivos(item_path)
            else:
                print(f"Arquivo: {item_path}")
    else:
        print(f"Erro: o path {path} não é um diretório")

path = '/path/para/o/diretorio'
listar_diretorios_arquivos(path)

#Usando a notação Big O explique a complexidade do algoritmo elaborado para resolver a questão anterior.
#A complexidade do algoritmo é 𝑂 ( 𝑛 ) O(n), onde 𝑛 n é o número total de arquivos e subdiretórios no sistema de arquivos.

def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    #RECURSIVIDADE
    torre_de_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    torre_de_hanoi(n-1, auxiliar, destino, origem)

n = 6  
torre_de_hanoi(n, 'X1', 'X2', 'X3')  

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)


#https://www.geeksforgeeks.org/python-program-for-quicksort/
def ordena_quick(arr):
    if len(arr) <= 1:
        return arr
    pi = arr[len(arr) // 2]  
    esquerda = [x for x in arr if x < pi]
    meio = [x for x in arr if x == pi]
    direita = [x for x in arr if x > pi]
    return ordena_quick(esquerda) + meio + ordena_quick(direita)


arr = [32, 17, 73, 9, 3, 99, 11]
arr_ordenado = ordena_quick(arr)
print(arr_ordenado)


def fatorial_stack(n, acc=1):
    if n == 0:
        return acc
    else:
        return fatorial_stack(n - 1, n * acc)

print(fatorial_stack(10000))

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial_iterativo(10000))

def fatorial_cauda(n, acc=1):
    if n == 0 or n == 1:
        return acc
    else:
        return fatorial_cauda(n - 1, n * acc)
    

def eh_palindromo(palavra):
    if len(palavra) <= 1:
        return True

    if palavra[0] == palavra[-1]:
        return eh_palindromo(palavra[1:-1])
    else:
        return False

palavra = "arara"
resultado = eh_palindromo(palavra)
print(f"{resultado}")

def soma_lista(lst):
    if not lst:
        return 0
    else:
        return lst[0] + soma_lista(lst[1:])

lista = [1, 2, 3, 4]
resultado = soma_lista(lista)
print(f"A soma é: {resultado}")


def contar_repeticoes(s, caractere):
    if not s:
        return 0
    return (s[0] == caractere) + contar_repeticoes(s[1:], caractere)

print(contar_repeticoes("banana", "a"))


#https://awari.com.br/python-reverso-aprenda-a-inverter-codigos-com-facilidade/#:~:text=Invers%C3%A3o%20de%20c%C3%B3digo%20em%20Python,-Manipula%C3%A7%C3%A3o%20de%20strings&text=Por%20exemplo%2C%20uma%20string%20em,dos%20elementos%20na%20pr%C3%B3pria%20lista.
def inverter_string(s):
    if s == "":
        return s
    return s[-1] + inverter_string(s[:-1])

resultado = inverter_string("recursao")
print(resultado)  
