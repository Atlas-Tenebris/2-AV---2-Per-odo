from colorama import Fore, Style
from user import register

logged = False
logged_like_employee = False


def user_login():
    print(f'{'=' * 35}')
    print('               LOGIN')
    print('='*35)
    error_amount = 0
    while True:
        if error_amount == 3:
            print('\nParece que você está tendo problemas para fazer Login. Faça o cadastro novamente, por favor.\n')
            register.user_record()
            user_login()
            break
        first_step = str(input('\nDigite seu e-mail ou Nickname: ')).strip()
        if first_step == register.user_data['email'] or first_step == register.user_data['nickname']:
            while True:
                global logged_like_employee
                global logged
                password = str(input('\nDigite agora sua senha: ')).strip()
                if password == register.user_data['senha'] and register.employee_registered is True:
                    print(f'Seja bem vindo,{Fore.LIGHTBLUE_EX}funcionário{Style.RESET_ALL}'
                          f' {register.user_data['nickname'].title()}!')
                    logged_like_employee = True
                    break
                elif password == register.user_data['senha'] and register.employee_registered is False:
                    print(f'\nSeja bem vindo, {register.user_data['nickname'].title()}!\n')
                    logged = True
                    break
                else:
                    print(f'{Fore.LIGHTRED_EX}Senha não reconhecida!{Style.RESET_ALL}\nTente novamente.')
        else:
            print(f'{Fore.LIGHTRED_EX}Nome de usuário ou e-mail não reconhecido.{Style.RESET_ALL}'
                  f'\n Tente novamente.\n')
            error_amount += 1
        break
