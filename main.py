print('Digite um cnpj para saber se é matemáticamente válido ou não')
cnpj = input('CNPJ:  ')

def remover_caracteres(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('.', '')
    return cnpj
    
cnpj_sem_caracteres = remover_caracteres(cnpj)
cnpj_puro = cnpj_sem_caracteres[:12]
lista_resultado = []

def encontrando_digito(cnpj_puro):
    contador = 5
    for numero in cnpj_puro:
        resultado = int(numero) * contador
        lista_resultado.append(resultado)
        contador -= 1
        if contador == 1:
            contador = 9
            continue
    soma_resultado = sum(lista_resultado)
    formula = 11 -(soma_resultado % 11)
    formula = formula if formula <= 9 else 0
    cnpj_puro = cnpj_puro + str(formula)
    lista_resultado.clear()
    return cnpj_puro

def encontrando_seg_digito(cnpj_1dig):
    contador = 6
    for numero in cnpj_1dig:
        resultado = int(numero) * contador
        lista_resultado.append(resultado)
        contador -= 1
        if contador == 1:
            contador = 9
            continue
    soma_resultado = sum(lista_resultado)
    formula = 11 -(soma_resultado % 11)
    formula = formula if formula <= 9 else 0
    novocnpj = cnpj_1dig + str(formula)
    lista_resultado.clear()
    return novocnpj

def verificando_sequencias(cnpj_sem_caracteres):
    sequencia = cnpj_sem_caracteres[0] * len(cnpj_sem_caracteres)

    if sequencia == cnpj_sem_caracteres:
        return True
    else:
        return None

def validando():
    try:
        cnpj_1dig = encontrando_digito(cnpj_puro)
        novocnpj = encontrando_seg_digito(cnpj_1dig)
    except ValueError:
        return False
    
    if verificando_sequencias(cnpj_sem_caracteres) == True:
         print('CNPJ inválido. Uma sequência de números foi digitada!')
    elif novocnpj == cnpj_sem_caracteres:
         print(f'{cnpj} é válido')
    else:
         print(f'{cnpj} é inválido')
    
validar = validando()

if validar == False:
    print('Formato de dados inválidos para um CNPJ!')



