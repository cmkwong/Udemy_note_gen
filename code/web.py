from selenium import webdriver

class Controller:
    def __init__(self, init_url):
        self.init_url = init_url
        self.open_chrome()

    def open_chrome(self, executable_path="../driver/chromedriver"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox') # refer: https://stackoverflow.com/questions/43008622/python-linux-selenium-chrome-not-reachable
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
        self.browser.get(self.init_url)

    def highlighted_text(self):
        js_code = """
            return document.querySelectorAll('[class*="transcript--highlight-cue"]')[0].innerText;
        """
        text = self.browser.execute_script(js_code)
        return text

    def read_transcript(self):
        js_code = """
            transcript_list = [];
            list = document.querySelectorAll('[class*="transcript--transcript-panel"]')[0].querySelectorAll('[class*="transcript--underline-cue"]');
            for (let i=0; i<list.length; i++) {
                transcript_list.push(list[i].innerText);
            }
            return transcript_list;
        """
        transcript_list = self.browser.execute_script(js_code)
        return transcript_list