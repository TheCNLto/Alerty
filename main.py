import time
from tkinter import BOTH, X, messagebox

from customtkinter import CTk, CTkTabview, CTkLabel, CTkButton, CTkToplevel, CTkEntry, CTkScrollableFrame, END
from playsound import playsound

# alert window
class alerty_alert(CTkToplevel):
    def __init__(self, info):
        super().__init__()
        self.minsize(200, 100)
        self.title(info[0])
        self.lb1 = CTkLabel(
            master=self,
            text=info[1]
        )
        self.lb1.pack(fill=BOTH, expand=1, padx=20, pady=20)
        self.lb2 = CTkLabel(
            master=self,
            text=info[2]
        )
        self.lb2.pack(fill=BOTH, expand=1, padx=20)
        self.btn1 = CTkButton(
            master=self,
            text='Clear alert',
            command=self.clearAlert
        )
        self.btn1.pack(fill=BOTH, expand=1)
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        # maybe not working
        self.after(ms=200, func=playsound("alert.mp3"))


    def clearAlert(self):
        self.destroy()

# default main window
class main(CTk):
    def __init__(self):
        super().__init__()
        # stored alert as a list
        self.alerts: list = []
        self.title("Alerty")
        # tabs defined
        self.tabs = CTkTabview(master=self)
        # creation tab
        self.create_tab = self.tabs.add("Create")
        self.lb_create_1 = CTkLabel(
            master=self.create_tab,
            text="Title of the alert:"
        )
        self.alert_title = CTkEntry(
            master=self.create_tab,
            height=10,
            placeholder_text='Something...'
        )
        self.lb_create_about = CTkLabel(
            master=self.create_tab,
            text="Description of the alert:"
        )
        self.alert_about = CTkEntry(
            master=self.create_tab,
            height=10,
            placeholder_text='Some explanation...'
        )
        self.alert_time = CTkEntry(
            master=self.create_tab,
            height=10,
            placeholder_text='Like 14:32'
        )
        self.lb_create_time = CTkLabel(
            master=self.create_tab,
            text="Time of the alert:"
        )
        self.alert_create_button = CTkButton(
            text="Create timed alert",
            master=self.create_tab,
            command=self.createTimedAlert,
            corner_radius=50
        )
        self.tabs.pack(fill=BOTH, expand=1)
        self.lb_create_1.pack(fill=BOTH, expand=1)
        self.alert_title.pack(fill=BOTH, expand=1)
        self.lb_create_about.pack(fill=BOTH, expand=1)
        self.alert_about.pack(fill=BOTH, expand=1)
        self.lb_create_time.pack(fill=BOTH, expand=1)
        self.alert_time.pack(fill=BOTH, expand=1)
        self.alert_create_button.pack(fill=BOTH, expand=1, pady=10)
        # created timers
        self.on_going_tab = self.tabs.add("On going")
        self.scrollableFrame = CTkScrollableFrame(
            master=self.on_going_tab,
        )
        # scrollable frame for easy scroll
        self.scrollableFrame.pack(fill=BOTH, expand=1)
        # update the class for correct sizes
        self.update()
        # prevent collapse
        self.minsize(self.winfo_width(), self.winfo_height())
        # place the window the center of the screen
        self.eval('tk::PlaceWindow . center')
        # time checker (loop starter)
        self.checker()

    def checker(self):
        for i in self.alerts:
            if i[2] <= time.strftime("%H:%M", time.localtime()):
                alerty_alert(i)
                print("time!!!!!")
                self.alerts.remove(i)
        # runs infinitely
        self.after(200, self.checker)

    def createTimedAlert(self):
        try:
            # needed basic information of the alert
            storeTitle, storeAbout, storeTime = self.alert_title.get(), self.alert_about.get(), self.alert_time.get()
            if len(storeTime) < 1 or len(storeTitle) < 1 or len(storeAbout) < 1:
                messagebox.showerror("Error", "You forgot something important!")
            else:
                self.alerts.append(tuple((self.alert_title.get(), self.alert_about.get(), self.alert_time.get())))
                lbCreated = CTkLabel(
                    master=self.scrollableFrame,
                    text=f"{storeTitle}\n{storeAbout}\n{storeTime}"
                )
                lbCreated.pack(fill=X, expand=0, pady=20)
                # after a successful creation clears itself
                self.alert_time.delete(first_index=0, last_index=END)
                self.alert_about.delete(first_index=0, last_index=END)
                self.alert_title.delete(first_index=0, last_index=END)
                self.alert_title.focus()

            # remove button function for expired alerts
            def x1():
                try:
                    self.alerts.remove(storeTime)
                except Exception:
                    pass
                finally:
                    lbCreated.destroy()
                    clearBtn.destroy()

            clearBtn = CTkButton(
                master=self.scrollableFrame,
                command=x1,
                text='Clear'
            )
            clearBtn.pack(fill=X, expand=0)
        except Exception as x:
            messagebox.showerror("Error", str(x))


app = main()
app.mainloop()
