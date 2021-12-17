import tkinter as tk
from TopicSuggestions import TopicSuggestions

import requests
from PIL import Image, ImageTk, UnidentifiedImageError
from urllib.request import urlopen
from io import BytesIO
import wikipedia
from WikiRequests import getWikiPageWords
import warnings

warnings.catch_warnings()

warnings.simplefilter("ignore")


def getRidOfReturnsAndSpaces(list):
    for i, s in enumerate(list):
        if s == " ":
            del list[i]
            continue
        if '\n' in s:
            words = s.split('\n')
            list[i] = words[0]
            list.insert(i + 1, words[1])
    return list


# use requests and ImageTk to load data of a .JPG photo
def getPhotoFromUrl(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    r = requests.get(url, stream=True)
    im = Image.open(BytesIO(r.content))
    im.thumbnail((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(im)
    return photo


class TopicEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel
        self.config(bg='black', bd=2, relief=tk.RAISED)

        self.label = tk.Label(self, text="ENTER A TOPIC:", font=(self.parent.typingFont, 14), bg='black', fg='white')
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(self, font=(self.parent.typingFont, 14), bg='black', fg='white', insertbackground='white')
        self.entry.grid(row=1, column=0)

        self.button = tk.Button(self.parent, font=(self.parent.typingFont, 12), text='CHANGE TOPIC!', overrelief=tk.RAISED, wraplength=80)
        self.button.place(relx=1.0, rely=0.0, x=-40, y=12, anchor="ne")

        self.suggestions = TopicSuggestions(self)
        self.suggestions.grid(row=2, column=0)

        self.img1 = None
        self.img2 = None

        self.update_self()
        self.button.bind("<Button-1>", self.buttonClicked)

    def buttonClicked(self, key):
        phrase = self.entry.get()
        self.entry.delete(0, tk.END)
        self.label.config(text='loading...')
        self.update()
        title = phrase
        new_words = getWikiPageWords(phrase).split(' ')
        self.parent.newTopicReset(new_words)
        self.label.config(text=title)
        self.button.config(relief=tk.RAISED)

    def createImages(self, page):
        urls = []
        url_index = 0
        while len(urls) < 4:
            if page.images[url_index][-4:].lower() == '.jpg':
                urls.append(page.images[url_index])
            url_index += 1
        photos = []
        for url in urls:
            try:
                photos.append(getPhotoFromUrl(url))

            except:
                print('Did not work')

        self.img1 = tk.Label(self.parent, image=photos[0])
        self.img1.image = photos[0]
        self.img1.place(relx=1.0, rely=1.0, x=-120, y=-30, anchor="se")

        self.img2 = tk.Label(self.parent, image=photos[1])
        self.img2.image = photos[1]
        self.img2.place(relx=0.0, rely=1.0, x=120, y=-30, anchor="sw")

    def update_self(self):
        self.widgetModel.current_topic_input = self.entry.get()
        # if not self.widgetModel.started and self.label.cget('text') != 'ENTER A TOPIC:':
        #     print('triggered')
        #     self.label.config(text='No Topic.')
        #     self.update()
        self.parent.parent.after(100, self.update_self)


