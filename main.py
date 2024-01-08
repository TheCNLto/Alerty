import time
from customtkinter import CTk, CTkTabview, CTkLabel, CTkButton, CTkToplevel, CTkEntry, CTkScrollableFrame, END
from tkinter import BOTH, X, messagebox


class alerty_alert(CTkToplevel):
    def __init__(self, title, about, timed):
        super().__init__()
        self.title(title)
        self.lb1 = CTkLabel(
            master=self,
            text=about
        )
        self.lb1.pack(fill=BOTH, expand=1, padx=20, pady=20)
        self.lb2 = CTkLabel(
            master=self,
            text=timed
        )
        self.lb2.pack(fill=BOTH, expand=1, padx=20)
        self.btn1 = CTkButton(
            master=self,
            text='Clear alert',
            command=self.clearAlert
        )

    def clearAlert(self):
        self.destroy()


class main(CTk):
    def __init__(self):
        super().__init__()
        self.alerts: list = []
        self.title("Alerty")
        self.tabs = CTkTabview(master=self)
        self.create_tab = self.tabs.add("Create")
        # self.exists_tab = self.tabs.add("Exists")
        self.on_going_tab = self.tabs.add("On going")
        self.tabs.pack(fill=BOTH, expand=1)
        self.lb_create_1 = CTkLabel(
            master=self.create_tab,
            text="Title of the alert:"
        )
        self.lb_create_1.pack(fill=BOTH, expand=1)
        self.alert_title = CTkEntry(
            master=self.create_tab,
            height=10,
            placeholder_text='Something...'
        )
        self.alert_title.pack(fill=BOTH, expand=1)
        self.lb_create_about = CTkLabel(
            master=self.create_tab,
            text="Description of the alert:"
        )
        self.lb_create_about.pack(fill=BOTH, expand=1)
        self.alert_about = CTkEntry(
            master=self.create_tab,
            height=10,
            placeholder_text='Some explanation...'
        )
        self.alert_about.pack(fill=BOTH, expand=1)
        self.lb_create_time = CTkLabel(
            master=self.create_tab,
            text="Time of the alert:"
        )
        self.lb_create_time.pack(fill=BOTH, expand=1)
        self.alert_time = CTkEntry(
            master=self.create_tab,
            height=10,
            placeholder_text='Like 14:32'
        )
        self.alert_time.pack(fill=BOTH, expand=1)
        self.alert_create_button = CTkButton(
            text="Create timed alert",
            master=self.create_tab,
            command=self.createTimedAlert,
            corner_radius=50
        )
        self.alert_create_button.pack(fill=BOTH, expand=1, pady=10)
        self.scrollableFrame = CTkScrollableFrame(
            master=self.on_going_tab,
        )
        self.scrollableFrame.pack(fill=BOTH, expand=1)
        self.eval('tk::PlaceWindow . center')
        self.checker()

    def checker(self):
        """current_time = time.localtime()
        current_datetime = datetime.fromtimestamp(time.mktime(current_time))
        new_datetime = current_datetime + timedelta(minutes=1)
        new_time = time.localtime(time.mktime(new_datetime.timetuple()))"""
        for i in self.alerts:
            if i <= time.strftime("%H:%M", time.localtime()):
                alerty_alert(self.alert_title.get(), self.alert_about.get(), i)
                print("time!!!!!")
                self.alerts.remove(i)
        self.after(200, self.checker)

    def createTimedAlert(self):
        # print(len(self.alert_title.get("0.0", "end")))
        try:
            storeTitle, storeAbout, storeTime = self.alert_title.get(), self.alert_about.get(), self.alert_time.get()
            if len(storeTime) < 1 or len(storeTitle) < 1 or len(storeAbout) < 1:
                messagebox.showerror("Error", "You forgot something important!")
            else:
                self.alerts.append(storeTime)
                lbCreated = CTkLabel(
                    master=self.scrollableFrame,
                    text=f"{storeTitle}\n{storeAbout}\n{storeTime}"
                )
                lbCreated.pack(fill=X, expand=0, pady=20)
                self.alert_time.delete(first_index=0, last_index=END)
                self.alert_about.delete(first_index=0, last_index=END)
                self.alert_title.delete(first_index=0, last_index=END)
                self.alert_title.focus()

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
        """finally:
            print(self.exists_tab.winfo_children())"""


app = main()
app.mainloop()
