import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='supermarket', size=24, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, skills, page1, page1_1, page1_2, castcoach, castcoach2, entertain, page2, page2_1, page2_2, page2_3, page2_4, page3, page3_1, page3_2, page3_3, page3_4, page3_5, page4, page4_1, page4_2, page4_3, page4_4, caster, caster2, proplayer, gameanalyst, gameanalyst2, youtuber, coach, creator, marketing, consultant, journalist, broadcaster, lawyer, emanager, admin, manager, stop):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def openweb():
        webbrowser.open(url,new=new)
        url = "https://projectpsitpage1.firebaseapp.com/"

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like to play games?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Yes",
                            command=lambda: controller.show_frame("page1"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page2"))
        button1.pack()
        button2.pack()


class skills(tk.Frame):#-What do you specialize in?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="What do you specialize in?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Medium Skill",
                           command=lambda: controller.show_frame("page1"))
        button2 = tk.Button(self, text="High Skill",
                            command=lambda: controller.show_frame("manager"))
        button.pack()
        button2.pack()


class page1(tk.Frame):#-Are you good at playing games?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="What would you like to do?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Playing",
                           command=lambda: controller.show_frame("page1_1"))
        button2 = tk.Button(self, text="Analyzing",
                            command=lambda: controller.show_frame("page1_2"))
        button.pack()
        button2.pack()


class page1_1(tk.Frame):#-You want to be a pro player?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="You want to be a pro player?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("proplayer"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page1_2"))
        button.pack()
        button2.pack()


class page1_2(tk.Frame):#-an you analyze the games you play?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Can you analyze the games you play?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("castcoach"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("castcoach2"))
        button.pack()
        button2.pack()

class castcoach(tk.Frame):#-an you analyze the games you play?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Can you cast a game?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("gameanalyst"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("coach"))
        button.pack()
        button2.pack()


class castcoach2(tk.Frame):#-an you analyze the games you play?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Can you cast a game?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("entertain"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("stop"))
        button.pack()
        button2.pack()


class entertain(tk.Frame):#-Can you entertain to an audience?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Can you entertain to an audience?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("youtuber"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("stop"))
        button.pack()
        button2.pack()


class page2(tk.Frame):#-How creative are you?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="How creative are you?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Highly creative",
                           command=lambda: controller.show_frame("page2_1"))
        button2 = tk.Button(self, text="Less creative",
                            command=lambda: controller.show_frame("page2_1"))
        button.pack()
        button2.pack()


class page2_1(tk.Frame):#-Do you like talking?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like talking?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("page2_2"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page3"))
        button.pack()
        button2.pack()

class page2_2(tk.Frame):#-Do you like talking to an audience to have fun?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like talking to an audience to have fun?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("caster2"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page2_3"))
        button.pack()
        button2.pack()


class page2_3(tk.Frame):#-Do you like the analysis in detail?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like the analysis in detail?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("gameanalyst2"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page2_4"))
        button.pack()
        button2.pack()


class page2_4(tk.Frame):#-Do you like creating knowledge videos?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like creating knowledge videos?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("creator"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page3"))
        button.pack()
        button2.pack()


class page3(tk.Frame):#-Do you specialize in economics?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you specialize in economics?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("page3_1"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page3_1"))
        button.pack()
        button2.pack()


class page3_1(tk.Frame):#-Do you like marketing?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like marketing?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("marketing"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page3_2"))
        button.pack()
        button2.pack()


class page3_2(tk.Frame):#-Do you specialize in consulting?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you specialize in consulting?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("consultant"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page3_3"))
        button.pack()
        button2.pack()


class page3_3(tk.Frame):#-Do you like working in social media?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like working in social media?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("page3_4"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page4"))
        button.pack()
        button2.pack()


class page3_4(tk.Frame):#-Do you like to writing and finding news?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like to writing or finding news?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("journalist"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page3_5"))
        button.pack()
        button2.pack()

class page3_5(tk.Frame):#-Do you like being behind the camera and controlling the broadcast?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like being behind the camera and controlling the broadcast?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("broadcaster"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page4"))
        button.pack()
        button2.pack()


class page4(tk.Frame):#-Do you specialize in law?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you specialize in law?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("lawyer"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page4_1"))
        button.pack()
        button2.pack()


class page4_1(tk.Frame):#-Do you have responsibility?

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you have responsibility?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("lawyer"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("stop"))
        button.pack()
        button2.pack()


class page4_2(tk.Frame):#-Do you like organizing or planning various events?
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like organizing or planning various events?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("emanager"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page4_3"))
        button.pack()
        button2.pack()


class page4_3(tk.Frame):#-Do you like to managing the game system and managing cheated players?
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like to managing the game system and managing cheated players??", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("admin"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("page4_4"))
        button.pack()
        button2.pack()

class page4_4(tk.Frame):#-Do you like to build your own Esports team?
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Do you like to build your own Esports team?", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Yes",
                           command=lambda: controller.show_frame("manager"))
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("stop"))
        button.pack()
        button2.pack()



""" Careers in Esports Industry """
class caster(tk.Frame):#-Suggested Career is Shoutcaster

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Shoutcaster", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class caster2(tk.Frame):#-Suggested Career is Game analyste

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Coach", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class proplayer(tk.Frame):#-Suggested Career is Pro Player

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Pro Player", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class gameanalyst(tk.Frame):#-Suggested Career is Game analyste

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Game analyst", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class gameanalyst2(tk.Frame):#-Suggested Career is Game analyste

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Game analyst", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class youtuber(tk.Frame):#-Suggested Career is Game analyste

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Gaming Youtuber", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class coach(tk.Frame):#-Suggested Career is Game analyste

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Coach", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class creator(tk.Frame):#-Suggested Career is Content Creator

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Content Creator", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class marketing(tk.Frame):#-Suggested Career is Marketing Executive

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Marketing Executive", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class consultant(tk.Frame):#-Suggested Career is Consultant

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Consultant", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class journalist(tk.Frame):#-Suggested Career is Esports Journalist

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Esports Journalist", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class broadcaster(tk.Frame):#-Suggested Career is Broadcaster

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Broadcaster", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class lawyer(tk.Frame):#-Suggested Career is Esports Lawyer

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Esports Lawyer", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class emanager(tk.Frame):#-Suggested Career is Event Manager

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Event Manager", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class admin(tk.Frame):#-Suggested Career is Admin/Referee

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Admin/Referee", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class manager(tk.Frame):#-Suggested Career is Team Manager

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Suggested Career is Team Manager", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class stop(tk.Frame):#-Suggested Career Farmer

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Maybe you are not suitable for this  Esports industry", font="supermarket")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.title("Careers in Esports")
    app.iconbitmap('icon123.ico')
    app.mainloop()