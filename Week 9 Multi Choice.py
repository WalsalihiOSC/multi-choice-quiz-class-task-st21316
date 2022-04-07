

from tkinter import *


class Multi_Choice:
    def __init__(self, parent):
        self.v = StringVar()
        self.v.set("0")
        f1 = Frame(parent)
        label_que = Label(parent, text="Question:", pady=3, padx=10)
        label_que.grid(row=1, column=1)
        self.q = Quize()
        label_question = Label(parent, text=self.q.question, pady=3, padx=3)
        label_question.grid(row=1, column=2)

        self.ans_list = self.q.choices
        self.ans_rb = []
        for i in range(len(self.ans_list)):
            self.ans_rb.append(Radiobutton(
                f1, text=self.ans_list[i], value=self.ans_list[i], variable=self.v, padx=3, pady=2, command=self.show_result))

            self.ans_rb[i].grid(rowspan=4, column=2)
            f1.grid(row=2, column=2)

        self.label_result = Label(parent, text="")
        self.label_result.grid(row=6, column=2)

    def show_result(self):
        if self.q.check_answer(self.v.get()) == True:
            self.label_result.configure(text="Correct!", bg="yellow")
        else:
            self.label_result.configure(text="Incorrect!", bg="Red")


class Quize:
    def __init__(self):
        self.question = "What is the capital of Mongolia?"
        self.choices = ["Vladivostok", "Anstana", "Ulan Bator", "Lhasa"]

    def check_answer(self, answer):
        if answer == "Ulan Bator":
            return True
        return False


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Multi Choice")
    root.geometry("300x300")

    question = Multi_Choice(root)
    root.mainloop()
