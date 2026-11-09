import re
from playwright.sync_api import Page, expect


#ФИО Андрей Андрюхин Иванович
# Дата: 09-11-2026
# Время: 14:30
# Описание: открываю главную страницу Playwright и проверяю,
# что загаловок вкладки содержит слово Playwright.
# Изменение: добавил re.IGNORECASE.
# Зачем: чтобы проверка слова Playwright не зависела от регистра букв.

def test_has_title(page: Page):
    # Открываю главную страницу сайта.
    page.goto("https://playwright.dev/")

    # Проверяю заголовок без учета регистра букв.
    expect(page).to_have_title(
        re.compile("Playwright", re.IGNORECASE)
    )

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    # Результат запуска: 2 passed, оба теста прошли успешно.
    # Команда: python -m pytest test_example.py -v
    # Оба теста прошли успешно: 2 passed.