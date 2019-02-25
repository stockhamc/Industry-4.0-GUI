import tkinter as tk
from tkinter import * # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
# from PIL import Image, ImageTk

class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Industry 4.0 Demo")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, PageOne, Assembly_1, Assembly_1_two, Assembly_1_three, Assembly_1_four, Assembly_Complete, Assembly_2, Assembly_3, Assembly_4, Assembly_5):
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


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.geometry('750x250')
        label = tk.Label(self, text="Industry 4.0 Assembly Demo", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        start_button = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("PageOne"))

        # ==========================================
        # ==========================================
        # Added lines to create a label with a background image
        photo = PhotoImage(file="")
        label1 = Label(self, image=photo)
        label1.image = photo  # keep a reference!
        label1.pack()
        # ==========================================
        # ==========================================

        start_button.config(bg="green", fg="black", width=20)
        start_button.pack(pady=5)

        setup_button = tk.Button(self, text="Setup",
                            command=lambda: controller.show_frame("PageTwo"))
        #setup = PhotoImage(file="setup.PNG")
        setup_button.config(bg="green", fg="black", width=20)
        setup_button.pack(pady=5)

        #button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose an Assembly", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
       # label.grid(row=0, column=0)

        # assembly 1 picture


        assembly_1 = tk.Button(self, text="Assembly 1",
                           command=lambda: controller.show_frame("Assembly_1"))
        assembly_1.pack(side="left", padx=10, pady=10)
       # assembly_1.grid(row=2, column=0, pady=10)

        assembly_2 = tk.Button(self, text="Assembly 2",
                           command=lambda: controller.show_frame("Assembly_2"))
        assembly_2.pack(side="left", padx=10, pady=10)
       # assembly_2.grid(row=2, column=1, pady=10)

        assembly_3 = tk.Button(self, text="Assembly 3",
                           command=lambda: controller.show_frame("Assembly_3"))
        assembly_3.pack(side="left", padx=10, pady=10)
      #  assembly_3.grid(row=2, column=2, pady=10)

        assembly_4 = tk.Button(self, text="Assembly 4",
                           command=lambda: controller.show_frame("Assembly_4"))
        assembly_4.pack(side="left", padx=10, pady=10)
      #  assembly_4.grid(row=2, column=3, pady=10)




class Assembly_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Acquire this part from the designated bin", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        photo = PhotoImage(file="Brick_1x2.PNG")
        label1 = Label(self, image=photo)
        label1.image = photo  # keep a reference!
        label1.pack()

        next_step = tk.Button(self, text="Continue", command=lambda: controller.show_frame("Assembly_1_two"))
        next_step.pack()

        return_button = tk.Button(self, text="Return to the home page", command=lambda: controller.show_frame("StartPage"))
        return_button.pack()


class Assembly_1_two(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Assemble the part like so", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        next_step = tk.Button(self, text="Continue", command=lambda: controller.show_frame("Assembly_1_three"))
        next_step.pack()

        return_button = tk.Button(self, text="Return to the home page", command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_1_three(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Acquire this part from the designated bin", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        photo = PhotoImage(file="Brick_2x2.PNG")
        label1 = Label(self, image=photo)
        label1.image = photo  # keep a reference!
        label1.pack()

        next_step = tk.Button(self, text="Continue", command=lambda: controller.show_frame("Assembly_1_four"))
        next_step.pack()

        return_button = tk.Button(self, text="Return to the home page", command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_1_four(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Assemble the part like so", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        next_step = tk.Button(self, text="Continue", command=lambda: controller.show_frame("Assembly_Complete"))
        next_step.pack()

        return_button = tk.Button(self, text="Return to the home page", command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_Complete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Assembly Complete", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="Thank you for trying the Industry 4.0 Assembly Demo!", font=controller.title_font)
        label2.pack(side="top", fill="x", pady=10)

        return_button = tk.Button(self, text="Return to the home page", command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Acquire this part from the designated bin", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        return_button = tk.Button(self, text="Return to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Acquire this part from the designated bin", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        return_button = tk.Button(self, text="Return to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Acquire this part from the designated bin", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        return_button = tk.Button(self, text="Return to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.pack()

class Assembly_5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Acquire this part from the designated bin", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        return_button = tk.Button(self, text="Return to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()