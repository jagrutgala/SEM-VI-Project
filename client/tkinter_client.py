import tkinter as tk
import requests

class InputField:
    def __init__(self, master, input_type, label, **input_kwargs) -> None:
        self.in_label = tk.Label(master, text=label)
        self.input = input_type(master, input_kwargs)

    def pack(self):
        self.in_label.pack()
        self.input.pack()

class App():
    def __init__(self, master) -> None:
        self.topic_clicked = tk.StringVar()
        self.topic = tk.OptionMenu( master , self.topic_clicked , *requests.get(f"http://127.0.0.1:5000/available topics").json())
        self.topic.pack()

        self.type_clicked = tk.IntVar()
        self.type = tk.OptionMenu( master , self.topic_clicked, *[""])
        self.type.pack()

        self.noq = tk.Spinbox(master, from_=1)
        self.noq.pack()

        self.ll = tk.Spinbox(master, from_=1)
        self.ll.pack()

        self.ul = tk.Spinbox(master, from_=2)
        self.ul.pack()

if __name__ == "__main__":
    # Code Here
    root = tk.Tk()
    app = App(root)
    root.mainloop()
