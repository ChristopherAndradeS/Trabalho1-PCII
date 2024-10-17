#
#  _____                   _             _   _____      _             __               
# |_   _|                 (_)           | | |_   _|    | |           / _|              
#   | | ___ _ __ _ __ ___  _ _ __   __ _| |   | | _ __ | |_ ___ _ __| |_ __ _  ___ ___ 
#   | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |   | || '_ \| __/ _ \ '__|  _/ _` |/ __/ _ \
#   | |  __/ |  | | | | | | | | | | (_| | |  _| || | | | ||  __/ |  | || (_| | (_|  __/
#   \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|_|  \___/_| |_|\__\___|_|  |_| \__,_|\___\___|
#                                                                                     
#
#   terminal interface, feita por Christopher Andrade
                                                             
import os
import platform
import time
import sys

#   PRE-SETS
#
#   Configure de acordo com o projeto atual
#
APRESENTATION_TIME_MS               = (6000)                        # Tempo (ms) do menu de apresentação
MAX_TEXT_LEN                        = (256)                         # Tamanho máximo do terminal input
COMMAND_PREFIX                      = '/'                           # Prefixo que identifica os comandos digitados
TERMINAL_INPUT_MSG_INT              = '[ » ] Selecione uma opção: ' # Menssagem de solicitação de input para números
TERMINAL_INPUT_MSG_STRING           = '[ » ] Digite um texto: \n'   # Menssagem de solicitação de input para texto
TERMINAL_WIDTH                      = (100)                         # Largura do terminal em "_"
DIR_DEFAULT                         = 'scriptfiles/default.ini'     # Nome da pasta de arquivos de código

#   CONSTS
#
#   Não é necessário mexer, apenas caso necessário
#
TYPE_INT                            = (0x10)                        # flag do tipo 'int'
TYPE_STRING                         = (0x20)                        # flag do tipo 'texto'
TYPE_FILE                           = (0x30)                        # flag do tipo 'arquivo'
INPUT_CMD                           = (0x80)                        # flag do tipo 'comando'
INVALID_INPUT_INT                   = (-1)                          # flag para 'input númerico inválido'
INVALID_INPUT_STRING                = 'null'                        # flag para 'input texto inválido'                  

#   MENUS ID'S
#
#   Definição global dos menus do projeto
#   
MENU_INIT                           = (1)
MENU_MAIN                           = (2)

#   'ClearTerminal()' limpa o terminal
def ClearTerminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

#   'KillTerminal()' finaliza o programa
def KillTerminal():
    sys.exit()

#   'TerminalDelay(ms)' deixa o programa em delay durante 'ms' milessegundos
def TerminalDelay(ms):      
    time.sleep(ms / 1000)

#   'GetTerminalBounds(width)' imprime as bordas da interface do programa com largura = 'width'
def GetTerminalBounds(width = TERMINAL_WIDTH): 
    return ("_" * width + "\n")

#   'ClearTerminalMenu()' limpa todas as variavéis globais
def ClearTerminalMenu():
    return 1

#   'SendTerminalMessage(msg)' envia 'msg' formatada para a interface do programa
def SendTerminalMessage(msg):
    print(GetTerminalBounds())
    print(msg)
    print(GetTerminalBounds())

#   'SendTerminalCommand(cmd)' envia um comando 'cmd'(sem o prefixo) para o terminal'
def SendTerminalCommand(cmd):
    global COMMAND_MENU , COMMAND_QUIT

    #   /menu
    if cmd == COMMAND_MENU:
        ClearTerminalMenu()
        CreateTerminalMenu(MENU_MAIN)

    #   /quit
    if cmd == COMMAND_QUIT:
        ClearTerminal()
        print("\n[ » ] Programa encerrado\n")
        TerminalDelay(2000)
        KillTerminal()

    else:
        return 0

#   'GetTerminalInput()' trata as entradas digitadas: tipo arquivo, número e texto'
def GetTerminalInput(input_msg, input_type, min_range = -1, max_range = -1, len_txt = MAX_TEXT_LEN, eflag = False, directory = DIR_DEFAULT):

    default_msg = input_msg

    if input_type == TYPE_FILE:
        while True:
            input_txt = input(input_msg)
            
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                
            flag = True
            for i in range(len(input_txt)):
                letter = ord(input_txt[i])
                if  (letter >= 48 and letter <= 57) or (letter >= 65 and letter <= 90) or (letter >= 97 and letter <= 122):
                    continue
                else:
                    flag = False
                    break

            if not flag:
                input_msg = f"[ x ] O nome digitado não é válido para nomear arquivos\n"
                continue
            
            if(len(input_txt) > len_txt):
                input_msg = f"[ x ] Entrada inválida. Escreva um nome com no máximo 10 caracteres:\n"
                continue

            if os.path.exists(directory) != eflag:
                input_msg = f"[ x ] \"{directory}\""
                input_msg += " já existe:\n" if not eflag else " não existe:\n"
                continue

            return input_txt
                
    if input_type == TYPE_INT:
        while True:
            input_txt = input(input_msg + default_msg if default_msg != input_msg else input_msg)
                
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                else: 
                    input_msg = f"[ x ] O comando digitado não existe. Tente novamente\n"
                    continue
            
            if not input_txt.isnumeric():
                input_msg = f"[ x ] Entrada inválida. Digite um número inteiro.\n"
                continue

            input_value = int(input_txt)
            
            if min_range != max_range:
                if (input_value < min_range or input_value > max_range):    
                    input_msg = f"[ x ] Entrada inválida. Digite um valor entre {min_range} e {max_range}.\n"
                    continue
            if min_range == max_range:
                if (input_value != min_range) and min_range != -1:    
                    input_msg = f"[ x ] Entrada inválida. Só há uma opção {min_range}.\n"
                    continue

            return input_value

    if input_type == TYPE_STRING:
        while True:
            input_txt = input(input_msg + default_msg if default_msg != input_msg else input_msg)
            
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                else: 
                    input_msg = f"[ x ] O comando digitado não existe. Tente novamente\n"
                    continue

            if(len(input_txt) > len_txt):
                input_msg = f"[ x ] Entrada inválida. Escreva um texto com no máximo {MAX_TEXT_LEN} caracteres:\n"
                continue

            return input_txt

#   'SendTermialInput(msg, typeinput, menuid, min, max)'
#
#   Envia uma mensagem e um campo para inserir uma entrada (input) na interface. A qual é analisada
#   posteriormente em 'GetTerminalInput(input_msg, typevar, min_range, max_range, len_txt)'

def SendTermialInput(msg, input_type, menuid, min = -1, max = -1, len_txt = MAX_TEXT_LEN, exists = False):
    
    if input_type == TYPE_FILE:
        input_txt = INVALID_INPUT_STRING
        while True:
            input_txt = GetTerminalInput(msg, input_type, min_range = min, max_range = max, eflag = exists)
            if input_txt == INPUT_CMD: return 1
            else:  
                return SendMenuResponse(menuid, input_txt)
            
    if input_type == TYPE_INT:
        input_value = INVALID_INPUT_INT
        while True:
            input_value = GetTerminalInput(msg, input_type, min_range = min, max_range = max, eflag = exists)
            if input_value == INPUT_CMD: return 1
            else:  
                return SendMenuResponse(menuid, input_value)
    
    if input_type == TYPE_STRING:
        input_txt = INVALID_INPUT_STRING
        while True:
            input_txt = GetTerminalInput(msg, input_type, min, max, len_txt)
            if input_txt == INPUT_CMD: return 1
            else: 
                return SendMenuResponse(menuid, input_txt)

#   'CreateTerminalMenu(menuid)' cria o menu de acordo com os arquivos .txt dentros da pasta 'menus'
def CreateTerminalMenu(menuid):

    ClearTerminal()

    txt = GetTerminalBounds() + "\n"

    try:            
        file = open(f"menus/menu-{menuid}.txt", 'rt')
    except IOError: 
        print(f"Não foi possível carregar \"menus/menu-{menuid}.txt\"")
        return -1
    else:
        for line in file:
            txt += line
    
    txt += GetTerminalBounds()

    print(txt)

    return 1

#   'SendMenuResponse()' decide quais serão os próximos passos do programa de acordo com a entrada digitada pelo usuário
def SendMenuResponse(menuid, input_value):
    return 1

#
#      _ _      _          __                      
#     | (_)    | |        / _|                     
#   __| |_  ___| |_ ___  | |_ _   _ _ __   ___ ___ 
#  / _` | |/ __| __/ __| |  _| | | | '_ \ / __/ __|
# | (_| | | (__| |_\__ \ | | | |_| | | | | (__\__ \
#  \__,_|_|\___|\__|___/ |_|  \__,_|_| |_|\___|___/
#                                                 
#   dict funcs, feita por Christopher Andrade
#                            
#                       
ERROR_VALUE  = 0xEE
SUCESS_VALUE = 0xAA

phone_dict = dict()

#   Verifica se uma chave 'key' existe dentro do dicionário 'dictio'
def IsDictKeyExists(dictio, key):
    return key in dictio

#   Verifica se um valor 'value' existe dentro de uma chave 'key' existente dentro do dicionário 'dictio'
def IsValueInDictKey(dictio, key, value):
    
    if(not IsDictKeyExists(dictio, key)):
        print(f"[ x ] Não foi possível localizar a chave '{key}' dentro do dicionário, pois a mesma não existia.")
        return False

    values_list = dictio[f'{key}']
    return value in values_list

#   Cria uma chave 'key' com valor padrão 'value' dentro do dicionário 'dictio', caso já não exista
#  
#   Equivalente a função 'incluirNovoNome'
def CreateDictKey(dictio, key, value):

    if(IsDictKeyExists(dictio, key)):
        print(f"[ x ] Não foi possível criar a chave '{key}' dentro do dicionário, pois a mesma já existia.")
        return ERROR_VALUE
    
    dictio[f'{key}'] = list( [value] )

    return SUCESS_VALUE

#   Insere um novo valor 'value' dentro da lista de uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'incluirTelefone'
def AppendDictValue(dictio, key, value):

    if(not IsDictKeyExists(dictio, key)):
        print(f"[ x ] Não foi possível inserir o valor '{value}' na chave '{key}' dentro do dicionário, pois a mesma não existia.")
        return ERROR_VALUE
    
    old_values = dictio[f'{key}']

    if IsValueInDictKey(dictio, key, value):
        print(f"[ x ] '{value}' não foi adicionado em '{key}', pois já existia.")
        return ERROR_VALUE        

    dictio[f'{key}'] = old_values + list( [value] )

    return SUCESS_VALUE

#   Remove um valor 'value' de dentro da lista de uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'excluirTelefone'
def RemoveDictValue(dictio, key, value):
    
    if(not IsDictKeyExists(dictio, key)):
        print(f"[ x ] Não foi possível remover o valor '{value}' na chave '{key}' dentro do dicionário, pois a mesma não existia.")
        return ERROR_VALUE

    old_values = dictio[f'{key}']

    if not IsValueInDictKey(dictio, key, value):
        print(f"[ x ] '{value}' não foi removida em '{key}', pois não existia.")
        return ERROR_VALUE  
    
    idx = old_values.index(f'{value}')
    old_values[idx:(idx + 1)] = list()

    if len(old_values) == 0:
        dictio.pop(f'{key}')
        print(f"[ ! ] A chave '{key}' foi deletada do dicionário, não há valores associados.")
    else:
        dictio[f'{key}'] = old_values
    return SUCESS_VALUE

#   Remove uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'excluirNome'
def RemoveDictKey(dictio, key):

    if(not IsDictKeyExists(dictio, key)):
        print(f"[ x ] Não foi possível remover a chave '{key}' dentro do dicionário, pois a mesma não existia.")
        return ERROR_VALUE
    
    dictio.pop(f'{key}')
    print(f"[ ! ] A chave '{key}' foi deletada do dicionário")

    return SUCESS_VALUE

#   Retorna a lista de valores da 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'consultarTelefone'
def GetDictKeyValue(dictio, key):
    return dictio[f'{key}']

def main():
    global phone_dict
    print(phone_dict)
main()