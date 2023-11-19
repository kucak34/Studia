
def is_user_available(user):
    if user not in user_dict.keys():
        print(f'Nazwa {user} dozwolna')
        return True
    else:
        print(f'Nazwa {user} NIEdozwolona')
        return False

def add_user(user):
    while True:
        passwd1 = input('Podaj haslo: ')
        passwd2 = input('Potwierdź haslo: ')
        if passwd1 == passwd2 and passwd_has_CAP_small_letter(passwd1):
            user_dict[user] = passwd1
            break
        else:
            print('Zle, jeszcze raz')


def suggest_username(user):
    return user + '1'
