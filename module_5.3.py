class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return  f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other,House):
            print(f'Ваш дом {other} типа не Хаус')
        else:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other,House):
            print(f'Ваш дом {other} типа не Хаус')
        else:
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            print(f'Ваш дом {other} типа не Хаус')
        else:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other,House):
            print(f'Ваш дом {other} типа не Хаус')
        else:
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if not isinstance(other,House):
            print(f'Ваш дом {other} типа не Хаус')
        else:
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
                print(f'Ваш дом {other} типа не Хаус')
        else:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value,int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print(f'Вы прибавили {value}, необходимо прибавить целое число')
        return self


    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print(f'Вы прибавили {value}, необходимо прибавить целое число')
        return self


def __iadd__(self, value):
    if isinstance(value, int):
        self.number_of_floors = self.number_of_floors + value
    else:
        print(f'Вы прибавили {value}, необходимо прибавить целое число')
    return self


house_JR = House('Балтийский берег',15)
house_GM = House('Янтарный берег',10)

print(str(f'\n {house_JR}'))
print(str(house_GM))
print(f'{house_JR == house_GM}\tравенство этажности домов\n')

house_GM = house_GM + 5
print(str(house_GM))
print(str(house_JR))
print(f'{house_JR == house_GM}\tравенство этажности домов\n')

house_JR += 10
print(str(house_JR))
house_GM = 10 + house_GM
print(str(house_GM))
print(f'{house_JR == house_GM}\tравенство этажности домов\n')

print(f'{house_JR < house_GM}\t{house_JR.name} меньше {house_GM.name}')
print(f'{house_JR <= house_GM}\t{house_JR.name} не больше {house_GM.name}')
print(f'{house_JR > house_GM}\t{house_JR.name} больше {house_GM.name}')
print(f'{house_JR >= house_GM}\t{house_JR.name} не меньше {house_GM.name}')
print(f'{house_JR != house_GM}\t{house_JR.name} не равна {house_GM.name}')
