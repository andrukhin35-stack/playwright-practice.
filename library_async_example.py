# ФИО Андрей Андрюхин Иванович
# Дата: 2026-11-12
# Время:
# тема асинхронный запуск Plywright
# Источник:  https://playwright.dev/python/docs/library
# Описание: запускает Chromium через Асинхронный API Playwright
# создает страницу , открывает Playwright.dev выводит загаловок в терминал и закрывает браузер

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())
# результат запуска:
# команда запуска python library_async_example.py
# скрипт выполнен без ошибок
# в терминале выведен playwright