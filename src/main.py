from tkinter import *
from tkinter import ttk
from color import *
from tkinter import filedialog as fd
from mod import modify

class app():

    def __init__(self,wn):

        self.window = wn

        #window config
        self.window.geometry("400x230")
        self.window.config(bg = tbox)
        self.window.title("mp3 tagger")
        self.window.resizable(False, False)

        self.fn = "" #file path



        #menus
        self.menubar = Menu(self.window)
        self.file_menu = Menu(self.menubar, tearoff = 0)
        self.file_menu.add_command(label = "Open File",command = self.get_file)
        self.menubar.add_cascade(label = "File", menu = self.file_menu)

        self.window.config(menu = self.menubar)

        #frames
        self.f1 = Frame(self.window,bg = bgs, width = 380, height = 210)
        self.f2 = Frame(self.window,bg = bgs, width = 380, height = 210)

        self.f2.place(x = 10, y = 10)
        self.f1.place(x = 10, y = 10)

        #deploy frames
        self.single_file_edit(self.f2)
        self.main_menu(self.f1)






        self.f1.tkraise()


    def swap(self,frame):
        frame.tkraise()


    def single_file_edit(self,frame): #utils for single file edit

        #labels

        self.lfile_name = Label(frame, bg = bgs, fg = fonts,
                          text = "File name:")
        self.ltitle = Label(frame, bg = bgs, fg = fonts, text = "Title:")
        self.lartist_name = Label(frame, bg = bgs, fg = fonts, text = "Artist:")
        self.lalbum = Label(frame, bg = bgs, fg = fonts, text = "Album:")
        self.lnumber = Label(frame, bg = bgs, fg = fonts, text = "Number:")

        #entrys

        self.file_name = Entry(frame, bg = tbox, fg = fonts, bd = 1,
                        width = 26)
        self.title = Entry(frame, bg = tbox, fg = fonts, bd = 1,
                        width = 26)
        self.artist_name = Entry(frame, bg = tbox, fg = fonts, bd = 1,
                        width = 26)
        self.album = Entry(frame, bg = tbox, fg = fonts, bd = 1, width = 26)

        self.number = Spinbox(frame, bg = tbox, width = 4, increment = 1,
                        from_ = 1, to = 9999, bd = 1, fg = fonts)

        #buttons

        self.b1 = Button(self.f2, width = 7, height = 2, text = "<--",
                    command = lambda: self.swap(self.f1), fg = bgs2, bg = bgs,
                    bd = 0)

        self.edit = Button(self.f2, width = 12, height = 2, text = "Edit",
                    fg = fonts, bg = bgs, command = lambda:
                    self.mod_file(self.fn,self.get_changes_sf()))




        #widget locations

        self.file_name.place(x = 200, y = 20)
        self.title.place(x = 200, y = 70)
        self.artist_name.place(x = 200, y = 120)
        self.album.place(x = 200, y = 170)
        self.number.place(x = 80 , y = 120)

        self.lfile_name.place(x = 135, y = 20)
        self.ltitle.place(x = 135, y = 70)
        self.lartist_name.place(x = 135, y = 120)
        self.lalbum.place(x = 135, y = 170)
        self.lnumber.place(x = 15, y = 120)

        self.b1.place(x = 0, y = 0)
        self.edit.place(x = 20, y = 160)


    def main_menu(self,frame): #main menu widgets

        self.b2 = Button(self.f1, width = 7,height = 2, text = "swap to 2",
                  command = lambda: self.swap(self.f2))


        self.b2.place(x = 40,y = 60)




    def get_file(self):
        self.fn = fd.askopenfilename()


    def get_changes_sf(self): #for single file

        return [self.file_name.get(),
                self.title.get(),
                self.artist_name.get(),
                self.album.get(),
                self.number.get()]


    def mod_file(self, path, changes):

        try:    #test if there is a file loaded
            modify(path, changes[0], changes[1],
                changes[2], changes[3], changes[4])

        except:
            print("No file selected")


root = Tk()
editor = app(root)






root.mainloop()
