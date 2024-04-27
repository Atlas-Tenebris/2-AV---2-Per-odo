from stocks import book_stock, cold_food_stocked, edit
from Company import info
from colorama import Fore, Style
from user import login, login_autenticacion, register
from time import sleep

while True:
    try:
        print('\nO que você busca?')
        choice = int(input('\n[1] Aprender um pouco sobre nós.'
                           '\n[2] Ver os produtos que vendemos.'
                           '\n[3] Fazer seu cadastro.'
                           '\n[4] Fazer Login.'
                           '\n[5] Editar um dos estoques.'
                           '\n[6] Finalizar o programa.'
                           '\nEscolha: '))
        if choice == 6:
            print('Obrigado por ter dado uma chance à MilkShakespeare. Você será sempre bem vindo aqui!')
            sleep(4)
            break
        if choice in range(1, 6):
            login_autenticacion.verification()

        if choice == 1:
            info.company_info()

        elif choice == 2:
            while True:
                try:
                    stock_choice = int(input('\nDigite qual dos nossos estoques deseja ver:'
                                             '\n[1]Livros.'
                                             '\n[2]Sobremesas geladas.'
                                             '\n[3] Voltar ao menu'
                                             '\nEscolha:  '))
                    if stock_choice == 1:
                        book_stock.see_books()
                        break
                    elif stock_choice == 2:
                        cold_food_stocked.food_stock()
                        break
                    elif stock_choice == 3:
                        break
                    else:
                        print(f'{Fore.LIGHTRED_EX}Escolha inválida!!{Style.RESET_ALL}\nTente novamente.\n')
                except ValueError:
                    print(f'{Fore.LIGHTRED_EX}!!!ERROR!!!{Style.RESET_ALL}\nO valor inserido é inválido. Digite apenas'
                          f' os números mostrados acima. Tente novamente.\n')
        elif choice == 3:
            login_autenticacion.employee_verification()
            login.logged = False
        elif choice == 4:
            if login.logged_like_employee is True:
                print('Você já está logado como funcionário. Não há porque logar como cliente.')
                continue
                if login.logged is True:
                    print('Você já está logado.')
                    continue
            if login.logged is False and register.employee_registered is True:
                print(login.user_login())
                continue
            else:
                login_autenticacion.employee_logged()
        elif choice == 5:
            if login.logged_like_employee is True:
                while True:
                    try:
                        choice = int(input('\nAntes de mudar algo, você deseja adicionar ou remover?'
                                           '\n[1] Adicionar.'
                                           '\n[2] Remover.'
                                           '\n[3] Voltar ao menu'
                                           '\n\nEscolha: '))
                        if choice == 1:
                            edit.increase()
                        elif choice == 2:
                            edit.decrease()
                        elif choice == 3:
                            break
                        else:
                            print(f'{Fore.LIGHTRED_EX}Opção inválida{Style.RESET_ALL}')
                    except ValueError:
                        print(f'{Fore.LIGHTRED_EX}!!!ERROR!!!{Style.RESET_ALL}'
                              f'\nO valor inserido é inválido. Tente novamente, por favor.')
                        continue
            else:
                print(f'\nVocê deve estar LOGADO como {Fore.LIGHTBLUE_EX}Funcionário{Style.RESET_ALL} para editar'
                      f' o estoque.\n')
        else:
            print(f'{Fore.RED}Opção inválida!!!!{Style.RESET_ALL}'
                  f'\nTente novamente.\n')
            continue
    except ValueError:
        print(f'{Fore.LIGHTRED_EX}!!!!ERROR!!!!'
              f'\nO valor inserido é inválido!{Style.RESET_ALL}\nTente novamente.')
