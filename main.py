from library import cleanerVk


def main():
    login, password = 'gimelside@gmail.com', 'DQ7TQJKA'
    session = cleanerVk(login, password)
    session.deleteTraces()


if __name__ == '__main__':
    main()
