estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_finais = []

print("Digite o conjunto de estados: ", end="")
estados = input().split()

print("Digite o alfabeto de entrada: ", end="")
alfabeto = input().split()

print("Digite o estado inicial: ", end="")
estado_inicial = input()

print("Digite o conjunto de estados finais: ", end="")
estados_finais = input().split()

print("Defina a funcao de transicao: ")
for estado in estados:
    for simbolo in alfabeto:
        print(f"Transição para o estado '{estado}' com o símbolo '{simbolo}': ", end="")
        proximo_estado = input()

        if proximo_estado == ".":
            func_transicao[(estado, simbolo)] = None
        else:
            func_transicao[(estado, simbolo)] = proximo_estado

# Reconhecendo a linguagem
print("Digite a linguagem a ser reconhecida: ", end="")
entrada = input()

estado_atual = estado_inicial

for simbolo in entrada:
    print(f"Estado atual: {estado_atual}")
    print(f"Entrada atual: {simbolo}")

  

    estado_atual = func_transicao.get((estado_atual, simbolo))

    if estado_atual is None:
        print("O automato nao reconhece a linguagem")
        break

    print(f"Proximo estado: {estado_atual}")
else:
    if estado_atual in estados_finais:
        print("Reconheceu a linguagem")
    else:
        print("O automato nao reconhece a linguagem")
