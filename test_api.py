# ФИО: Андрей Андрюхин Иванович.
# Дата: 2026-11-10
# Время: 18:37
# Тема: API-тестирование с помощью Playwright.
# Источник: https://playwright.dev/python/docs/api-testing
# Описание: отправляю GET-запрос для получения записи №1.
# Проверяю статус ответа, номер записи и номер её автора.
from playwright.sync_api import Playwright


def test_get_post(playwright: Playwright):
    # Создаю отдельный контекст для HTTP-запросов.
    api = playwright.request.new_context()

    try:
        # Запрашиваю запись с номером 1.
        response = api.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        # Проверяю, что сервер ответил успешно.
        assert response.status == 200

        # Преобразую JSON из ответа в словарь Python.
        data = response.json()

        # Показываю ответ в терминале.
        print("Статус:", response.status)
        print("Данные:", data)

        # Проверяю номер полученной записи.
        assert data["id"] == 1

        # Проверяю номер автора записи.
        assert data["userId"] == 1

    finally:
        # Освобождаю ресурсы даже при ошибке проверки.
        api.dispose()
        # Результат запуска:
    # Команда: python -m pytest test_api.py -v -s
    # Тест прошёл успешно: 1 passed.
    # Сервер вернул статус 200.
    # Полученная запись имеет id=1 и userId=1.