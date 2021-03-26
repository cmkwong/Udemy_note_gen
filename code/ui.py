import tkinter as tk
import common
from functools import partial
from datetime import datetime

class Controller:
    def __init__(self, web, X, Y, main_path, img_dir, text_dir, transcript_txt_file, mark_txt_file):
        self.web_controller = web
        self.window = tk.Tk()
        self.window.title("Udemy Notes Auto Gen")
        self.window.wm_attributes("-topmost", 1)
        self.img_count = 0

        def read_transcript(self):
            text_path = main_path + '/' + text_dir
            transcript_list = self.web_controller.read_transcript()
            for transcript in transcript_list:
                common.append_text(transcript, text_path, transcript_txt_file)

        def cap_screen(self):
            # current time
            now = datetime.now()
            DT_STRING = now.strftime("%y%m%d%H%M%S")
            img_path = main_path + '/' + img_dir
            text_path = main_path + '/' + text_dir

            img_file_name = "{}_{}.jpg".format(str(self.img_count), DT_STRING)
            common.cap_screen(X[0],Y[0],X[1],Y[1], img_path, img_file_name)
            mark = self.web_controller.highlighted_text()
            common.append_text(mark, text_path, mark_txt_file)
            self.img_count += 1

        def clear_docs(self):
            common.init_docs(main_path, img_dir, text_dir)
            self.img_count = 0

        def write_doc(self):
            transcript_list = common.read_text2list(main_path + '/' + text_dir, transcript_txt_file, cut='\n\n')
            mark_list = common.read_text2list(main_path + '/' + text_dir, mark_txt_file, cut='\n\n')
            text_list = common.compara_transcript_with_mark(transcript_list, mark_list)
            common.write_notes(text_list, main_path, img_dir, text_dir)

        # def button
        read_btn = tk.Button(self.window, text="Read Transcript", fg="green", command=partial(read_transcript, self))
        cpsrc_btn = tk.Button(self.window, text="Cap Screen", fg="green", command=partial(cap_screen, self))
        clear_btn = tk.Button(self.window, text="Clean", fg="black", command=partial(clear_docs, self))
        write_btn = tk.Button(self.window, text="Write Notes", fg="red", command=partial(write_doc, self))

        read_btn.grid(row=0, column=0)
        cpsrc_btn.grid(row=0, column=1)
        clear_btn.grid(row=1, column=1)
        write_btn.grid(row=0, column=2)

    def run(self):
        self.window.mainloop()