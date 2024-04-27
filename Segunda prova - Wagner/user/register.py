from colorama import Style, Fore
user_data = {'email': '', 'senha': '', 'nickname': '', 'telefone': ''}

symbols = ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
           ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~')


employee_registered = False
user_registered = False
def user_record():
    print('=' * 35)
    print('              CADASTRO')
    print('=' * 35)

    while True:
        global employee_registered
        global user_registered
        employee_registered, user_registered = False, False
        symbol_detected = False
        user = input('Digite aqui o seu nome de usuário: ').strip()
        for symbol in symbols:
            if user.isdigit() or symbol in user:
                symbol_detected = True
                break
        if symbol_detected or user.isdigit():
            print(f'{Fore.LIGHTRED_EX}               !!!ERROR!!! {Style.RESET_ALL}'
                  f'\nNão utilize símbolos ou apenas números.')
            continue
        else:
            user_data['nickname'] = user
            break

    while True:
        password = str(input('\nAgora, digite sua senha: ')).strip()
        if len(password) < 5:
            print(f'{Fore.LIGHTRED_EX}              !!!!ERROR!!!!{Style.RESET_ALL}'
                  f'\nSenha muito curta. Faça uma com, no mínimo, 5 caracteres.')
        else:
            user_data['senha'] = password
            break

    while True:
        email = str(input('\nDigite agora seu email: ')).strip()

        if '@gmail.com' in email or '@hotmail.com' in email:
            if '@gmail.com' in email and len(email) < 15:
                print(f'{Fore.LIGHTRED_EX}E-mail muito curto! Precisa ter, no mínimo 15 caracteres.{Style.RESET_ALL}')
                continue
            elif '@hotmail.com' in email and len(email) < 17:
                print(f'{Fore.LIGHTRED_EX}E-mail muito curto! Precisa ter, no mínimo 17 caracteres.{Style.RESET_ALL}')
                continue
            else:
                user_data['email'] = email
                user_registered = True
                break
        elif '@milkshakespeare.com' in email:
            if '@milkshakespeare.com' in email and len(email) < 26:
                print(f'{Fore.LIGHTRED_EX}E-mail muito curto!!!!{Style.RESET_ALL}\n'
                      f'E-mails de funcionários precisam ter, no mínimo, 26 dígitos. Tente novamente.')
                continue
            else:
                user_data['email'] = email
                employee_registered = True
                break
        else:
            print(f'{Fore.LIGHTRED_EX}! !!!ERROR!!!!{Style.RESET_ALL}'
                  f'\nO e-mail informado é inválido. Só serão aceitos e-mails com "@gmail.com" ou "@hotmail.com" ou'
                  f' e-mails de funcionários.'
                  f'\nTente novamente.')
    while True:
        try:
            cellphone_number = int(input('\nDigite agora seu número de telefone (Sem DDD e sem o 9 na frente): '))
            if len(str(cellphone_number)) > 8:
                print(f'{Fore.LIGHTRED_EX}!!!!ERROR!!!!!{Style.RESET_ALL}\n'
                      f'O número de telefone fornecido excede o limite de 8 dígitos. Lembre-se de '
                      f'não colocar o DDD e nem o 9 na frente.\n')
            elif len(str(cellphone_number)) < 8:
                print(f'{Fore.LIGHTRED_EX}!!!!ERROR!!!!!{Style.RESET_ALL}\n'
                      f'O número de telefone fornecido não atende a quantidade mínima de 8 dígitos.\n')
            else:
                user_data['telefone'] = str(cellphone_number)
                break
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}!!!!ERROR!!!!!{Style.RESET_ALL}'
                  f'\nDigite apenas números, sem hífen ou qualquer outra coisa. Tente novamente.')
