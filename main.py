from library import cleanerVk
import sys
import time
from messages import invalid_password

def main():

    print('Введите логин')
    login = input()
    print('Ввведите пароль')
    password = input()
    
    try:
        session = cleanerVk(login, password)
        print('Сколько диалогов просмотреть?')
        session.conversations_count = int(input())
        print('Сколько в среднем сообщений в день вы отправляете?')
        session.messages_count = int(input())
        session.deleteTraces()
    except invalid_password:
        print('Ошибка входа')


    

if __name__ == '__main__':
    main()
