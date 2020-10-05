from tkinter import *
import time
from src.Chatbots.GetStoryFromFile import getstorylines_from_file
import tkinter.messagebox
from src.Chatbots.NLPTokensGeneration import NLPTokens
import pyttsx3
import threading
from src.Chatbots.MainChatbotFile import Chatbot
saved_username = ["You"]
window_size="400x400"

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.botclass = Chatbot() # calling bot class

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)

        # File Menu -Top bar
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        file.add_command(label="Clear Chat", command=self.clear_chat)
        file.add_command(label="Exit",command=self.chatexit)
        # Help option - Top bar
        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        help_option.add_command(label="About Chatbot", command=self.msg)
        help_option.add_command(label="Developer", command=self.about)


        # canvas = Canvas(self, width=150, height=150)
        # canvas.pack()
        # img=ImageTk.PhotoImage(Image.open('chatbot.png'))
        # #img = PhotoImage(Image.open("chatbot.png"))
        # canvas.create_image(10, 10, anchor=NW, image=img)

        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#2263E7",
                                  activeforeground="#2263E7")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)
        
        self.last_sent_label(date="No messages sent.")
        

    def playResponce(self,responce):
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')

    def last_sent_label(self, date):

        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("Chatbot AI SP17-BCS-012",'Story Title: A Good Boy')

    def about(self):
        tkinter.messagebox.showinfo("Chatbot AI Project","Asad Haroon")
    
    def send_message_insert(self, message):

        user_input = self.entry_field.get()
        if user_input!='': # if input message is not empty string then.
            pr1 = "Me : " + user_input + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr1)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.botconversation=self.botclass.conversation(user_input)
            pr="Chatbot : " + self.botconversation + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)
            t2 = threading.Thread(target=self.playResponce, args=(self.botconversation,))
            t2.start()

    def font_change_default(self):
        self.text_box.config(font="Verdana 10")
        self.entry_field.config(font="Verdana 10")
        self.font = "Verdana 10"

    def color_theme_default(self):
        self.master.config(bg="#EEEEEE")
        self.text_frame.config(bg="#EEEEEE")
        self.entry_frame.config(bg="#EEEEEE")
        self.text_box.config(bg="#FFFFFF", fg="#000000")
        self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
        self.send_button_frame.config(bg="#EEEEEE")
        self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        #self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.sent_label.config(bg="#EEEEEE", fg="#000000")

        self.tl_bg = "#FFFFFF"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
    

    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()    

if __name__=='__main__':

    root=Tk()
    getstorylines_from_file() # first initialize file with content
   # print("Tokens are: ")
    NLPTokens().gen_tokens()  # print tokens
    a = ChatInterface(root)
    root.geometry(window_size)


    root.title("AI Chatbot SP17-BCS-012")
    root.iconbitmap('icon.ico')
    root.mainloop()
    #NLPTokens.delete_graph()




