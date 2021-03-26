import ui, web

INIT_URL = "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/learn/lecture/15064978#notes"
X = (146,1280)
Y = (169,800)
MAIN_PATH = "C:/Users/Chris/projects/210326_Udemy_autogen_notes/docs"
IMG_DIR = "pic"
TEXT_DIR = "text"
TRANSCRIPT_TXT_FILE = "transcript.txt"
MARK_TXT_FILE = "marks.txt"

web_controller = web.Controller(init_url=INIT_URL)
controller = ui.Controller(web_controller, X, Y, MAIN_PATH, IMG_DIR, TEXT_DIR, TRANSCRIPT_TXT_FILE, MARK_TXT_FILE)
controller.run()