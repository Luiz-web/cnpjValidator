import random
import re
cnpj = ''

def remover_caracteres(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('.', '')
    return cnpj
    
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

def validando(cnpj):
    try:
        cnpj_sem_caracteres = remover_caracteres(cnpj)
        cnpj_puro = cnpj_sem_caracteres[:12]   
        
        cnpj_1dig = encontrando_digito(cnpj_puro)
        novocnpj = encontrando_seg_digito(cnpj_1dig)
    except ValueError as e:
        return 'Formato de CNPJ inválido'
   
    if novocnpj == cnpj_sem_caracteres:
         return f'{cnpj } é Válido'
    else:
         return f'{cnpj} é inválido'
    
def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    cnpj_random = f'{primeiro_digito}{segundo_digito}{segundo_bloco}' \
        f'{terceiro_bloco}{quarto_bloco}'
    
    primeiro_calculo = encontrando_digito(cnpj_random)
    novocnpj_aleatorio = encontrando_seg_digito(primeiro_calculo)

    return novocnpj_aleatorio

def formata():
    novocnpj_aleatorio = gera()
    formatado = f'{novocnpj_aleatorio[:2]}.{novocnpj_aleatorio[2:5]}.{novocnpj_aleatorio[5:8]}/{novocnpj_aleatorio[8:12]}-{novocnpj_aleatorio[12:14]}'
    return formatado