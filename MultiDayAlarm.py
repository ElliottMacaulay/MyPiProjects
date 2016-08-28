




import tkinter as tk
import time
from threading import Thread
import threading
import datetime
from tkinter import ttk


LARGE_FONT= ("verdana", 12)
XL_FONT= ("verdana", 16)


class Clock():
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent):
        """
        Create the clock widget
        It's an ordinary Label element
        """
        self.time = time.strftime('%H:%M:%S')
        self.widget = tkinter.Label(parent, text=self.time)
        self.widget.after(200, self.tick)      # Wait 200 ms, then run tick()


    def tick(self):
        """ Update the display clock """
        new_time = time.strftime('%H:%M:%S')
        if new_time != self.time:
            self.time = new_time
            self.widget.config(text=self.time)
        self.widget.after(200, self.tick)      # 200 =  millisecond delay
                                               #        before running tick() again



class AlarmClock(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (SunPage, MonPage, TuesPage, WedPage, ThursPage, FriPage, SatPage, ControlPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(F)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class SunPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sunday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.time = time.strftime('%H:%M:%S')

        self.widget = tk.Label(self, text=self.time, font=XL_FONT)
        self.widget.pack(pady=10,padx=10)

        self.widget.after(200, self.tick)      # Wait 200 ms, then run tick()




        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.place(x=460+125*0, y=100)

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.place(x=460+125*1, y=100)

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.place(x=460+125*2, y=100)

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.place(x=460+125*3, y=100)

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.place(x=460+125*4, y=100)

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.place(x=460+125*5, y=100)

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.place(x=460+125*6, y=100)

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.place(x=460+125*7, y=100)

        #Rest of the page's code goes here!

        alarmHr = 0
        alarmMin = 0

        alarmLabel = tk.Label(self, text="Alarm Is set for: %d:%d" % (alarmHr, alarmMin), font=LARGE_FONT)
        alarmLabel.place(anchor="c", relx=.5, rely=.3)

        self.decrementButton = ttk.Button(self, text="Test Button", command = lambda: self.decrement("hour"))
        self.decrementButton.place(anchor="c", relx=.5, rely=.5)





    def decrement(self, div):
        if div == "hour":
            if alarmHr == 0:
                alarmHr = 23
            else:
                alarmHr -= 1
            return alarmHr
        else:
            if alarmMin == 0:
                alarmMin = 59
            else:
                alarmMin -= 1
            return alarmMin


    def tick(self):
        """ Update the display clock """
        new_time = time.strftime('%H:%M:%S')
        if new_time != self.time:
            self.time = new_time
            self.widget.config(text=self.time)
        self.widget.after(200, self.tick)      # 200 =  millisecond delay
                                               #        before running tick() again




class MonPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Monday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.time = time.strftime('%H:%M:%S')

        clockContainer = tk.Frame(self)
        self.widget = tk.Label(self, text=self.time, font=LARGE_FONT)
        self.widget.pack(pady=10,padx=10)

        self.widget.after(200, self.tick)      # Wait 200 ms, then run tick()


        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.place(x=460+125*0, y=100)

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.place(x=460+125*1, y=100)

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.place(x=460+125*2, y=100)

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.place(x=460+125*3, y=100)

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.place(x=460+125*4, y=100)

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.place(x=460+125*5, y=100)

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.place(x=460+125*6, y=100)

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.place(x=460+125*7, y=100)

        #Rest of the page's code goes here!






    def tick(self):
        """ Update the display clock """
        new_time = time.strftime('%H:%M:%S')
        if new_time != self.time:
            self.time = new_time
            self.widget.config(text=self.time)
        self.widget.after(200, self.tick)      # 200 =  millisecond delay
                                               #        before running tick() again




class TuesPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tuesday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.pack()

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.pack()

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.pack()

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.pack()

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.pack()

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.pack()

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.pack()

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.pack()

class WedPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wednesday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.pack()

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.pack()

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.pack()

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.pack()

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.pack()

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.pack()

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.pack()

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.pack()

class ThursPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Thursday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.pack()

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.pack()

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.pack()

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.pack()

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.pack()

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.pack()

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.pack()

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.pack()

class FriPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Friday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.pack()

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.pack()

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.pack()

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.pack()

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.pack()

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.pack()

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.pack()

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.pack()

class SatPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Saturday", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.pack()

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.pack()

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.pack()

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.pack()

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.pack()

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.pack()

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.pack()

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.pack()

class ControlPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Controlla", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        SunButton = ttk.Button(self, text="Sunday", command = lambda: controller.show_frame(SunPage))
        SunButton.pack()

        MonButton = ttk.Button(self, text="Monday", command = lambda: controller.show_frame(MonPage))
        MonButton.pack()

        TuesButton = ttk.Button(self, text="Tuesday", command = lambda: controller.show_frame(TuesPage))
        TuesButton.pack()

        WedButton = ttk.Button(self, text="Wednesday", command = lambda: controller.show_frame(WedPage))
        WedButton.pack()

        ThursButton = ttk.Button(self, text="Thursday", command = lambda: controller.show_frame(ThursPage))
        ThursButton.pack()

        FriButton = ttk.Button(self, text="Friday", command = lambda: controller.show_frame(FriPage))
        FriButton.pack()

        SatButton = ttk.Button(self, text="Saturday", command = lambda: controller.show_frame(SatPage))
        SatButton.pack()

        ControlButton = ttk.Button(self, text="Controlla", command = lambda: controller.show_frame(ControlPage))
        ControlButton.pack()







app = AlarmClock()
app.mainloop()
