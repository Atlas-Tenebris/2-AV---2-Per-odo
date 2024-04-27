from stocks import all_book_stocked
from colorama import Fore, Style
from stocks import show_all_items_stocked


def see_books():
    while True:
        try:
            choice = int(input("\nEm qual gênero de livros está interessado?\n"
                               "\n[1] Livros de história                  [2] Livros de fantasia"
                               "\n[3] Livros de terror                    [4] Livros de romance"
                               "\n[5] Mangás                              [6] Comics (HQ's)"
                               "\n[7] Os 15 melhores livros.              [8] Todos os livros por gênero."
                               "\n[9] Voltar.\n"
                               "\nEscolha:  "))
            if choice == 1:
                show_all_items_stocked.show_history_books()
                print('\nAgora que você já viu quais são os livros de História que a MilkShakespeare possui,'
                      ' faça sua escolha:')
            
            elif choice == 2:
                show_all_items_stocked.show_fantasy_books()
                print('\nAgora que você já viu quais são os livros de Fantasia que a MilkShakespeare possui,'
                      ' faça sua escolha:')
            elif choice == 3:
                show_all_items_stocked.show_horror_books()
                print('\nAgora que você já viu quais são os livros de Terror que a MilkShakespeare possui,'
                      ' faça sua escolha:')
            elif choice == 4:
                show_all_items_stocked.show_romance_books()
                print('\nAgora que você já viu quais são os livros de Romance que a MilkShakespeare possui,'
                      ' faça sua escolha:')
            elif choice == 5:
                show_all_items_stocked.show_mangas()
                print('\nAgora que você já viu quais são os Mangás que a MilkShakespeare possui,'
                      ' faça sua escolha:')
            elif choice == 6:
                show_all_items_stocked.show_comics()
                print('\nAgora que você já viu quais são As histórias em quadrinhos que a MilkShakespeare possui,'
                      ' faça sua escolha:')
            elif choice == 7:
                print('\nEstes são os 15 melhores livros da MilkShakespeare, de acordo com o número de vendas.\n')
                for i in range(0, len(all_book_stocked.best_books)):
                    print(f'{'='*58}')
                    print(f'{i + 1}° LUGAR: '
                          f'{Fore.LIGHTYELLOW_EX}{all_book_stocked.best_books[i][0]}{Style.RESET_ALL}\n'
                          f'De: {Fore.LIGHTBLUE_EX}{all_book_stocked.best_books[i][1]}{Style.RESET_ALL}')
                    i += 1
                print('='*58)
            elif choice == 8:
                show_all_items_stocked.show_history_books()
                show_all_items_stocked.show_fantasy_books()
                show_all_items_stocked.show_horror_books()
                show_all_items_stocked.show_romance_books()
                show_all_items_stocked.show_mangas()
                show_all_items_stocked.show_comics()
            elif choice == 9:
                break
            else:
                print(f'\n{Fore.LIGHTRED_EX}         !!!ERRO!!!\nA ALTERNATIVA ESCOLHIDA NÃO EXISTE.{Style.RESET_ALL}\n'
                      f'\nTente novamente.\n')
                continue

            while True:
                try:
                    choice2 = int(input('\n[1] Ver outra categoria de livro.'
                                        '\n[2] Voltar ao Menu.'
                                        '\nEscolha: '))
                    if choice2 == 1:
                        see_books()
                    elif choice2 == 2:
                        break
                    else:
                        print('Sinto muito, mas a opção que você digitou não existe. Tente novamente.')
                        continue
                except ValueError:
                    print(f'{Fore.LIGHTRED_EX}                 !!!ERROR!!!\n'
                          f'O valor inserido não é válido. Tente novamente.{Style.RESET_ALL}')
                    continue
                break
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}                 !!!ERROR!!!\n'
                  f'O valor inserido não é válido. Tente novamente.{Style.RESET_ALL}')
        break
