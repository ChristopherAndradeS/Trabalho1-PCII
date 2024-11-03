#  _____         _           _ _             __            ______  _____   _____ _____ 
# |_   _|       | |         | | |           /  |           | ___ \/  __ \ |_   _|_   _|
#   | |_ __ __ _| |__   __ _| | |__   ___   `| |   ______  | |_/ /| /  \/   | |   | |  
#   | | '__/ _` | '_ \ / _` | | '_ \ / _ \   | |  |______| |  __/ | |       | |   | |  
#   | | | | (_| | |_) | (_| | | | | | (_) | _| |_          | |    | \__/\  _| |_ _| |_ 
#   \_/_|  \__,_|_.__/ \__,_|_|_| |_|\___/  \___/          \_|     \____/  \___/ \___/ 
#
#   MACROS - INTERFACE DE MENUS
#
WAITING_TIME_MS                 = (3000)                            # Tempo (ms) de espera
MAX_TEXT_LEN                    = (256)                             # Tamanho máximo do terminal input
COMMAND_PREFIX                  = '/'                               # Prefixo que identifica os comandos digitados
COMMAND_MENU                    = 'menu'                            # Comando voltar p/ Menu Principal 
COMMAND_QUIT                    = 'quit'                            # Comando encerrar programa
COMMAND_RELOAD                  = 'reload'                          # Comando reiniciar programa
TERMINAL_INPUT_MSG_INT          = '\n[ » ] Selecione uma opção: '   # Menssagem de solicitação de input para números
TERMINAL_INPUT_MSG_STRING       = '\n[ » ] Insira um texto: '       # Menssagem de solicitação de input para texto
TERMINAL_WIDTH                  = (120)                             # Largura do terminal em "_"
DIR_DEFAULT                     = 'scriptfiles'                     # Nome da pasta de arquivos de código
FILE_NAME                       = "phones"                          # Nome do arquivo .dictio que armazena o dicionário
FILE_ENCODING                   = 'utf-8'                           # Unicode dos arquivos do menu
#
#   CONSTS
#
TYPE_INT                        = (0x10)                            # flag do tipo 'int'
TYPE_STRING                     = (0x20)                            # flag do tipo 'texto'
TYPE_CONFIRM                    = (0x30)                            # flag do tipo 'confirmar'
INPUT_CMD                       = (0x80)                            # flag do tipo 'comando'
INVALID_INPUT_INT               = (-1)                              # flag para 'input númerico inválido'
INVALID_INPUT_STRING            = 'null'                            # flag para 'input texto inválido' 
ERROR_VALUE                     = 0xEE                              # Valor de retorno p/ 'erro'
SUCESS_VALUE                    = 0xAA                              # Valor de retorno p/ 'sucesso'       
REMOVE_KEY_VALUE                = 0xDD                              # Valor que identifica remoção de chave no dictio     
#
#   MENUS ID'S
#
#   Apresentação e menu principal
#
MENU_INIT                       = (1)                               # Menu de apresentação
MENU_MAIN                       = (2)                               # Menu principal
#
#   incluir Novo Nome
#
MENU_INSERT_NEW_KEY_NAME        = (3)                               # Menu Inserir Novo Chave   - Definir Nome
MENU_INSERT_NEW_KEY_PHONE       = (11)                              # Menu Inserir Novo Chave   - Definir Telefone
#
#   incluir Telefone
#
MENU_INSERT_NEW_VALUE_NAME      = (4)                               # Menu Inserir Novo Valor   - Definir Nome
MENU_INSERT_NEW_VALUE_PHONE     = (12)                              # Menu Inserir Novo Valor   - Definir Telefone
#
#   excluir Telefone
#
MENU_REMOVE_VALUE_NAME          = (5)                               # Menu Remover Valor        - Definir Nome
MENU_REMOVE_VALUE_PHONE         = (13)                              # Menu Remover Valor        - Definir Telefone
#
#   excluir Nome
#
MENU_REMOVE_NAME                = (6)                               # Menu Remover Valor        - Definir Nome
#
#   consultar Telefone / consultar Dicionário
#
MENU_GET_PHONE                  = (7)                               # Menu Consultar Telefone   - Definir Nome
MENU_PRINT_DICTIO               = (8)                               # Menu Vizualizar Dictio
#
#   BIBLIOTECAS - INTERFACE DE MENUS
#                                                         
import os
import platform
import time
import sys 
#
#   VARIÁVEIS GLOBAL - INTERFACE DE MENUS
#
input_name  = ''        # Variável global - armazena o input do Nome digitado
#
#   FUNÇÕES - INTERFACE DE MENUS
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
    #   /reload
    if cmd == COMMAND_RELOAD:
        TerminalDelay(WAITING_TIME_MS)
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
    print(GetTerminalBounds() + "\n" + "Alerta".center(TERMINAL_WIDTH) + '\n\n' + msg + '\n' + GetTerminalBounds())
    TerminalDelay(WAITING_TIME_MS)
    SendTerminalCommand(COMMAND_QUIT)
#
#   'SendTerminalMessage(msg)' envia uma mensagem 'msg' para o terminal'
def SendTerminalMessage(msg, flag = True):
    print('\n' + msg)
    if flag:
        print(GetTerminalBounds())
        TerminalDelay(WAITING_TIME_MS * 0.3)
#
#   'GetTerminalInput()' trata as entradas digitadas: tipo arquivo, número e texto'
def GetTerminalInput(input_msg, input_type, min_range = -1, max_range = -1, len_txt = MAX_TEXT_LEN):
    default_msg = input_msg
    if input_type == TYPE_INT:
        while True:
            input_txt = input(input_msg + default_msg if default_msg != input_msg else input_msg)
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                else: 
                    input_msg = f"\n[ x ] O comando digitado NÃO EXISTE. Tente novamente\n" + GetTerminalBounds()
                    continue
            if not input_txt.isnumeric():
                input_msg = f"\n[ x ] Entrada INVÁLIDA. Digite um NÚMERO INTEIRO entre {min_range} e {max_range}.\n" + GetTerminalBounds()
                continue
            input_value = int(input_txt)
            if min_range != max_range:
                if (input_value < min_range or input_value > max_range):    
                    input_msg = f"\n[ x ] Entrada INVÁLIDA. Digite UM VALOR entre {min_range} e {max_range}.\n"
                    continue
            if min_range == max_range:
                if (input_value != min_range) and min_range != -1:    
                    input_msg = f"\n[ x ] Entrada INVÁLIDA. Só há UMA OPÇÃO {min_range}.\n" + GetTerminalBounds()
                    continue
            return input_value
    if input_type == TYPE_STRING:
        while True:
            input_txt = input(input_msg + default_msg if default_msg != input_msg else input_msg)
            if '/' in input_txt: 
                if SendTerminalCommand(input_txt.removeprefix(COMMAND_PREFIX)):
                    return INPUT_CMD
                else: 
                    input_msg = f"\n[ x ] O comando digitado NÃO EXISTE. Tente novamente\n" + GetTerminalBounds()
                    continue
            if(len(input_txt) > len_txt):
                input_msg = f"\n[ x ] Entrada INVÁLIDA. Escreva UM TEXTO com no MÁXIMO {MAX_TEXT_LEN} caracteres:\n" + GetTerminalBounds()
                continue
            return input_txt
#
#   'SendTermialInput(msg, typeinput, menuid, min, max)'
#
#   Envia uma mensagem e um campo para inserir uma entrada (input) na interface. A qual é analisada
#   posteriormente em 'GetTerminalInput(input_msg, typevar, min_range, max_range, len_txt)'
#
def SendTermialInput(msg, input_type, menuid = 0, min = -1, max = -1, len_txt = MAX_TEXT_LEN):
    if input_type == TYPE_INT:
        input_value = INVALID_INPUT_INT
        while True:
            input_value = GetTerminalInput(msg, input_type, min_range = min, max_range = max)
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
    if input_type == TYPE_CONFIRM:
        input_value = INVALID_INPUT_INT
        while True:
            input_value = input(msg + '\n' + TERMINAL_INPUT_MSG_INT)
            if '/' in input_value: 
                if SendTerminalCommand(input_value.removeprefix(COMMAND_PREFIX)):
                    return 1
            if(input_value == '1' or input_value == '2'):
                break
            else:
                msg ="\n" + GetTerminalBounds() + f"\n[ x ] Digite APENAS ({min}) ou ({max})\n"
        return int(input_value)
#
#   'CreateTerminalMenu(menuid)' cria o menu de acordo com os arquivos .txt dentros da pasta 'menus'
def CreateTerminalMenu(menuid):
    ClearTerminal()
    txt = ''
    try:            
        file = open(f"menus/menu-{menuid}.txt", 'rt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"menus/menu-{menuid}.txt\"")
        return ERROR_VALUE
    else:
        global input_name
        for line in file:
            line = line.replace('\n', "")
            line = line.replace('<br>', "\n")
            line = line.replace('<t>', "\t")
            line = line.replace('<name>', f'{input_name}')
            if '<center>' in line:
                line = line.replace('<center>', "")
                line = line.center(TERMINAL_WIDTH)
            if '<left>' in line:
                line = line.replace('<left>', "")
                line = line.ljust(TERMINAL_WIDTH)
            if '<right>' in line:
                line = line.replace('<right>', "")
                line = line.rjust(TERMINAL_WIDTH)
            if '<bounds>' in line:
                line = GetTerminalBounds(TERMINAL_WIDTH)
            if line == "<request-input-str>" or line == "<request-input-int>":
                continue
            txt += line
    print(txt, end = '')
    file.close()
    if line == "<request-input-str>":
        SendTermialInput(TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
    elif line == "<request-input-int>":
        SendTermialInput(TERMINAL_INPUT_MSG_INT, TYPE_INT, menuid, 1, 6)
    elif line == "<bounds>":
        print(GetTerminalBounds())
#
#   'SendMenuResponse()' decide quais serão os próximos passos do programa de acordo com a entrada digitada pelo usuário
def SendMenuResponse(menuid, input_value):
    global input_name, phone_dict

    if(menuid == MENU_MAIN): 
        if not (input_value + 2 == MENU_INSERT_NEW_KEY_NAME or input_value + 2 == MENU_INSERT_NEW_VALUE_NAME):
            if IsEmptyDict(phone_dict):
                SendTermialInput(GetTerminalBounds() + "\n[ ! ] Dicionário VAZIO, tente incluir uma NOVA CHAVE primeiro\n" + TERMINAL_INPUT_MSG_INT, TYPE_INT, menuid, 1, 6)

        if(input_value + 2 == MENU_PRINT_DICTIO):
            CreateTerminalMenu(MENU_PRINT_DICTIO)
            
            str_print = '\n\nphone_dict = \n{\n'

            for key in phone_dict.keys():
                str_print += " " * 3 + f"'{key}'" + " " * (10 - len(key)) + f": {phone_dict[key]}\n" 

            str_print += '}\n'

            print("\n» Lista de usuários no Dicionário:", str_print + GetTerminalBounds())
            input("[ » ] Aperte QUALQUER TECLA para voltar ao MENU: ")
            CreateTerminalMenu(MENU_MAIN)
        else:
            CreateTerminalMenu(input_value + 2)

    if(menuid == MENU_INSERT_NEW_KEY_NAME):
        name = input_value

        if not IsValidInputName(name, False, menuid): return ERROR_VALUE
         
        txt = f"\n[ • ] Deseja CRIAR uma CHAVE de nome » {name} « ?\n\n\t1. Sim, quero CRIAR com esse NOME\n\t"
        txt += "2. Não, quero VOLTAR e digitar OUTRO nome\n" + GetTerminalBounds()
            
        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            input_name = name
            CreateTerminalMenu(MENU_INSERT_NEW_KEY_PHONE)
        else:
            CreateTerminalMenu(MENU_INSERT_NEW_KEY_NAME)

    if(menuid == MENU_INSERT_NEW_KEY_PHONE):
        phone_list = list()

        input_list = input_value.split(" ")

        for idx in range(len(input_list)):
            if(IsValidPhone(input_list[idx]) and input_list[idx] != ''):
                phone_list.append(input_list[idx])

        if not IsValidInputPhoneList(phone_list, menuid): return ERROR_VALUE     
        
        txt = '\n[ • ] Lista de TELEFONES digitado:\n\n'
        for idx, phone in enumerate(phone_list):
            txt += f'\t» {idx + 1}. {phone}\n'

        txt += f"\n[ • ] Deseja INSERIR a lista de TELEFONE(S) dentro da CHAVE » {input_name} « ?"
        txt += "\n\n\t1. Sim, quero INSERIR esse(s) TELEFONE(S) na chave\n\t2. Não, quero VOLTAR e digitar OUTRA lista\n" + GetTerminalBounds()
        
        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)
        
        if(not (input_value - 1)):
            CreateDictKey(phone_dict, input_name, phone_list)
            SendTerminalCommand(COMMAND_MENU)
        else:
            CreateTerminalMenu(MENU_INSERT_NEW_KEY_PHONE)
                
    if(menuid == MENU_INSERT_NEW_VALUE_NAME):
        name = input_value

        if(not IsValidName(name)):
            SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return False
        
        if(not IsDictKeyExists(phone_dict, name)):
            txt = f"\n[ ! ] O NOME '{name}' NÃO EXISTE no dicionário.\n" + f"\n» Deseja criar UM NOVO NOME '{name}' ?\n\n"
            txt += "\t1. Sim, quero CRIAR um NOME NOVO\n\t2. Não, quero digitar OUTRO NOME\n" + GetTerminalBounds()

            input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)
            
            if(not (input_value - 1)):
                input_name = name
                CreateTerminalMenu(MENU_INSERT_NEW_KEY_PHONE)
            else:
                CreateTerminalMenu(MENU_INSERT_NEW_VALUE_NAME)

        input_name = name
        CreateTerminalMenu(MENU_INSERT_NEW_VALUE_PHONE)

    if(menuid == MENU_INSERT_NEW_VALUE_PHONE):
        phone = input_value

        if not IsValidInputPhoneList([phone], menuid): return ERROR_VALUE

        if(IsValueInDictKeyExists(phone_dict, input_name, phone)):
            SendTermialInput('\n[ x ] EXISTE(M) TELEFONE(S) na LISTA digitada que JÁ EXISTE na LISTA da chave:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return False 
        
        AppendDictValue(phone_dict, input_name, phone)

        txt = f"\n[ • ] Deseja ADICIONAR outro telefone dentro da lista telefônica de '{input_name}' ?\n\n"
        txt += "\t1. Sim, quero ADICIONAR mais telefones\n\t2. Não, quero VOLTAR para o menu"

        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            CreateTerminalMenu(MENU_INSERT_NEW_VALUE_PHONE)
        else:
            SendTerminalCommand(COMMAND_MENU)  

    if(menuid == MENU_REMOVE_VALUE_NAME):
        name = input_value

        if not IsValidInputName(name, True, menuid): return ERROR_VALUE
                
        input_name = name
        CreateTerminalMenu(MENU_REMOVE_VALUE_PHONE)

    if(menuid == MENU_REMOVE_VALUE_PHONE):        
        phone = input_value

        if not IsValidInputPhoneList([phone], menuid): return ERROR_VALUE
        
        if(not IsValueInDictKeyExists(phone_dict, input_name, phone)):
            SendTermialInput('\n[ x ] EXISTE(M) TELEFONE(S) na LISTA digitada que NÃO EXISTE na LISTA da chave:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return False  
        
        txt = f"\n[ • ] Tem certeza que deseja REMOVER o telefone [{phone}] de '{input_name}' ? O telefone será perdido permanentemente.\n\n"
        txt += "\t1. Sim, quero REMOVER o TELEFONE\n\t2. Não, quero digitar OUTRO TELEFONE"

        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            RemoveDictValue(phone_dict, input_name, phone)
        else:
            return CreateTerminalMenu(MENU_REMOVE_VALUE_PHONE)  

        txt = f"\n[ • ] Deseja REMOVER outro TELEFONE de dentro da lista telefônica de '{input_name}' ?\n\n"
        txt += "\t1. Sim, quero REMOVER outro TELEFONE\n\t2. Não, quero VOLTAR para o MENU PRINCIPAL"
        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            if IsEmptyDict(phone_dict):
                SendTerminalMessage("[ ! ] Dicionário VAZIO, voltando para o MENU PRINCIPAL")
                TerminalDelay(WAITING_TIME_MS * 0.5)
                SendTerminalCommand(COMMAND_MENU)

            CreateTerminalMenu(MENU_REMOVE_VALUE_PHONE)
        else:
            SendTerminalCommand(COMMAND_MENU)  
  
    if(menuid == MENU_REMOVE_NAME):       
        name = input_value

        if not IsValidInputName(name, True, menuid): return ERROR_VALUE
        
        input_name = name

        txt = f"\n[ • ] Tem certeza que deseja REMOVER o nome '{input_name}' da lista? Os dados serão perdidos permanentemente.\n\n"
        txt += "\t1. Sim, quero REMOVER a CHAVE\n\t2. Não, quero digitar OUTRO NOME"

        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            RemoveDictKey(phone_dict, name)
        else:
            return CreateTerminalMenu(MENU_REMOVE_NAME)  

        txt = f"\n[ • ] Deseja REMOVER OUTRO NOME do dicionário ?\n\n"
        txt += "\t1. Sim, quero REMOVER OUTRO NOME\n\t2. Não, quero VOLTAR para o MENU PRINCIPAL"
        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            if IsEmptyDict(phone_dict):
                SendTerminalMessage("[ ! ] Dicionário VAZIO, voltando para o MENU PRINCIPAL")
                TerminalDelay(WAITING_TIME_MS * 0.5)
                SendTerminalCommand(COMMAND_MENU)

            CreateTerminalMenu(MENU_REMOVE_NAME)
        else:
            SendTerminalCommand(COMMAND_MENU)  

    if(menuid == MENU_GET_PHONE):       
        name = input_value
        
        if not IsValidInputName(name, True, menuid): return ERROR_VALUE

        phones = GetDictKeyValue(phone_dict, name)

        print("\n" + GetTerminalBounds() + f"\n• Lista de telefone de '{name}':\n")
        for idx in range(len(phones)):
            print(f"\t{idx + 1:0>2d}. {phones[idx]}")
        
        txt = GetTerminalBounds() + f"\n[ • ] Deseja CONSULTAR outro NOME dentro da lista telefônica ?\n\n"
        txt += "\t1. Sim, quero CONSULTAR mais NOMES\n\t2. Não, quero VOLTAR para o MENU PRINCIPAL"

        input_value = SendTermialInput(msg = txt, input_type = TYPE_CONFIRM, min = 1, max = 2)

        if(not (input_value - 1)):
            CreateTerminalMenu(MENU_GET_PHONE)
        else:
            SendTerminalCommand(COMMAND_MENU) 

    return 1
#
#   'IsValidInputName()' verifica o input do nome
def IsValidInputName(name, must_exists, menuid):
    global phone_dict
    if not IsValidName(name):
        SendTermialInput('\n[ x ] O NOME digitado é INVÁLIDO, use APENAS LETRAS [A-Z / a-z]: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
        return False
    if not must_exists:
        if IsDictKeyExists(phone_dict, name):
            SendTermialInput('\n[ x ] O NOME digitado JÁ EXISTE, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return False 
    else:
        if not IsDictKeyExists(phone_dict, name):
            SendTermialInput('\n[ x ] O NOME digitado NÃO EXISTE, tente outro:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
            return False     
    return True
#
#   'IsValidInputName()' verifica do(s) telefone(s)
def IsValidInputPhoneList(phone_list, menuid):
    if(len(str(phone_list)) == 0): 
        return False

    global input_name, phone_dict

    if len(phone_list) == 0 or [''] == phone_list:
        SendTermialInput('\n[ x ] A LISTA digitada está VAZIA: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
        return False
    if has_duplicates(phone_list):
        SendTermialInput('\n[ x ] A LISTA possui TELEFONES REPETIDOS: \n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
        return False
    if not IsValidPhoneList(phone_list):
        SendTermialInput('\n[ x ] A LISTA de TELEFONES digitada é INVÁLIDA, use APENAS NÚMEROS [0-9]:\n' + GetTerminalBounds() + TERMINAL_INPUT_MSG_STRING, TYPE_STRING, menuid, len_txt = 64)
        return False    
    return True
#
#   VARIÁVEL GLOBAL - DICTIO
#
phone_dict      = dict()    # Dicionário Globla de telefones
#
#   FUNÇÕES - DICTIO
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
    return value in dictio[f"{key}"]
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
    TerminalDelay(WAITING_TIME_MS * 0.5)
    SendTerminalMessage(f"[ ✓ ] O(s) VALOR(ES) {values_list} INSERIDOS(S) em '{key}' com SUCESSO.", False)
    TerminalDelay(WAITING_TIME_MS * 0.5)
    Create_db_key(FILE_NAME, key, dictio[f"{key}"])

    return SUCESS_VALUE
#
#   Insere um novo valor 'value' dentro da lista de uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'incluirTelefone'
def AppendDictValue(dictio, key, value):

    if(not IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível INSERIR o VALOR [ '{value}' ] na CHAVE '{key}' dentro do dicionário, pois a mesma NÃO EXISTIA.")
        return ERROR_VALUE
    
    if IsValueInDictKeyExists(dictio, key, value):
        SendTerminalWarning(f"[ x ] O VALOR [ '{value}' ] NÃO foi ADICIONADO em '{key}', pois JÁ EXISTIA.")
        return ERROR_VALUE        
    
    temp_list = list()
    
    for phone in dictio[f"{key}"]:
        temp_list.append(phone)

    temp_list.append(value)
    dictio[f"{key}"] = temp_list

    SendTerminalMessage(f"[ ✓ ] O(s) VALOR(ES) [ '{value}' ] INSERIDOS(S) em '{key}' com SUCESSO.", False)
    TerminalDelay(WAITING_TIME_MS * 0.5)
    Save_db_key(FILE_NAME, key, dictio[f"{key}"])

    return SUCESS_VALUE
#
#   Remove um valor 'value' de dentro da lista de uma chave 'key' do dicionário 'dictio'
#  
#   Equivalente a função 'excluirTelefone'
def RemoveDictValue(dictio, key, value):
    
    if(not IsDictKeyExists(dictio, key)):
        SendTerminalWarning(f"[ x ] NÃO foi possível REMOVER o VALOR [ '{value}' ] na CHAVE '{key}' dentro do dicionário, pois a mesma NÃO EXISTIA.")
        return ERROR_VALUE

    if not IsValueInDictKeyExists(dictio, key, value):
        SendTerminalWarning(f"[ x ] O VALOR [ '{value}' ] NÃO foi REMOVIDO em '{key}', pois NÃO EXISTIA.")
        return ERROR_VALUE  
    
    values_list = dictio[f"{key}"]
    values_list.remove(f'{value}')
    dictio[f"{key}"] = values_list
    
    if len(values_list) == 0:
        SendTerminalMessage(f"[ ✓ ] O VALOR [ '{value}' ] foi DELETADO de '{key}' com SUCESSO.", False)
        TerminalDelay(WAITING_TIME_MS * 0.5)
        SendTerminalMessage(f"[ ! ] A CHAVE '{key}' será DELETADA do dicionário, pois NÃO HÁ VALORES associados.", False)
        TerminalDelay(WAITING_TIME_MS * 0.5)
        RemoveDictKey(dictio, key)
    else:
        SendTerminalMessage(f"[ ✓ ] O VALOR [ '{value}' ] foi DELETADO de '{key}' com SUCESSO.", False)
        TerminalDelay(WAITING_TIME_MS * 0.5)
        Save_db_key(FILE_NAME, key, dictio[f"{key}"])

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
    TerminalDelay(WAITING_TIME_MS * 0.5)
    Remove_db_key(FILE_NAME, key)

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
    if name == '': return False
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
    if phone_number == REMOVE_KEY_VALUE:
        return False
    for number in phone_number:
        if (not ((48 <= ord(number) and ord(number) <= 57))):
            return False
    return True
#
#   Verifica se há valores repetidos em uma lista  
def has_duplicates(lists):
    return len(set(lists)) < len(lists)
#
def IsEmptyDict(dictio):
    return (len(dictio.keys()) == 0)

#   Cria banco de dados do dicionário, arquivo 'fname'.dictio
def Create_db_dictio_file(fname):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    try:            
        file = open(path, 'wt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\"")
        return ERROR_VALUE
    else:
        file.write("EOF")
        file.close()
        SendTerminalMessage(f"[ ✓ ] Arquivo \"{path}\" CRIADO com SUCESSO")
#
#   Cria uma chave 'key' dentro do banco de dados  
def Create_db_key(fname, key, value):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    file_str = Get_db_file_str(fname).removesuffix("EOF")
    file_str = file_str.removesuffix("\n")

    try:            
        file = open(path, 'wt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\" para SALVAR")
        return ERROR_VALUE
    else:
        if key in file_str:
            return SendTerminalWarning(f"[ x ] A CHAVE {key} NÃO foi CRIADA em \"{path}\", pois JÁ EXISTIA")

        new_str = f"{file_str}\n" if file_str != '' else ""
        new_str += f"{key} = {value}\nEOF"

        file.write(new_str)
        file.close()

        SendTerminalMessage(f"[ ✓ ] Chave {key} CRIADA dentro de \"{path}\" com SUCESSO")
#
#   Salva uma chave 'key' com valor 'value' no banco de dados  
def Save_db_key(fname, key, value):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    file_str = Get_db_file_str(fname).removesuffix("EOF")
    file_str = file_str.removesuffix("\n")

    try:            
        file = open(path, 'wt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\" para SALVAR")
        return ERROR_VALUE
    else:
        
        if key not in file_str:
            action = "REMOVIDA de" if value == REMOVE_KEY_VALUE else "SALVA em"
            return SendTerminalWarning(f"[ x ] A CHAVE {key} NÃO foi {action} \"{path}\", pois NÃO EXISTIA")

        file_lines_list = file_str.split("\n")

        for line in file_lines_list:
            if line == 'EOF': continue
            
            elements_list = line.split(" = ")
            
            f_key = elements_list[0]
            f_value = elements_list[1]

            if(f_key == key):
                if(value == REMOVE_KEY_VALUE): continue
                file.write(f"{key} = {value}\n")
            else:
                 file.write(f"{f_key} = {f_value}\n")

        file.write("EOF")
        file.close()

        SendTerminalMessage(f"[ ✓ ] Chave {key} SALVA dentro de \"{path}\" com SUCESSO")
#
#   Remove uma chave 'key' do banco de dados  
def Remove_db_key(fname, key):
    return Save_db_key(fname, key, REMOVE_KEY_VALUE)
#
#   Carrega os dados do banco para dentro de um dicionário 'dictio'
def Load_db_dictio_file(fname, dictio):

    path = f"{DIR_DEFAULT}/{fname}.dictio"

    try:            
        file = open(path, 'rt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\"")
        return ERROR_VALUE
    else:
        for line in file:
            if(line == 'EOF'): continue

            line = line.strip("\n")

            elements_list = str(line).split(" = ")
            file_key = elements_list[0]

            file_value = elements_list[1].strip("[']")
            file_value = file_value.split("', '")

            dictio.update({file_key: file_value})

        file.close()
        SendTerminalMessage(f"[ ✓ ] Arquivo \"{path}\" CARREGADO com SUCESSO")
#
#   Retona uma string dos textos do arquivo 'fname'
def Get_db_file_str(fname):
        
    path = f"{DIR_DEFAULT}/{fname}.dictio"

    try:            
        file = open(path, 'rt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\"")
        return ERROR_VALUE
    else:
        str_file = ''
        for line in file:
            str_file += line
        
        file.close()

        return str_file
#
#   Verifica se a chave 'key' existe dentro de 'fname'
def IsKeyExistInFile(fname, key):
    path = f"{DIR_DEFAULT}/{fname}.dictio"
    try:            
        file = open(path, 'rt', encoding = FILE_ENCODING)
    except IOError: 
        SendTerminalWarning(f"[ x ] NÃO foi possível CARREGAR \"{path}\"")
        return ERROR_VALUE
    else:
        return key in file.read() 
#
#   Função main()
def main():
    global phone_dict

    path = f"{DIR_DEFAULT}/{FILE_NAME}.dictio"
    
    CreateTerminalMenu(MENU_INIT)
    
    if not os.path.exists(path): Create_db_dictio_file(FILE_NAME)
    else:                        Load_db_dictio_file(FILE_NAME, phone_dict)

    input("Aperte ENTER para iniciar o programa: ")

    CreateTerminalMenu(MENU_MAIN)  
main()