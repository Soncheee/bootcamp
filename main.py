import requests

# Ваш API-ключ для Google Books API (зарегистрируйтесь на https://console.cloud.google.com/, чтобы получить ключ)
API_KEY = "AIzaSyDn9yBPBZ-4nKtiAVE8knpwT5mYV5VAjLI"
BASE_URL = "https://www.googleapis.com/books/v1/volumes"

favourites = []
readed = []

def search_books_by_author(author, many_books=0):
    # Формируем запрос к Google Books API
    params = {
        'q': f'inauthor:{author}',  # Поиск книг по автору
        'key': API_KEY,
        'maxResults': 10,  # Максимум 10 книг
    }

    try:
        # Выполняем GET-запрос
        response = requests.get(BASE_URL, params=params)

        # Проверяем статус ответа
        if response.status_code == 200:
            data = response.json()
            # Проверяем, есть ли результаты
            if 'items' in data:
                print(f"Книги автора '{author}':")
                for item in data['items']:
                    title = item['volumeInfo'].get('title', 'Без названия')
                    authors = item['volumeInfo'].get('authors', ['Неизвестный автор'])
                    published_date = item['volumeInfo'].get('publishedDate', 'Неизвестно')
                    print(
                        f"- Название: {title}\n  Автор(ы): {', '.join(authors)}\n  Дата публикации: {published_date}\n")

                    answers_to_add = (input("Хотите ли вы добавить эту книгу в список избранных или уже прочитанного?(да/нет"))
                    if answers_to_add == "нет":
                        continue
                    elif answers_to_add == "да":
                        add_to = input("куда вы хотите добавить: избранное или прочитанное?")
                        if add_to == "избранное":
                            favourites.append(title)
                            print("Книга добавлена в избранное")
                        elif add_to == "прочитанное":
                            readed.append(title)
                            print("Книга добавлена в прочитанное")
                        else:
                            print("Не пиши ерунду")
                    else:
                        print("Не пиши ерунду")
                    many_books += 1
                    if many_books <= 3:
                        continue
                    else:
                        more = input(("Хотите больше книг этого автора?да/нет"))
                        if more == "да":
                            continue
                        elif more == "нет":
                            print("OK")
                            break

            else:
                print(f"Книги автора '{author}' не найдены.")
        else:
            print(f"Ошибка: код ответа {response.status_code}")
            print(f"Сообщение: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")


def fav(favourites, readed):
    fav_or_readed = input("Хотите посмотреть избранное или прочитанное?.Напишите да или нет")
    if fav_or_readed == "нет":
        print("ok")
    elif fav_or_readed == "да":
        ans = input('напишите "избранное" или "прочитанное"')
        if ans == "избранное":
            print(favourites)
        else:
            print(readed)


# Ввод автора
author_name = input("Введите имя автора для поиска книг: ")
author_name.title()

search_books_by_author(author_name)
fav(favourites, readed)


