from user import register, login
from colorama import Fore, Style


def verification():
    while True:
        if register.employee_registered is False and register.user_registered is False:
            print(f'\nParece que você ainda não se cadastrou. Você precisa se cadastrar como {Fore.LIGHTYELLOW_EX}'
                  f'cliente{Style.RESET_ALL} ou como {Fore.LIGHTBLUE_EX}funcionário{Style.RESET_ALL}.\n')
            register.user_record()
            print('\nVocê já está cadastrado, mas ainda não logou. Para ver qualquer informação sobre a empresa, '
                  'primeiramente você deve estar logado.\n')
            login.user_login()
        else:
            break


def employee_verification():
    if register.user_registered is True and login.logged is True and login.logged_like_employee is False:
        print('\nVocê já está logado como cliente, talvez queira logar como funcionário ou só mudar o cadastro.'
              '\nLembre-se: Se quiser logar como funcionário, utilize o e-mail de funcionário para cadastrar-se'
              f' e depois faça login com suas informações de {Fore.LIGHTBLUE_EX}funcionário.{Style.RESET_ALL}\n')
        register.user_record()
    elif register.employee_registered is True and login.logged_like_employee is False:
        print(f'\nVocê já está cadastrado como funcionário, porém ainda não {Fore.LIGHTBLUE_EX}logou{Style.RESET_ALL}.')

    elif register.employee_registered is True and login.logged_like_employee is False:
        print(f'\nVocê já está cadastrado como funcionário, {register.user_data['nickname']}, '
              f'não há porque se cadastrar novamente.'
              f'\nSe estiver tendo algum problema, talvez tenha se esquecido'
              f' de {Fore.LIGHTBLUE_EX}logar{Style.RESET_ALL}.\n')


def employee_logged():
    if register.employee_registered is True and login.logged_like_employee is False:
        login.user_login()
    elif register.user_registered is True and login.logged is False:
        login.user_login()
    elif login.logged is True or login.logged_like_employee is True:
        print('Você já está logado.\n')
