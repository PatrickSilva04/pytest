def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email Valido'
    else:
        return 'email incorreto'
    
def eh_par(numero):
    if numero % 2 == 0:
        return 'é par'
    else:
        return 'é impar'
    
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b 
    
def validar_senha(senha):
    caractere = '@#$%&A'
    if len(senha) > 8 and \
        any (c. isdligt() for c in senha) and \
        any(c.isupper() for c in senha) and \
        any(c in caractere for c in senha ):
        return 'Senha cadastrada'
    else:
        return 'Senha nao contem elementos obrigatorios'
    
def verificar_maior_idade(idade):
    if idade <=18:
        return True
    else:
        return False
    
def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    total = 0
    
    for num in lista_numeros:
        total += num
        media = total / len(lista_numeros)
        return media
    
def eh_positivo(num):
    if num >= 0:
        return 'positivo'
    else:
        return 'negativo'
    
def status_aluno(nota):
    if nota < 3:
        return 'reprovado'
    elif nota < 7:
        return 'recuperação'
    else:
        return 'aprovado'
    
    
            
    
    
