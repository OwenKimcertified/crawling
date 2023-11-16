from playwright.sync_api import Playwright, sync_playwright
import random, time
# from fake_useragent import UserAgent
# ua = UserAgent()
# ua.random()

ran_sec = random.uniform(0.1, 4)
waiting = time.sleep(ran_sec)
url = 'https://www.coupang.com/'
extra_header = {
    'Referer': 'https://www.google.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Language': 'ko-KR',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Security-Policy': 'upgrade-insecure-requests;',
    'Content-Type': 'text/html;charset=UTF-8',
    'Sec-Ch-Ua-Platform': "Windows",
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def request_headers(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context(extra_http_headers = extra_header)
    page = context.new_page()
    
    response = page.goto('https://www.coupang.com/')
    
    headers = response.all_headers()

    for key, value in headers.items():
        print(f"{key}: {value}")
    
    context.close()
    browser.close()


def crawling_data(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context(extra_http_headers = extra_header)
    page = context.new_page()
    page.goto(url)
    
    page.get_by_role('textbox').fill("노트북")
    waiting

    page.get_by_role('link', name = '검색').click()
    waiting
    page.wait_for_load_state()

    # notebook product pagination 1.
    # product_table = page.locator('.search-product-list').all()
    # waiting

    # for product in product_table:
    #     print(product.inner_text())
    #     waiting

    page.goto(url)

    context.close()
    browser.close()

def request_headers(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context(extra_http_headers = extra_header)
    page = context.new_page()
    
    response = page.goto('https://www.coupang.com/')
    
    headers = response.all_headers()

    for key, value in headers.items():
        print(f"{key}: {value}")
    
    context.close()
    browser.close()

with sync_playwright() as pw:
    crawling_data(pw)