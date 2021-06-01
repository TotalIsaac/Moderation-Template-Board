from codecs import BOM_UTF16
from tkinter import *
import yaml

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultRelief = self["relief"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['relief'] = RIDGE

    def on_leave(self, e):
        self['relief'] = self.defaultRelief


def copy_button(template):
    """Clears the current clipboard and appends a new template"""
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(template)
    r.destroy()


def lang_button_setup(templates, language, frm_copy, frm_lang):
    """Draws copy and language buttons with the associated language. Also used to initialise"""
    
    copy_button_setup(templates, language, frm_copy)

    lang = ['EN', 'RU', 'BR', 'TH', 'DE', 'FR', 'ES', 'KR']
    pad = (6, 1)
    col = 0

    for i in range(8):
        row = i
        
        if i > 3:
            col = 1
            row -= 4
            pad = (1, 1)

        if lang[i] == language:
            btn = Button(frm_lang, text=lang[i], width=5, relief=SUNKEN, 
                        state='disabled', background='grey70', borderwidth=2)
        else:
            btn = HoverButton(frm_lang, text=lang[i], width=5, relief=GROOVE,
                        command=lambda k=lang[i]: lang_button_setup(templates, k, frm_copy, frm_lang))
        
        btn.grid(row=row, column=col, padx=pad, pady=1, sticky="NSEW")


def copy_button_setup(templates, language, frame):
    for r in range(4):
        for c in range(5):
            rowcol = 'R' + str(r) + str(c)
            btn = HoverButton(frame, activebackground='green', text=templates[rowcol]['title'], 
                        width=15, relief=GROOVE, background=templates[rowcol]['color'],
                        command=lambda rowcol=rowcol: copy_button(templates[rowcol][language]))
            btn.grid(row=r, column=c, padx=1, pady=1, sticky='NSEW')


def start():
    with open("Templates_chat.yaml", 'r', encoding="utf-8") as stream:
        templates = yaml.safe_load(stream)

    root = Tk()
    root.title("Chat Templates")
    root.geometry('960x150')
    root.config(bg="skyblue")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frm_copy = Frame(root, borderwidth=2)
    frm_copy.grid(row=0, column=0, sticky='NSEW')

    frm_lang = Frame(root, borderwidth=2)
    frm_lang.grid(row=0, column=1, sticky='NSEW')

    #Copy Button Grid
    frm_copy.grid_rowconfigure(0, weight=1) #Row
    frm_copy.grid_rowconfigure(1, weight=1)
    frm_copy.grid_rowconfigure(2, weight=1)
    frm_copy.grid_rowconfigure(3, weight=1)
    frm_copy.grid_columnconfigure(0, weight=1) #Column
    frm_copy.grid_columnconfigure(1, weight=1)
    frm_copy.grid_columnconfigure(2, weight=1)
    frm_copy.grid_columnconfigure(3, weight=1)
    frm_copy.grid_columnconfigure(4, weight=1)

    #Language Button Grid
    frm_lang.grid_rowconfigure(0, weight=1) #Row
    frm_lang.grid_rowconfigure(1, weight=1)
    frm_lang.grid_rowconfigure(2, weight=1)
    frm_lang.grid_rowconfigure(3, weight=1)
    frm_lang.grid_columnconfigure(0, weight=1) #Column
    frm_lang.grid_columnconfigure(1, weight=1)

    #Language and copy button initial setup
    lang_button_setup(templates, 'EN', frm_copy, frm_lang)

    root.mainloop()

if __name__ == '__main__':
    start()

