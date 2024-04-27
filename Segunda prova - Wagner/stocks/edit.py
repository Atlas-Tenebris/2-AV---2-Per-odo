from colorama import Fore, Style
from stocks import cold_food_stocked, all_book_stocked, show_all_items_stocked

mistakes = 0
ice_cream_removed = 0
milkshake_removed = False


def decrease():
    global ice_cream_removed
    global milkshake_removed
    while True:
        choice = str(input('\nQual estoque deseja editar?'
                           '\n - Sobremesas geladas.'
                           '\n - Livros.'
                           '\n - Voltar.'
                           '\n\nDigite: ')).title()
        if choice == 'Sobremesas' or choice == 'Sobremesas geladas' or choice == 'Sobremesa'\
                or choice == 'Sobremesa Gelada':
            while True:
                try:
                    product = str(input('\nDigite qual tipo de sobremesa gelada deseja editar o estoque:'
                                        '\n- Sorvete'
                                        '\n- Milk-Shake'
                                        '\n- Voltar.'
                                        '\n\nDigite: ')).lower().strip()
                    if product == 'sorvete' or product == 'sorvetes':
                        print('\nEsses são todos os sorvetes que comercializamos: \n')

                        show_all_items_stocked.show_ice_creams()
                        while True:
                            ice_cream_removed = False
                            change = str(input('\nDigite o nome do sabor de sorvete que quer retirar '
                                               'do estoque: '))
                            if 'sorvete' in change or 'sorvetes' in change:
                                print(f'Não digite o tipo de produto, apenas o sabor, por favor.')
                                continue
                            if 'milkshake' in change or 'milk-shake' in change:
                                print('\nNão digite o tipo de produto, apenas o sabor, por favor.\n'
                                      'Se quiser retirar um milkshake, selecione o estoque de milkshakes.')
                                continue
                            for item in cold_food_stocked.ice_creams:
                                if change.lower().strip() == item[0].lower().strip():
                                    cold_food_stocked.ice_creams.remove(item)
                                    ice_cream_removed = True
                                    print(f'\nO produto {Fore.LIGHTYELLOW_EX}"{change.title()}"{Style.RESET_ALL}'
                                          f' foi removido com sucesso do estoque.')
                                    break
                                elif change != item[0].lower():
                                    pass
                            if ice_cream_removed is False:
                                print('Produto não encontrado.')
                                break
                            break
                    elif product == 'milkshakes' or product == 'milk-shakes' or product == 'milk-shake' \
                            or product == 'milkshake':
                        while True:
                            milkshake_removed = False
                            print('\nEsses são todos os Milk-Shakes que comercializamos: \n')

                            show_all_items_stocked.show_milkshakes()
                            change = str(input('\nDigite o nome do sabor de milk-shake que quer retirar '
                                               'do estoque: ')). lower(). strip()
                            if 'milkshake' in change or 'milk-shake' in change:
                                print(f'\nNão digite o tipo de produto, apenas o sabor, por favor.')
                                continue
                            if 'sorvete' in change or 'sorvetes' in change:
                                print('\nNão digite o tipo de produto, apenas o sabor, por favor.\n'
                                      'Se quiser retirar um sorvete, selecione o estoque de sorvetes.')
                                continue
                            for item in cold_food_stocked.milkshakes:
                                if change.lower().strip() == item[0].lower():
                                    cold_food_stocked.milkshakes.remove(item)
                                    milkshake_removed = True
                                    break
                                elif change != item[0].lower():
                                    pass
                            if milkshake_removed is False:
                                print('Sabor não encontrado.')
                                continue
                            if milkshake_removed is True:
                                print(f'O Milk-Shake de{Fore.LIGHTYELLOW_EX} "{change}" {Style.RESET_ALL}'
                                      f' foi removido do estoque com sucesso!')
                            break
                    elif product == 'voltar' or product == 'voltar ao menu':
                        break
                    else:
                        print(f'{Fore.LIGHTRED_EX}Escolha inválida!!{Style.RESET_ALL}'
                              f'\nDigite uma das opções fornecidas.')
                        continue
                except ValueError:
                    print(f'{Fore.LIGHTRED_EX}!!!ERROR!!!{Style.RESET_ALL}'
                          f'\nO valor inserido é inválido. Por favor, tente novamente.')
        elif choice == 'livros':
            while True:
                book_found = 0
                sec_choice = str(input('Digite qual categoria de livros quer ver:'
                                       '\n - Livros de história.'
                                       '\n - Livros de fantasia.'
                                       '\n - Livros de terror.'
                                       '\n - Livros de romance.'
                                       '\n - Mangás'
                                       "\n - Comics (Hq's)"
                                       "\n\nDigite: ")).lower().strip()
                if sec_choice == 'livros de história' or sec_choice == 'livros de historia' \
                        or sec_choice == 'história' or sec_choice == 'historia':
                    print(f'\n{"=" * 35}')
                    print('        LIVROS DE HISTÓRIA')
                    print('=' * 35)
                    for i in range(1, len(all_book_stocked.history_books)):
                        print(
                            f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.history_books[i][0]}'
                            f'{Style.RESET_ALL}'
                            f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.history_books[i][1]}'
                            f'{Style.RESET_ALL}'
                            f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.history_books[i][2]}'
                            f'{Style.RESET_ALL}')
                    print('=' * 70)
                    change = str(input('\nQual livro você deseja remover do estoque?\n'
                                       'Nome do livro: '))
                    for item in all_book_stocked.history_books:
                        if change.lower().strip() == item[0].lower().strip():
                            all_book_stocked.history_books.remove(item)
                            book_found = 1
                            print(f'O livro {Fore.LIGHTYELLOW_EX}"{change.title()}"{Style.RESET_ALL}'
                                  f' foi retirado do estoque de livros de história')

                        elif change.lower().strip() != item[0].lower().strip():
                            pass
                    if book_found == 0:
                        print(f'\n{Fore.LIGHTRED_EX}Livro não encontrado.{Style.RESET_ALL}\n')
                    break
                elif sec_choice == 'fantasia' or sec_choice == 'livros de fantasia' \
                        or sec_choice == 'livro de fantasia':
                    print(f'\n{"=" * 35}')
                    print('        LIVROS DE FANTASIA')
                    print('=' * 35)

                    for i in range(1, len(all_book_stocked.fantasy_books)):
                        print(
                            f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.fantasy_books[i][0]}'
                            f'{Style.RESET_ALL}'
                            f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.fantasy_books[i][1]}'
                            f'{Style.RESET_ALL}'
                            f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.fantasy_books[i][2]}'
                            f'{Style.RESET_ALL}')
                    print('=' * 70)
                    change = str(input('\nQual livro você deseja remover do estoque?\n'
                                       'Nome do livro: '))
                    for item in all_book_stocked.fantasy_books:
                        if change.lower().strip() == item[0].lower().strip():
                            all_book_stocked.fantasy_books.remove(item)
                            book_found = 1
                            print(f'O livro {Fore.LIGHTYELLOW_EX}"{change.title()}"{Style.RESET_ALL}'
                                  f' foi retirado do estoque de livros de fantasia')

                        elif change.lower().strip() != item[0].lower().strip():
                            pass
                        if book_found == 0:
                            print(f'\n{Fore.LIGHTRED_EX}Livro não encontrado.{Style.RESET_ALL}\n')
                        break
                elif sec_choice == 'terror' or sec_choice == 'livro de terror' \
                        or sec_choice == 'livros de terror':
                    print(f'\n{"=" * 35}')
                    print('        LIVROS DE TERROR')
                    print('=' * 35)

                    for i in range(1, len(all_book_stocked.horror_books)):
                        print(
                            f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.horror_books[i][0]}'
                            f'{Style.RESET_ALL}'
                            f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.horror_books[i][1]}'
                            f'{Style.RESET_ALL}'
                            f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.horror_books[i][2]}'
                            f'{Style.RESET_ALL}')
                    print('=' * 70)
                    change = str(input('\nQual livro você deseja remover do estoque?\n'
                                       'Nome do livro: '))
                    for item in all_book_stocked.horror_books:
                        if change.lower().strip() == item[0].lower().strip():
                            all_book_stocked.horror_books.remove(item)
                            book_found = 1
                            print(f'O livro {Fore.LIGHTYELLOW_EX}"{change.title()}"{Style.RESET_ALL}'
                                  f' foi retirado do estoque de livros de terror.')

                        elif change.lower().strip() != item[0].lower().strip():
                            pass
                        if book_found == 0:
                            print(f'\n{Fore.LIGHTRED_EX}Livro não encontrado.{Style.RESET_ALL}\n')
                        break
                elif sec_choice == 'romance' or sec_choice == 'livro de romance' \
                        or sec_choice == 'livros de romance':
                    print(f'\n{"=" * 35}')
                    print('        LIVROS DE ROMANCE')
                    print('=' * 35)

                    for i in range(1, len(all_book_stocked.romance_books)):
                        print(
                            f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.romance_books[i][0]}'
                            f'{Style.RESET_ALL}'
                            f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.romance_books[i][1]}'
                            f'{Style.RESET_ALL}'
                            f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.romance_books[i][2]}'
                            f'{Style.RESET_ALL}')
                        change = str(input('\nQual livro você deseja remover do estoque?\n'
                                           'Nome do livro: '))
                        for item in all_book_stocked.fantasy_books:
                            if change.lower().strip() == item[0].lower().strip():
                                all_book_stocked.fantasy_books.remove(item)
                                book_found = 1
                                print(
                                    f'O livro {Fore.LIGHTYELLOW_EX}"{change}"{Style.RESET_ALL} foi retirado do '
                                    f'estoque de livros de romance.')

                            elif change.lower().strip() != item[0].lower().strip():
                                pass
                            if book_found == 0:
                                print(f'\n{Fore.LIGHTRED_EX}Livro não encontrado.{Style.RESET_ALL}\n')
                            break
                elif sec_choice == 'mangas' or sec_choice == 'mangás':
                    print(f'\n{"=" * 35}')
                    print('        MANGÁS')
                    print('=' * 35)

                    for i in range(1, len(all_book_stocked.mangas)):
                        print(f'\nMangá:{Fore.LIGHTYELLOW_EX} {all_book_stocked.mangas[i][0]}'
                              f'{Style.RESET_ALL}'
                              f'\nAutor:{Fore.LIGHTBLUE_EX} {all_book_stocked.mangas[i][1]}'
                              f'{Style.RESET_ALL}'
                              f'\nPreço pr Capítulo: {Fore.LIGHTGREEN_EX}R${all_book_stocked.mangas[i][2]}'
                              f'{Style.RESET_ALL}'
                              f'\nCapítulos:{Fore.LIGHTMAGENTA_EX} {all_book_stocked.mangas[i][3]}'
                              f'{Style.RESET_ALL}')
                    print('=' * 70)
                    change = str(input('\nQual mangá você deseja remover do estoque?\n'
                                       'Nome do mangá: '))
                    for item in all_book_stocked.mangas:
                        if change.lower().strip() == item[0].lower().strip():
                            all_book_stocked.mangas.remove(item)
                            book_found = 1
                            print(f'O mangá {Fore.LIGHTYELLOW_EX}"{change.title()}"{Style.RESET_ALL}'
                                  f' foi retirado do estoque de mangás')

                        elif change.lower().strip() != item[0].lower().strip():
                            pass
                    if book_found == 0:
                        print(f'\n{Fore.LIGHTRED_EX}Livro não encontrado.{Style.RESET_ALL}\n')
                    break
                elif sec_choice == 'comics' or sec_choice == "hq's" or sec_choice == 'quadrinhos' \
                        or sec_choice == 'hq':
                    print(f'\n{"=" * 35}')
                    print("         COMICS")
                    print('=' * 35)

                    for i in range(1, len(all_book_stocked.comics)):
                        print(f'\nMangá:{Fore.LIGHTYELLOW_EX} {all_book_stocked.comics[i][0]}'
                              f'{Style.RESET_ALL}'
                              f'\nAutor:{Fore.LIGHTBLUE_EX} {all_book_stocked.comics[i][1]}'
                              f'{Style.RESET_ALL}'
                              f'\nPreço por Edição: {Fore.LIGHTGREEN_EX}R${all_book_stocked.comics[i][2]}'
                              f'{Style.RESET_ALL}'
                              f'\nEdições:{Fore.LIGHTMAGENTA_EX} {all_book_stocked.comics[i][3]}'
                              f'{Style.RESET_ALL}')
                    print('=' * 70)
                    change = str(input('\nQual mangá você deseja remover do estoque?\n'
                                       'Nome do mangá: '))
                    for item in all_book_stocked.comics:
                        if change.lower().strip() == item[0].lower().strip():
                            all_book_stocked.comics.remove(item)
                            book_found = 1
                            print(f'A HQ {Fore.LIGHTYELLOW_EX}"{change.title()}"{Style.RESET_ALL}'
                                  f' foi retirada do estoque de comics.')

                        elif change.lower().strip() != item[0].lower().strip():
                            pass
                    if book_found == 0:
                        print(f'\n{Fore.LIGHTRED_EX}Livro não encontrado.{Style.RESET_ALL}\n')
                    break
        elif choice.lower().strip() == 'voltar' or choice == 'voltar ao menu':
            break
        else:
            print(f'{Fore.LIGHTRED_EX} !!!!ERROR!!!!{Style.RESET_ALL}'
                  f'\nOpção inválida, tente novamente.')
            continue


def increase():
    while True:
        try:
            choice = str(input('\nQual estoque deseja adicionar algum produto?'
                               '\n  Sobremesas geladas.'
                               '\n  Livros.'
                               '\n  Voltar.'
                               '\n Digite: ')).lower().strip()
            if choice == 'sobremesas' or choice == 'sobremesas geladas':
                while True:
                    stock_name = str(input('\ndigite em qual estoque deseja adicionar (Sorvete ou'
                                           ' Milk-shake): ')).lower().strip()
                    if stock_name == 'sorvetes' or stock_name == 'sorvete':
                        print('\nÓtimo. Este é o estoque atual de sorvetes: ')
                        show_all_items_stocked.show_ice_creams()
                        while True:
                            has_digit = False
                            flavour = str(input('\nDigite o sabor do sorvete: ')).lower().strip()
                            if any(flavour in taste for taste in cold_food_stocked.ice_creams):
                                print(f'{Fore.LIGHTRED_EX}O sabor já esxiste no estoque.{Style.RESET_ALL}'
                                      f'\nDigite um sabor novo.')
                                continue
                            for caractere in flavour:
                                if caractere.isdigit():
                                    has_digit = True
                                    break
                                else:
                                    pass
                            if has_digit is True:
                                print(f'{Fore.LIGHTRED_EX}O sabor não pode conter números{Style.RESET_ALL}')
                                continue
                            if 'milkshake' in flavour or 'milk-shake' in flavour:
                                print(f'\nSe quiser adicionar um milk-shake, adicione-o ao estoque de milk-shakes.'
                                      f'Também não coloque o tipo do produto, apenas o sabor.\n')
                                continue
                            if 'sorvete' in flavour or 'sorvetes' in flavour:
                                print('Não coloque o tipo de produto, apenas o sabor.\n')
                            else:
                                while True:
                                    try:
                                        price = float(input(f'Digite o valor do sorvete de {flavour}: '))
                                        if price < 4.0:
                                            print(
                                                f'{Fore.LIGHTRED_EX}O produto está muito barato!{Style.RESET_ALL}\n'
                                                f'Isso não paga nem o leite pra fazer o'
                                                ' sorvete.\nInsira outro valor, em nome de Deus.\n')
                                            continue
                                        elif price > 20:
                                            print(f'{Fore.LIGHTRED_EX}O produto está muito caro.{Style.RESET_ALL}'
                                                  '\n Eu quero que alguém possa comprar ele. Coloque um preço '
                                                  'mais baixo.\n')
                                            continue
                                        else:
                                            new_flavour = [flavour, price]
                                            cold_food_stocked.ice_creams.append(new_flavour)
                                            print(f'\nNovo sabor{Fore.LIGHTYELLOW_EX} "{flavour}" {Style.RESET_ALL}'
                                                  f'adicionado ao estoque de sorvetes com sucesso!!')
                                            break
                                    except ValueError:
                                        print(f'{Fore.LIGHTRED_EX}!!!ERROR!!!{Style.RESET_ALL}'
                                              f'\nO valor inserido é inválido. Tente novamente.')
                            break
                    elif stock_name == 'milk-shake' or stock_name == 'milkshake' or stock_name == 'milkshakes'\
                            or stock_name == 'milk-shakes':
                        print('Ótimo, este é o estoque de milk-shakes: ')
                        show_all_items_stocked.show_milkshakes()
                        while True:
                            has_digit = False
                            flavour = str(input('\nDigite o sabor do Milk-shake: ')).lower().strip()
                            if any(flavour in taste for taste in cold_food_stocked.milkshakes):
                                print(f'{Fore.LIGHTRED_EX}O sabor já esxiste no estoque.{Style.RESET_ALL}'
                                      f'\nDigite um sabor novo.')
                                continue
                            for caractere in flavour:
                                if caractere.isdigit():
                                    has_digit = True
                                    break
                                else:
                                    pass
                            if has_digit is True:
                                print(f'{Fore.LIGHTRED_EX}O sabor não pode conter números{Style.RESET_ALL}')
                                continue
                            if 'sorvete' in flavour:
                                print(f'\nSe quiser adicionar um sorvete, adicione-o ao estoque de sorvete.'
                                      f'Também não coloque o tipo do produto, apenas o sabor.\n')
                                continue
                            if 'milkshake' in flavour or 'milk-shake' in flavour:
                                print('Não coloque o tipo de produto, apenas o sabor.\n')
                                continue
                            else:
                                while True:
                                    try:
                                        price = float(input(f'Digite o valor do Milk-Shake de {flavour}: '))
                                        if price < 10.0:
                                            print(
                                                f'{Fore.LIGHTRED_EX}O produto está muito barato!'
                                                f'{Style.RESET_ALL}\n'
                                                f'Isso não paga nem o leite pra fazer o'
                                                ' Milk-Shake.\nInsira outro valor, em nome de Deus.\n')
                                            continue
                                        elif price > 25:
                                            print(
                                                f'{Fore.LIGHTRED_EX}O produto está muito caro.{Style.RESET_ALL}'
                                                '\n Eu quero que alguém possa comprar ele. Coloque um preço '
                                                'mais baixo.\n')
                                            continue
                                        else:
                                            new_flavour = [flavour, price]
                                            cold_food_stocked.milkshakes.append(new_flavour)
                                            print(
                                                f'\nNovo sabor{Fore.LIGHTYELLOW_EX} "{flavour.title()}"'
                                                f' {Style.RESET_ALL}'
                                                f'adicionado ao estoque de Milk-shakes com sucesso!!')
                                            break
                                    except ValueError:
                                        print(f'{Fore.LIGHTRED_EX}!!!ERROR!!!{Style.RESET_ALL}'
                                              f'\nO valor inserido é inválido. Tente novamente.')
                            break
                    else:
                        print(f'{Fore.LIGHTRED_EX}ESTOQUE INEXISTENTE!!!{Style.RESET_ALL}'
                              f'\nDigite o nome de um estoque válido. "Sorvete" ou "Milk-shake".')
                        continue
                    break

            elif choice == 'livros' or choice == 'livro':
                while True:
                    stock_name = str(input('\nDigite qual categoria de livros deseja incluir um livro:\n'
                                           '    \n\n - Terror                - História '
                                           '    \n\n - Romance               - Mangás'
                                           '    \n\n - Fantasia              - Comics'
                                           '\n\nDigite: ')).lower().strip()
                    if stock_name == 'terror':
                        print('\nÓtimo. os livros de terror são: \n')
                        show_all_items_stocked.show_horror_books()
                        title = str(input('\nDigite o nome do livro de terror que deseja adicionar: ')).lower().strip()
                        duplicated_book = False
                        for item in all_book_stocked.horror_books:
                            if title == item[0].lower().strip():
                                duplicated_book = True
                                break
                        if duplicated_book is True:
                            print(f'{Fore.LIGHTRED_EX}O livro "{title.title()}" já existe no estoque.{Style.RESET_ALL}'
                                  f'\nTente outro livro.')
                            continue
                        else:
                            price = float(input('\nDigite o preço do livro: R$'))
                            if price < 10.0:
                                print('\nNão é viável vender um livro por menos de R$10; bote outro preço, por'
                                      ' favor.')
                                continue

                            author = str(input('Digite o nome do autor do livro: '))
                            new_book = [[title, author, price]]
                            all_book_stocked.horror_books.append(new_book)
                            print(f'\nO livro {Fore.LIGHTYELLOW_EX}"{title.title()}"{Style.RESET_ALL}'
                                  f' foi adicionado ao estoque de livros de terror.')
                            break
                    elif stock_name == 'fantasia':
                        print('\nÓtimo. os livros de fantasia são: \n')
                        show_all_items_stocked.show_fantasy_books()
                        title = str(input('\nDigite o nome do livro de fantasia'
                                          ' que deseja adicionar: ')).lower().strip()
                        duplicated_book = False
                        for item in all_book_stocked.fantasy_books:
                            if title == item[0].lower().strip():
                                duplicated_book = True
                                break
                        if duplicated_book is True:
                            print(f'{Fore.LIGHTRED_EX}O livro "{title.title()}" já existe no estoque.{Style.RESET_ALL}'
                                  f'\nTente outro livro.')
                            continue
                        else:
                            price = float(input('\nDigite o preço do livro: R$'))
                            if price < 10.0:
                                print('\nNão é viável vender um livro por menos de R$10; bote outro preço, por'
                                      ' favor.')
                                continue

                            author = str(input('Digite o nome do autor do livro: '))
                            new_book = [[title, author, price]]
                            all_book_stocked.fantasy_books.append(new_book)
                            print(f'\nO livro {Fore.LIGHTYELLOW_EX}"{title.title()}"{Style.RESET_ALL}'
                                  f' foi adicionado ao estoque de livros de fantasia.')
                            break
                    elif stock_name == 'romance':
                        print('\nÓtimo. os livros de romance são: \n')
                        show_all_items_stocked.show_romance_books()
                        title = str(input('\nDigite o nome do livro de romance que deseja adicionar: ')).lower().strip()
                        duplicated_book = False
                        for item in all_book_stocked.romance_books:
                            if title == item[0].lower().strip():
                                duplicated_book = True
                                break
                        if duplicated_book is True:
                            print(f'{Fore.LIGHTRED_EX}O livro "{title.title()}" já existe no estoque.{Style.RESET_ALL}'
                                  f'\nTente outro livro.')
                            continue
                        else:
                            price = float(input('\nDigite o preço do livro: R$'))
                            if price < 10.0:
                                print('\nNão é viável vender um livro por menos de R$10; bote outro preço, por'
                                      ' favor.')
                                continue

                            author = str(input('Digite o nome do autor do livro: '))
                            new_book = [[title, author, price]]
                            all_book_stocked.romance_books.append(new_book)
                            print(f'\nO livro {Fore.LIGHTYELLOW_EX}"{title.title()}"{Style.RESET_ALL}'
                                  f' foi adicionado ao estoque de livros de romance.')
                            break
                    elif stock_name == 'história':
                        print('\nÓtimo. os livros de história são: \n')
                        show_all_items_stocked.show_horror_books()
                        title = str(input('\nDigite o nome do livro de história que'
                                          ' deseja adicionar: ')).lower().strip()
                        duplicated_book = False
                        for item in all_book_stocked.history_books:
                            if title == item[0].lower().strip():
                                duplicated_book = True
                                break
                        if duplicated_book is True:
                            print(f'{Fore.LIGHTRED_EX}O livro "{title.title()}" já existe no estoque.{Style.RESET_ALL}'
                                  f'\nTente outro livro.')
                            continue
                        else:
                            price = float(input('\nDigite o preço do livro: R$'))
                            if price < 10.0:
                                print('\nNão é viável vender um livro por menos de R$10; bote outro preço, por'
                                      ' favor.')
                                continue

                            author = str(input('Digite o nome do autor do livro: '))
                            new_book = [[title, author, price]]
                            all_book_stocked.history_books.append(new_book)
                            print(f'\nO livro {Fore.LIGHTYELLOW_EX}"{title.title()}"{Style.RESET_ALL}'
                                  f' foi adicionado ao estoque de livros de história.')
                            break
                    elif stock_name == 'mangás' or stock_name == 'mangas':
                        print('\nÓtimo. Os mangás são são: \n')
                        show_all_items_stocked.show_mangas()
                        title = str(input('\nDigite o nome do mangá que deseja adicionar:')).lower().strip()
                        duplicated_book = False
                        for item in all_book_stocked.mangas:
                            if title == item[0].lower().strip():
                                duplicated_book = True
                                break
                        if duplicated_book is True:
                            print(f'{Fore.LIGHTRED_EX}O mangá "{title.title()}" já existe no estoque.{Style.RESET_ALL}'
                                  f'\nTente outro mangá.')
                            continue
                        else:
                            price = float(input('\nDigite o preço do mangá: R$'))
                            if price < 8.0:
                                print('\nNão é viável vender um livro por menos de R$8; bote outro preço, por'
                                      ' favor.')
                                continue

                            author = str(input('Digite o nome do mangaká (autor/desenhista do mangá): '))
                            new_book = [[title, author, price]]
                            all_book_stocked.mangas.append(new_book)
                            print(f'\nO livro {Fore.LIGHTYELLOW_EX}"{title.title()}"{Style.RESET_ALL}'
                                  f' foi adicionado ao estoque de mangás.')
                            break
                    elif stock_name == 'comics' or stock_name == 'hqs' or stock_name == "hq's":
                        print('\nÓtimo. Os quadrinhos são são: \n')
                        show_all_items_stocked.show_comics()
                        title = str(input('\nDigite o nome do quadrinho que deseja adicionar:')).lower().strip()
                        duplicated_book = False
                        for item in all_book_stocked.comics:
                            if title == item[0].lower().strip():
                                duplicated_book = True
                                break
                        if duplicated_book is True:
                            print(f'{Fore.LIGHTRED_EX}O mangá "{title.title()}" já existe no estoque.{Style.RESET_ALL}'
                                  f'\nTente outro quadrinho.')
                            continue
                        else:
                            price = float(input('\nDigite o preço do quadrinho: R$'))
                            if price < 12.0:
                                print('\nNão é viável vender um livro por menos de R$12; bote outro preço, por'
                                      ' favor.')
                                continue

                            author = str(input('Digite o nome do mangaká (autor/desenhista do mangá): '))
                            new_book = [[title, author, price]]
                            all_book_stocked.comics.append(new_book)
                            print(f'\nO livro {Fore.LIGHTYELLOW_EX}"{title.title()}"{Style.RESET_ALL}'
                                  f' foi adicionado ao estoque de quadrinhos.')
                            break
                    else:
                        print(f'\n{Fore.LIGHTRED_EX}Estoque inexistente.{Style.RESET_ALL}'
                              f'\nPor favor, digite um dos estoques mostrados.')
            elif choice == 'voltar' or choice == 'voltar ao menu':
                break
            else:
                print(f'{Fore.LIGHTRED_EX}!!!!ERROR!!!!{Style.RESET_ALL}'
                      f'\nA opção escolhida não existe. Tente novamente, por favor.')
                continue
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}!!!ERROR!!!{Style.RESET_ALL}'
                  f'\nO valor inserido é inválido. Tente novamente.')
        break
