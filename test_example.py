from playwright.sync_api import Playwright, sync_playwright, expect, APIRequestContext
from playwright_stealth import stealth_sync
from typing import Generator
import random, time, pytest

ran_sec = random.uniform(1, 4)
url = 'https://breachforums.is/Forum-Databases'
extra_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',}

# .tborder clear, div class float left -> class pagination -> class pagination_current


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(extra_http_headers = extra_header)
    stealth_sync(context) 
    page = context.new_page()
    page.goto(url)
    # legacy
    # elements = page.query_selector_all('.tborder.clear')
    
    # if elements:
    #     for element in elements:
    #         table_data = element.inner_text()

    d = page.locator('.tborder.clear tbody tr').and_(page.locator('.inline_row'))    
    post = d.get_by_role('link').all()

    # click => scrap => backspace
    for i in post:
        # print(i.text_content())
        i.click()
        element = page.locator('table')
        if element.is_visible():
            element.inner_text()
        else:
            pass
        print(element.inner_text())
        time.sleep(ran_sec)
        page.goto("https://breachforums.is/Forum-Databases")


    context.close()
    browser.close()

@pytest.fixture(scope="session", autouse=True)
def test(api_request_context: APIRequestContext,) -> Generator[None, None, None]:

    new_repo = api_request_context.post("/user/repos", data={"name": 'GITHUB_REPO'})
    assert new_repo.ok
    yield

    deleted_repo = api_request_context.delete(f"/repos/{'GITHUB_USER'}/{'GITHUB_REPO'}")
    assert deleted_repo.ok

with sync_playwright() as playwright:
    run(playwright)


