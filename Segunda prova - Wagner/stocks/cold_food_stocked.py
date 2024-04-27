

ice_creams = [['chocolate', 10.0],
              ['morango', 10.0],
              ['baunilha', 12.0],
              ['creme', 16.0],
              ['chiclete', 10.0],
              ['banana caramelada', 12.0],
              ['flocos', 13.0]]

milkshakes = [['chocolate', 15.0],
              ['morango', 14.0],
              ['óreo', 17.0],
              ['maracujá', 18.0],
              ['baunilha', 18.0],
              ['doce de leite', 16.0]]


def food_stock():

    print(f'\n{"=" * 30}')
    print('           SORVETES')
    print('='*30)
    for i in range(0, len(ice_creams)):
        print(f'Sorvete de {ice_creams[i][0].title()} -->  R${ice_creams[i][1]}')
        i += 1
    print(f'\n\n{"="*35}')
    print('            MILK-SHAKES')
    print('='*35)
    for i in range(0, len(milkshakes)):
        print(f'Milk-shake de {milkshakes[i][0].title()} -->  R${milkshakes[i][1]}')
        i += 1
