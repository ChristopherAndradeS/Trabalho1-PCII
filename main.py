#  _____         _           _ _             __            ______  _____   _____ _____ 
# |_   _|       | |         | | |           /  |           | ___ \/  __ \ |_   _|_   _|
#   | |_ __ __ _| |__   __ _| | |__   ___   `| |   ______  | |_/ /| /  \/   | |   | |  
#   | | '__/ _` | '_ \ / _` | | '_ \ / _ \   | |  |______| |  __/ | |       | |   | |  
#   | | | | (_| | |_) | (_| | | | | | (_) | _| |_          | |    | \__/\  _| |_ _| |_ 
#   \_/_|  \__,_|_.__/ \__,_|_|_| |_|\___/  \___/          \_|     \____/  \___/ \___/ 
#
#
#
#   MACROS - INTERFACE DE MENUS
#
#
#
DEBUG_MODE                      = False                             # Modo de Debug (True - Ativado) (False - Desativado)
APRESENTATION_TIME_MS           = (5000)                            # Tempo (ms) do menu de apresentação
WAITING_TIME_MS                 = (3500)                            # Tempo (ms) de espera
MAX_TEXT_LEN                    = (256)                             # Tamanho máximo do terminal input
COMMAND_PREFIX                  = '/'                               # Prefixo que identifica os comandos digitados
COMMAND_MENU                    = 'menu' 
COMMAND_QUIT                    = 'quit' 
COMMAND_RELOAD                  = 'reload' 
TERMINAL_INPUT_MSG_INT          = '\n[ » ] Selecione uma opção: '   # Menssagem de solicitação de input para números
TERMINAL_INPUT_MSG_STRING       = '\n[ » ] Insira um texto: '       # Menssagem de solicitação de input para texto
TERMINAL_WIDTH                  = (100)                             # Largura do terminal em "_"
DIR_DEFAULT                     = 'scriptfiles'                    # Nome da pasta de arquivos de código
FILE_ENCODING                   = 'utf-8'                           # Unicode dos arquivos do menu
#
#
#
#   CONSTS
#
#
#
TYPE_INT                        = (0x10)                            # flag do tipo 'int'
TYPE_STRING                     = (0x20)                            # flag do tipo 'texto'
TYPE_FILE                       = (0x30)                            # flag do tipo 'arquivo'
INPUT_CMD                       = (0x80)                            # flag do tipo 'comando'
INVALID_INPUT_INT               = (-1)                              # flag para 'input númerico inválido'
INVALID_INPUT_STRING            = 'null'                            # flag para 'input texto inválido' 
ERROR_VALUE                     = 0xEE                              # Valor de retorno p/ 'erro'
SUCESS_VALUE                    = 0xAA                              # Valor de retorno p/ 'sucesso'                 
#
#
#
#   MENUS ID'S
#
#
#   
MENU_INIT                       = (1)                               # Menu de apresentação
MENU_MAIN                       = (2)                               # Menu principal
MENU_CREATE_NEW_NAME            = (3)                               # Menu Inserir Novo Nome
MENU_CREATE_PHONE_NUMBER        = (4)                               # Menu Inserir Telefone
MENU_REMOVE_PHONE_NUMBER        = (5)                               # Menu Remover Telefone
MENU_REMOVE_NAME                = (6)                               # Menu Remover Nome
MENU_GET_PHONE                  = (7)                               # Menu Consultar Telefone
MENU_PRINT_DICTIO               = (8)                               # Menu Vizualizar Dictio
#
#
#
#   BIBLIOTECAS - INTERFACE DE MENUS
#
#
#                                                              
import os
import platform
import time
import sys
#
#
#   FUNÇÕES - INTERFACE DE MENUS
#
#
#   'ClearTerminal()' limpa o terminal
def ClearTerminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
#
#   'KillTerminal()' finaliza o programa
def KillTerminal():
    sys.exit()
#
#   'TerminalDelay(ms)' deixa o programa em delay durante 'ms' milessegundos
def TerminalDelay(ms):      
    time.sleep(ms / 1000)
#
#   'GetTerminalBounds(width)' imprime as bordas da interface do programa com largura = 'width'
def GetTerminalBounds(width = TERMINAL_WIDTH): 
    return ("_" * width + "\n")
#
#   'SendTerminalCommand(cmd)' envia um comando 'cmd'(sem o prefixo) para o terminal'
def SendTerminalCommand(cmd):
    global COMMAND_MENU , COMMAND_QUIT

    #   /menu
    if cmd == COMMAND_MENU:
        TerminalDelay(500)
        ClearTerminal()
        CreateTerminalMenu(MENU_MAIN)

    #   /quit
    if cmd == COMMAND_QUIT:
        ClearTerminal()
        print("\n[ » ] Encerrando programa...\n")
        TerminalDelay(WAITING_TIME_MS)
        ClearTerminal()
        print("\n[ » ] Programa encerrado\n")
        KillTerminal()

    if cmd == COMMAND_RELOAD:
        ClearTerminal()
        print("\n[ » ] Reiniciando programa...\n")
        TerminalDelay(WAITING_TIME_MS)
        main()

    else:
        return 0
#
#   'SendTerminalWarning(msg)' envia uma mensagem de alerta a'msg' para o terminal'
def SendTerminalWarning(msg):
    ClearTerminal()
    print(GetTerminalBounds())
    print("\nAlerta".center(TERMINAL_WIDTH))
    print(msg)
    print(GetTerminalBounds())
    TerminalDelay(WAITING_TIME_MS - 500)
    SendTerminalCommand(COMMAND_MENU)
#
#
def SendTerminalMessage(msg, flag = True):
    print(GetTerminalBounds())
    print(msg)
    if flag:
        print(GetTerminalBounds()) 
        TerminalDelay(WAITING_TIME_MS - 500)
        SendTerminalCommand(COMMAND_MENU)

#   'GetTerminalInput()' trata as entradas digitadas: tipo arquivo, número e texto'
def GetTerminalInput(input_msg, input_type, min_range = -1, max_range = -1, len_txt = MAX_TEXT_LEN, eflag = False, directory = DIR_DEFAULT):

    default_msg = input_msg

    print(GetTerminalBounds(), end = "")

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
                input_msg = GetTerminalBounds() + f"\n[ x ] O nome digitado NÃO É VÁLIDO para nomear arquivos\n" + GetTerminalBounds()
                continue
            
            if(len(input_txt) > len_txt):
                input_msg = GetTerminalBounds() +  f"\n[ x ] Entrada INVÁLIDA. Escreva um NOME com no máximo 10 caracteres:\n" + GetTerminalBounds()
                continue

            if os.path.exists(directory) != eflag:
                input_msg = GetTerminalBounds() + f"\n[ x ] \"{directory}\""
                input_msg += " JÁ EXISTE:\n" if not eflag else " NÃO EXISTE:\n" + GetTerminalBounds()
                continue

            return input_txt
                
    if input_type == TYPE_INT:
        while True:
            input_txt = input(input_msg + default_msg if default_msg != input_msg else input_msg)
                
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                else: 
                    input_msg = GetTerminalBounds() +  f"\n[ x ] O comando digitado NÃO EXISTE. Tente novamente\n" + GetTerminalBounds()
                    continue
            
            if not input_txt.isnumeric():
                input_msg = GetTerminalBounds() +  f"\n[ x ] Entrada INVÁLIDA. Digite um NÚMERO INTEIRO.\n" + GetTerminalBounds()
                continue

            input_value = int(input_txt)
            
            if min_range != max_range:
                if (input_value < min_range or input_value > max_range):    
                    input_msg = GetTerminalBounds() +  f"\n[ x ] Entrada INVÁLIDA. Digite UM VALOR entre {min_range} e {max_range}.\n"
                    continue
            if min_range == max_range:
                if (input_value != min_range) and min_range != -1:    
                    input_msg = GetTerminalBounds() +  f"\n[ x ] Entrada INVÁLIDA. Só há UMA OPÇÃO {min_range}.\n" + GetTerminalBounds()
                    continue

            return input_value

    if input_type == TYPE_STRING:
        while True:
            input_txt = input(input_msg + default_msg if default_msg != input_msg else input_msg)
            
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                else: 
                    input_msg = GetTerminalBounds() +  f"\n[ x ] O comando digitado NÃO EXISTE. Tente novamente\n" + GetTerminalBounds()
                    continue

            if(len(input_txt) > len_txt):
                input_msg = GetTerminalBounds() +  f"\n[ x ] Entrada INVÁLIDA. Escreva UM TEXTO com no MÁXIMO {MAX_TEXT_LEN} caracteres:\n" + GetTerminalBounds()
                continue

            return input_txt
#
#   'SendTermialInput(msg, typeinput, menuid, min, max)'
#
#   Envia uma mensagem e um campo para inserir uma entrada (input) na interface. A qual é analisada
#   posteriormente em 'GetTerminalInput(input_msg, typevar, min_range, max_range, len_txt)'
#
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
#
#   'CreateTerminalMenu(menuid)' cria o menu de acordo com os arquivos .txt dentros da pasta 'menus'
def CreateTerminalMenu(menuid):

    ClearTerminal()

    txt = ''
    print(GetTerminalBounds(), end = "")

    try:            
        file = open(f"menus/menu-{menuid}.txt", 'rt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"menus/menu-{menuid}.txt\"")
        return ERROR_VALUE
    else:
        for line in file:
            line = line.replace('\n', "")
            line = line.replace('<br>', "\n")
            line = line.replace('<t>', "\t")

            if '<center>' in line:
                line = line.replace('<center>', "")
                line = line.center(TERMINAL_WIDTH)
            if '<left>' in line:
                line = line.replace('<left>', "")
                line = line.ljust(TERMINAL_WIDTH)
            if '<right>' in line:
                line = line.replace('<right>', "")
                line = line.rjust(TERMINAL_WIDTH)

            if line == "<request-input-str>" or line == "<request-input-int>":
                continue

            txt += line
    
    print(txt, end = '')
    
    if line == "<request-input-str>":
        SendTermialInput(TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
    elif line == "<request-input-int>":
        SendTermialInput(TERMINAL_INPUT_MSG_INT, TYPE_INT, menuid, 1, 6)
    else:
        print(GetTerminalBounds())
    
    return 1
#
#   'SendMenuResponse()' decide quais serão os próximos passos do programa de acordo com a entrada digitada pelo usuário
def SendMenuResponse(menuid, input_value):

    if(menuid == MENU_MAIN):
    
        if(input_value + 2 == MENU_PRINT_DICTIO):

            CreateTerminalMenu(MENU_PRINT_DICTIO)
            
            print(f"\n\n» Lista de usuários no Dicionário:")
    
            key_list = phone_dict.keys()

            if(len(key_list) == 0):
                print(f"\n\t• Lista de usuários VAZIA", end = '')
            
            else:
                for key in key_list:
                    phones = GetDictKeyValue(phone_dict, key)
                    print(f"\n\t• Lista de telefone do usuário '{key}':\n", end = '')
                    for idx, phone in enumerate(phones):
                        print(f"\t\t- {idx + 1:0>2d}. {phone}\n", end = '')

            print("\n\n",  end = '')
            print(GetTerminalBounds())
            input("[ » ] Aperte Enter para voltar ao MENU: ")
            CreateTerminalMenu(MENU_MAIN)

        else:
            CreateTerminalMenu(input_value + 2)

    if(menuid == MENU_CREATE_NEW_NAME):

        input_list = str(input_value).split(" ")

        if(len(input_list) == 1):
            SendTermialInput('\n[ x ] Digite um NOME e uma LISTA de telefones: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1

        name = input_list[0]
        phone_list = list()

        for idx in range(1, len(input_list)):
            if(IsValidPhone(input_list[idx]) and input_list[idx] != ''):
                phone_list.append(input_list[idx])

        if(len(phone_list) == 0):
            SendTermialInput('\n[ x ] A LISTA digitada está VAZIA: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        if(has_duplicates(phone_list)):
            SendTermialInput('\n[ x ] A LISTA possui TELEFONES REPETIDOS: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1

        if(not IsValidName(name)):
            SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        if(not IsValidPhoneList(phone_list)):
            SendTermialInput('\n[ x ] A LISTA de TELEFONES digitada é INVÁLIDA, use APENAS NÚMEROS [0-9]:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1        

        if(IsDictKeyExists(phone_dict, name)):
            SendTermialInput('\n[ x ] O NOME digitado JÁ EXISTE, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1    
        
        CreateDictKey(phone_dict, name, phone_list)
        SendTerminalCommand(COMMAND_MENU)

    if(menuid == MENU_CREATE_PHONE_NUMBER):

        input_list = str(input_value).split(" ")

        if(len(input_list) != 2):
            SendTermialInput('\n[ x ] Digite UM NOME e UM TELEFONE: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1

        name  = input_list[0]
        phone_list = list()

        for idx in range(1, len(input_list)):
            if(IsValidPhone(input_list[idx]) and input_list[idx] != ''):
                phone_list.append(input_list[idx])

        if(len(phone_list) == 0):
            SendTermialInput('\n[ x ] A LISTA digitada está VAZIA: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        if(not IsValidName(name)):
            SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        if(not IsValidPhoneList(phone_list)):
            SendTermialInput('\n[ x ] O TELEFONE digitado é INVÁLIDO, use APENAS NÚMEROS [0-9]:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1        

        if(not IsDictKeyExists(phone_dict, name)):
            print(GetTerminalBounds() + f"\n[ ! ] O NOME '{name}' NÃO EXISTE no dicionário.\n" + f"\n» Deseja criar UM NOVO NOME '{name}' ?\n\n\t1. Sim, quero criar\n\t2. Não, quero voltar para o menu\n" + GetTerminalBounds(), end = "")
            
            input_txt = ''
            input_msg = TERMINAL_INPUT_MSG_INT
            while True:
                input_txt = input(input_msg)
                if(input_txt == '1' or input_txt == '2'):
                    break
                else:
                    input_msg = "[ x ] Digite APENAS '1' ou '2'\n" + TERMINAL_INPUT_MSG_INT

            if(not (int(input_txt) - 1)):
                CreateDictKey(phone_dict, name, phone_list)
                SendTerminalCommand(COMMAND_MENU)
            else:
                print("[ ! ] Voltando para o menu...")
                TerminalDelay(WAITING_TIME_MS)
                SendTerminalCommand(COMMAND_MENU)

            return 1    
    
        if(IsValueInDictKeyExists(phone_dict, name, phone_list)):
            SendTermialInput('\n[ x ] O TELEFONE digitado JÁ EXISTE dentro da LISTA:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1  
        
        AppendDictValue(phone_dict, name, phone_list)
        SendTerminalCommand(COMMAND_MENU)  

    if(menuid == MENU_REMOVE_PHONE_NUMBER):

        input_list = str(input_value).split(" ")

        if(len(input_list) != 2):
            SendTermialInput('\n[ x ] Digite UM NOME e UM TELEFONE: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1

        name = input_list[0]
        phone = input_list[1]

        if(not IsValidName(name)):
            SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        if(not IsValidPhone(phone)):
            SendTermialInput('\n[ x ] o TELEFONE digitado é INVÁLIDO, use APENAS NÚMEROS [0-9]:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1 
        
        if(not IsDictKeyExists(phone_dict, name)):
            SendTermialInput('\n[ x ] O NOME digitado NÃO EXISTE, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1    

        if(not IsValueInDictKeyExists(phone_dict, name, phone)):
            SendTermialInput('\n[ x ] O TELEFONE digitado NÃO EXISTE na LISTA, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1    
        
        RemoveDictValue(phone_dict, name, phone)
        SendTerminalCommand(COMMAND_MENU) 

    if(menuid == MENU_REMOVE_NAME):

        input_list = str(input_value).split(" ")

        if(len(input_list) != 1):
            SendTermialInput('\n[ x ] Digite um NOME APENAS: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        name = input_list[0]

        if(not IsValidName(name)):
            SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        if(not IsDictKeyExists(phone_dict, name)):
            SendTermialInput('\n[ x ] O nome digitado NÃO EXISTE, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1   
        
        RemoveDictKey(phone_dict, name)
        SendTerminalCommand(COMMAND_MENU) 

    if(menuid == MENU_GET_PHONE):

        input_list = str(input_value).split(" ")

        if(len(input_list) != 1):
            SendTermialInput('\n[ x ] Digite UM NOME APENAS: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1
        
        name = input_list[0]
        
        if(not IsValidName(name)):
            SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1

        if(not IsDictKeyExists(phone_dict, name)):
            SendTermialInput('\n[ x ] O NOME digitado NÃO EXISTE, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return 1  
    
        phones = GetDictKeyValue(phone_dict, name)

        print(f"\n» Lista de telefone do usuário {name}:\n")
        for idx in range(len(phones)):
            print(f"\t• {idx + 1:0>2d}. {phones[idx]}\n")
        
        SendTermialInput("\n[ ! ] Digite outro NOME de usuário OU digite /menu para VOLTAR ao MENU\n" + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)

    return 1
#
#
#   VARIÁVEIS - DICTIO
#
#
phone_dict      = dict()    # Dicionário Globla de telefones
#
#
#   FUNÇÕES - DICTIO
#
#
#   Verifica se existe 'key' dentro do dicionário 'dictio'
def IsDictKeyExists(dictio, key):
    return key in dictio
#
#   Verifica se um valor 'value' existe dentro de uma chave 'key' existente dentro do dicionário 'dictio'
def IsValueInDictKeyExists(dictio, key, value):
    
    if(not IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível LOCALIZAR a CHAVE '{key}' dentro do dicionário, pois a mesma NÃO EXISTIA.")
        return False

    values_list = dictio[f"{key}"]

    return value in values_list
#
#   Cria uma chave 'key' com valor padrão 'value' dentro do dicionário 'dictio', caso já não exista
#  
#   Equivalente a função 'incluirNovoNome'
def CreateDictKey(dictio, key, values_list):

    if(IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível CRIAR a chave '{key}' dentro do dicionário, pois a mesma JÁ EXISTIA.")
        return ERROR_VALUE
    
    dictio.update({f"{key}": values_list})

    SendTerminalMessage(f"[ ✓ ] A CHAVE '{key}' CRIADA com SUCESSO.", False)
    SendTerminalMessage(f"[ ✓ ] O(s) VALOR(ES) {values_list} INSERIDOS(S) em '{key}' com SUCESSO.", False)
    Save_db_dictio_file("phone_list")

    return SUCESS_VALUE
#
#   Insere um novo valor 'value' dentro da lista de uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'incluirTelefone'
def AppendDictValue(dictio, key, value):

    if(not IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível INSERIR o VALOR {value} na CHAVE '{key}' dentro do dicionário, pois a mesma NÃO EXISTIA.")
        return ERROR_VALUE
    
    if IsValueInDictKeyExists(dictio, key, value):
        SendTerminalWarning(f"[ x ] O VALOR {value} NÃO foi ADICIONADO em '{key}', pois JÁ EXISTIA.")
        return ERROR_VALUE        
    
    dictio[f"{key}"] += [value]

    SendTerminalMessage(f"[ ✓ ] O(s) VALOR(ES) {value} INSERIDOS(S) em '{key}' com SUCESSO.", False)
    Save_db_dictio_file("phone_list")

    return SUCESS_VALUE
#
#   Remove um valor 'value' de dentro da lista de uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'excluirTelefone'
def RemoveDictValue(dictio, key, value):
    
    if(not IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível REMOVER o VALOR {value} na CHAVE '{key}' dentro do dicionário, pois a mesma NÃO EXISTIA.")
        return ERROR_VALUE

    if not IsValueInDictKeyExists(dictio, key, value):
        SendTerminalWarning(f"[ x ] O VALOR {value} NÃO foi REMOVIDO em '{key}', pois NÃO EXISTIA.")
        return ERROR_VALUE  
    
    values_list = dictio[f"{key}"]
    values_list.remove(f'{value}')
    dictio[f"{key}"] = values_list
    
    if len(values_list) == 0:
        SendTerminalMessage(f"[ ✓ ] O VALOR {value} foi DELETADO de '{key}' com SUCESSO.", False)
        SendTerminalMessage(f"[ ! ] A CHAVE '{key}' será DELETADA do dicionário, pois NÃO HÁ VALORES associados.", False)
        RemoveDictKey(dictio, key)
    else:
        SendTerminalMessage(f"[ ✓ ] O VALOR {value} foi DELETADO de '{key}' com SUCESSO.", False)
        Save_db_dictio_file("phone_list")

    return SUCESS_VALUE
#
#   Remove uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'excluirNome'
def RemoveDictKey(dictio, key):

    if(not IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível REMOVER a CHAVE '{key}' de dentro do dicionário, pois a mesma NÃO EXISTIA.")
        return ERROR_VALUE
    
    dictio.pop(key)
    SendTerminalMessage(f"[ ✓ ] A CHAVE '{key}' foi DELETADO do dicionário com SUCESSO.", False)
    Save_db_dictio_file("phone_list")

    return SUCESS_VALUE
#
#   Retorna a lista de valores da 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'consultarTelefone'
def GetDictKeyValue(dictio, key):
    return dictio[f"{key}"]
#
#   Verifica se o nome que será inserido no dicionário é válido [a-z / A-Z]
def IsValidName(name):
    for letter in name:
        if not ((65 <= ord(letter) and ord(letter) <= 90) or (97 <= ord(letter) and ord(letter) <= 122)):
            return False
    return True
#
#   Verifica se uma lista de números telefônicos é válida            
def IsValidPhoneList(phone_list):
    for phone_number in phone_list:
        if not IsValidPhone(phone_number):
            return False
    return True
#
#   Verifica se um telefone é válido [0-9]        
def IsValidPhone(phone_number):
    for number in phone_number:
        if (not ((48 <= ord(number) and ord(number) <= 57))):
            return False
    return True
#
#   Verifica se há valores repetidos em uma lista  
def has_duplicates(lists):
    return len(set(lists)) < len(lists)

def Create_db_dictio_file(fname):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    try:            
        file = open(path, 'wt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\"")
        return ERROR_VALUE
    else:
        file.write(f"{fname} = ")
        file.close()
        SendTerminalMessage(f"[ ✓ ] \"{path}\" CRIADO com SUCESSO")

def Save_db_dictio_file(fname):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    try:            
        file = open(path, 'at', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível SALVAR \"{path}\"")
        return ERROR_VALUE
    else:
        global phone_dict
        key_list = phone_dict.keys()

        for key in key_list:
            file.write(f"{key} = {phone_dict[key]}\r")
        file.close()
        SendTerminalMessage(f"[ ✓ ] \"{path}\" SALVO com SUCESSO")

def Load_db_dictio_file(fname):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    try:            
        file = open(path, 'rt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\"")
        return ERROR_VALUE
    else:

        line = file.read().removeprefix(f"{fname} = ")
        line = line.strip("{}")
        print(line.split(",")[0])
        # global phone_dict

        # for line in file:
        #     dictio = line.split(",")

        #     for pair in dictio:
        #         elements = pair.split(":")
        #         phone_dict.update({f"{elements[0]}" : elements[1]})

        # print(phone_dict, type(phone_dict))
        file.close()
        # SendTerminalMessage(f"[ ✓ ] \"{path}\" CARREGADO com SUCESSO")

#
#   Função main()
def main():

    # fname = "phone_list"
    # path = f"{DIR_DEFAULT}/{fname}.dictio"

    # if not os.path.exists(path):
    #     Create_db_dictio_file(fname)
    # else:
    #     Load_db_dictio_file(fname)

    if not DEBUG_MODE:
        CreateTerminalMenu(MENU_INIT)
        TerminalDelay(APRESENTATION_TIME_MS)

    CreateTerminalMenu(MENU_MAIN)  
main()