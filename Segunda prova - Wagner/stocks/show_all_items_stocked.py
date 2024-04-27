from stocks import cold_food_stocked, all_book_stocked
from colorama import Fore, Style


def show_ice_creams():
    print(f'\n{"=" * 30}')
    print('           SORVETES')
    print('=' * 30)
    for i in range(0, len(cold_food_stocked.ice_creams)):
        print(f'Sorvete de {cold_food_stocked.ice_creams[i][0]} -->  R${cold_food_stocked.ice_creams[i][1]}')
        i += 1


def show_milkshakes():
    print(f'\n\n{'=' * 35}')
    print('            MILK-SHAKES')
    print('=' * 35)
    for i in range(0, len(cold_food_stocked.milkshakes)):
        print(f'Milk-shake de {cold_food_stocked.milkshakes[i][0]} -->  R${cold_food_stocked.milkshakes[i][1]}')
        i += 1


def show_history_books():
    print(f'\n{"=" * 35}')
    print('        LIVROS DE HISTÓRIA')
    print('=' * 35)
    for i in range(0, len(all_book_stocked.history_books)):
        print(f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.history_books[i][0]}{Style.RESET_ALL}'
              f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.history_books[i][1]}{Style.RESET_ALL}'
              f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.history_books[i][2]}{Style.RESET_ALL}\n')
    print('=' * 70)


def show_fantasy_books():
    print(f'\n{"=" * 35}')
    print('        LIVROS DE FANTASIA')
    print('=' * 35)

    for i in range(0, len(all_book_stocked.fantasy_books)):
        print(f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.fantasy_books[i][0]}{Style.RESET_ALL}'
              f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.fantasy_books[i][1]}{Style.RESET_ALL}'
              f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.fantasy_books[i][2]}{Style.RESET_ALL}\n')


def show_romance_books():
    print(f'\n{"=" * 35}')
    print('        LIVROS DE ROMANCE')
    print('=' * 35)

    for i in range(0, len(all_book_stocked.romance_books)):
        print(f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.romance_books[i][0]}{Style.RESET_ALL}'
              f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.romance_books[i][1]}{Style.RESET_ALL}'
              f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.romance_books[i][2]}{Style.RESET_ALL}\n')


def show_horror_books():
    print(f'\n{"=" * 35}')
    print('        LIVROS DE TERROR')
    print('=' * 35)

    for i in range(0, len(all_book_stocked.horror_books)):
        print(f'\nLivro: {Fore.LIGHTYELLOW_EX}{all_book_stocked.horror_books[i][0]}{Style.RESET_ALL}'
              f'\nAutor: {Fore.LIGHTBLUE_EX}{all_book_stocked.horror_books[i][1]}{Style.RESET_ALL}'
              f'\nPreço: {Fore.LIGHTGREEN_EX}R${all_book_stocked.horror_books[i][2]}{Style.RESET_ALL}\n')


def show_mangas():
    print(f'\n{"=" * 35}')
    print('        MANGÁS')
    print('=' * 35)
    for i in range(0, len(all_book_stocked.mangas)):
        print(f'\nMangá:{Fore.LIGHTYELLOW_EX} {all_book_stocked.mangas[i][0]} {Style.RESET_ALL}'
              f'\nAutor:{Fore.LIGHTBLUE_EX} {all_book_stocked.mangas[i][1]} {Style.RESET_ALL}'
              f'\nPreço pr Capítulo: {Fore.LIGHTGREEN_EX}R${all_book_stocked.mangas[i][2]}{Style.RESET_ALL}'
              f'\nCapítulos:{Fore.LIGHTMAGENTA_EX} {all_book_stocked.mangas[i][3]} {Style.RESET_ALL}\n')


def show_comics():
    print(f'\n{"=" * 35}')
    print("         COMICS")
    print('=' * 35)

    for i in range(0, len(all_book_stocked.comics)):
        print(f'\nMangá:{Fore.LIGHTYELLOW_EX} {all_book_stocked.comics[i][0]} {Style.RESET_ALL}'
              f'\nAutor:{Fore.LIGHTBLUE_EX} {all_book_stocked.comics[i][1]} {Style.RESET_ALL}'
              f'\nPreço por Edição: {Fore.LIGHTGREEN_EX}R${all_book_stocked.comics[i][2]} {Style.RESET_ALL}'
              f'\nEdições:{Fore.LIGHTMAGENTA_EX} {all_book_stocked.comics[i][3]} {Style.RESET_ALL}\n')

