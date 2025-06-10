from funcoes import *

def test_email_correto():
    assert verifica_email('test@teste.com') == 'email Valido' 
    assert verifica_email('teste') == 'email incorreto'
    assert verifica_email('teste.com') == 'email incorreto'
    assert verifica_email('teste@test') == 'email incorreto'
    
def test_verifica_se_numero_par():
        assert eh_par(3) == 'é impar'
        assert eh_par(6) == 'é par'
        
def  test_verifica_soma_e_subtrair():
    assert somar(5,6) == 11
    assert subtrair(10,8)  == 2  
    
    
def test_verifica_senha():
    assert validar_senha('test@') == 'Senha cadastrada'
    assert validar_senha('test') == 'Senha nao contem elementos obrigatorios'
    
    
def test_maior_idade():
    assert verificar_maior_idade(17) ==  False
    assert verificar_maior_idade(21) == True

def test_positivo():
    assert eh_positivo(18) == 'positivo'
    assert eh_positivo(-18) == 'negativo'
    

def test_aluno():
    assert status_aluno(4) == 'recuperação'
    assert status_aluno(8) ==  'aprovado'
    assert status_aluno(2) == 'reprovado'
    
    

    
    
    
    

    
     