# Inicializar as variáveis
total_entrevistados = 0
total_sim = 0
total_nao = 0
total_mulheres_sim = 0
total_homens_nao = 0

# Loop para coletar as informações dos entrevistados
while True:
    sexo = input("Digite o sexo do entrevistado (M/F): ")
    idade = int(input("Digite a idade do entrevistado: "))
    resposta = input("Digite a resposta do entrevistado (S/N/I): ")

    # Verificar se a resposta é válida
    if resposta not in ['S', 'N', 'I']:
        print("Resposta inválida. Digite S, N ou I.")
        continue

    # Incrementar as variáveis de acordo com as respostas
    total_entrevistados += 1
    if resposta == 'S':
        total_sim += 1
        if sexo == 'F':
            total_mulheres_sim += 1
    elif resposta == 'N':
        total_nao += 1
        if sexo == 'M':
            total_homens_nao += 1

    # Verificar se o usuário deseja continuar coletando informações
    continuar = input("Deseja continuar coletando informações? (S/N): ")
    if continuar.upper() == 'N':
        break

# Imprimir os resultados
print("Total de entrevistados: ".format(total_entrevistados))
print("Total de respostas 'Sim':".format(total_sim))
print("Total de respostas 'Não':".format(total_nao))
print("Total de mulheres que responderam 'Sim':".format(total_mulheres_sim))
print("Total de homens que responderam 'Não':".format(total_homens_nao))