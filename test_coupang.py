from playwright.sync_api import Playwright, sync_playwright
import random, time
# from fake_useragent import UserAgent

# ua = UserAgent()
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

# host = 'http://localhost:8118'
# proxy={'server' : host}

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context(extra_http_headers = extra_header)
    page = context.new_page()
    page.goto(url)
    

    page.get_by_role('textbox').fill("노트북")

    page.get_by_role('link', name='검색').click()

    # tes = page.get_by_role('generic').all()
    # for i in tes:
    #     print(i.text_content())
    # ---------------------

    context.close()
    browser.close()


with sync_playwright() as pw:
    run(pw)