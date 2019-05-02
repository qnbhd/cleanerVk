from library import cleanerVk


def main():
    login, password = 'login', 'password'
    session = cleanerVk(login, password)
    session.deleteTraces()


if __name__ == '__main__':
    main()
