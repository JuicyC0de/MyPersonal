from time import sleep


def clear():
    print("\n"*20)


def disp(lyb):
    for i in lyb:
        yield i


library = [' GUCCI ', ' PRADA ', ' ARMANI ', '  D&G  ', '  L&V  ']
print('Load butique...')
for i in range(len(library)):
    print('\r', int((i+1)*(100/len(library))), '%', library[i]*10, end=' ',)
    sleep(1)
print('\n', 'Load complete')