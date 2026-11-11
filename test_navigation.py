from playwright.sync_api import Page, expect


def test_task_checkbox(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")

    task_input = page.get_by_role("textbox")
    task_input.fill("Изучить Playwright")
    task_input.press("Enter")

    task = page.get_by_role("listitem").filter(
        has_text="Изучить Playwright"
    )
    checkbox = task.get_by_role("checkbox")

    expect(checkbox).not_to_be_checked()

    checkbox.check()
    expect(checkbox).to_be_checked()

    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()