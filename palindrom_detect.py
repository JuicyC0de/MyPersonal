a = 'dabb dbba d'


def palindrom(word):
    word = word.replace(' ', '')
    i = 0
    while i < int(len(word)/2):
        if word[i] == word[-i-1]:
            i += 1
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    print(palindrom(a))
