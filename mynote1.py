import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import askstring
#from tkinter.messagebox import askokcancel
import datetime

  
class Notepad: 
  
    __root = Tk() 
  
    # default window width and height 
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFormatMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFontMenu=Menu(__thisFormatMenu, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
      
    # To add scrollbar 
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
    __target = ''

  
    def __init__(self,**args): 
  
        # Set icon 
##        try: 
##                self.__root.wm_iconbitmap("Notepad.ico")  
##        except: 
##                pass
  
        # Set window size (the default is 300x300) 
  
        try: 
            self.__thisWidth = args['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = args['height'] 
        except KeyError: 
            pass
  
        # Set the window text 
        self.__root.title("Untitled - MyNote") 
  
        # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
  
        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
        # Add controls (widget) 
        self.__thisTextArea.grid(sticky = N + E + S + W) 
          
        # To open new file 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)     
          
        # To open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
          
        # To save current file 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)
        self.__thisFileMenu.add_command(label="Saveas", 
                                        command=self.__saveasFile) 
  
        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
        # To give a feature of cut  
        self.__thisEditMenu.add_command(label="Cut",accelerator="ctrl+x", 
                                        command=self.__cut)              
      
        # to give a feature of copy     
        self.__thisEditMenu.add_command(label="Copy",accelerator="ctrl+c", 
                                        command=self.__copy)          
          
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste",accelerator="ctrl+v", 
                                        command=self.__paste)
        self.__thisEditMenu.add_command(label="Delete",accelerator="del", 
                                         command=self.delete)
        
        
        self.__thisEditMenu.add_separator()
        self.__thisEditMenu.add_command(label="Date", 
                                         command=self.date)
        
          
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        #format menu

##        self.__thisFormatMenu.add_command(label="Font", 
##                                        command=self.font)
        self.__thisFormatMenu.add_command(label="Bold", 
                                        command=self.bold)
        self.__thisFormatMenu.add_command(label="Underline", 
                                        command=self.underline)
        self.__thisFormatMenu.add_command(label="Italic", 
                                        command=self.italic)
        self.__thisMenuBar.add_cascade(label="Format", 
                                       menu=self.__thisFormatMenu)
        #submenu

        self.__thisFormatMenu.add_cascade(label="Font", 
                                        menu=self.__thisFontMenu)
        self.__thisFontMenu.add_command(label="TimesNewRoman",
                                        command=self.timesnewroman)
        self.__thisFontMenu.add_command(label="Algerian",
                                        command=self.algerian)
        self.__thisFontMenu.add_command(label="Berlin Sans FB Demi",
                                        command=self.berlinSansFBDemi)
        self.__thisFontMenu.add_command(label="Chiller",
                                        command=self.chiller)
        self.__thisFontMenu.add_command(label="Forte",
                                        command=self.forte)
        # To create a feature of description of the notepad 
        self.__thisHelpMenu.add_command(label="About Notepad", 
                                        command=self.__showAbout)  
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu) 
  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
        # Scrollbar will adjust automatically according to the content         
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
      
          
    def __quitApplication(self): 
        self.__root.destroy() 
        # exit() 
  
    def __showAbout(self): 
        showinfo("Notepad","Best Text Editor") 
  
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
            # Try to open the file 
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - Notepad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Notepad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
  
    def __saveFile(self): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close()
    def __saveasFile(self): 
  
        
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
           
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>")

    def delete(self):
      
        if self.__thisTextArea.tag_ranges(SEL):
            self.__thisTextArea.delete(SEL_FIRST, SEL_LAST)
    def date(self):

        data = datetime.date.today()

        self.__thisTextArea.insert(INSERT,data)

    def timesnewroman(self):
        self.__thisTextArea.config(font = ("TimesNewRoman", 10))

          
    def algerian(self):
        self.__thisTextArea.config(font = ("Algerian", 10))

        
    def berlinSansFBDemi(self):
        self.__thisTextArea.config(font = ("BerlinSansFBDemi", 10))
        
    def chiller(self):
        self.__thisTextArea.config(font = ("Chiller", 10))

        
    def forte(self):
        self.__thisTextArea.config(font = ("Forte", 10))

    def bold(self):
        self.__thisTextArea.config(font = ("Arial", 10, "bold"))

    def underline(self):

        self.__thisTextArea.config(font = ("Arial", 10, "underline"))

##    def find(self):
##        self.__target = askstring('Notepad', 'Search String?',
##                                initialvalue=self.__target)
##        if self.__target:
##            where = self.__thisTextArea.search(self.__target, INSERT, END, nocase=True)
##            if where:
##                print(where)
##                self.__thisTextArea.tag_remove(SEL, '1.0', END)
##                pastit = '{}+{}c'.format(where, len(self.__target))
##                self.__thisTextArea.tag_add(SEL, where, pastit)
##                self.__thisTextArea.mark_set(INSERT, pastit)
##                self.__thisTextArea.see(INSERT)
##                self.__thisTextArea.focusset()

    def find(self):
        self.__target = simpledialog.askstring('Notepad', 'Search String?',
                                initialvalue=self.__target)
        if self.__target:
            where = self.__thisTextArea.search(self.__target, INSERT, END, nocase=True)
            if where:
                pastit = '{}+{}c'.format(where, len(self.__target))
                self.__thisTextArea.tag_add(SEL, where, pastit)
                self.__thisTextArea.mark_set(INSERT, pastit)
                self.__thisTextArea.see(INSERT)
                self.__thisTextArea.focus()


  
    def italic(self):

        self.__thisTextArea.config(font = ("Arial",10,"italic"))

    


  
    def run(self): 
  
        # Run main application 
        self.__root.mainloop() 
  
  
  
  
# Run main application 
notepad = Notepad(width=600,height=400) 
notepad.run() 
