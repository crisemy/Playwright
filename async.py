import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # By default runs in the background. In False, open up the browser instead of running it in the background.
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://whatsmyuseragent.org")
        print(await page.title())
        await browser.close()

asyncio.run(main())