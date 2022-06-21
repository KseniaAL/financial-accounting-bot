import tkinter as tk
import random
import tkinter.messagebox as tmb
window = tk.Tk()
window.title("Назови цвет")
window.geometry("400x250")
instructions = tk.Label(window, text = "Введите цвет слова, а не слово! Жми Enter, чтобы играть.", font = ("Helvetica", 10))
instructions.place(x=10, y=10)
color_label = tk.Label(window, text = "color", font=("Helvetica", 60))
color_label.place(x=10, y=80)
entry = tk.Entry(window, font=("Helvetica", 10))
entry.place(x=10, y=180)
entry.focus_set()
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple",
          "brown", "white"]
score = 0
fails = 0
time_left = 30
score_label = tk.Label(window, text = f"Правильно: {score}", font = ("Hekvetica", 10))
score_label.place(x=10, y=40)
fails_label = tk.Label(window, text = f"Неправильно: {fails}", font = ("Hekvetica", 10))
fails_label.place(x=10, y=60)
time_label = tk.Label(window, text = f"Оталось секунд: {time_left}")
time_label.place(x=10, y=210)
def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label["text"] = f"Оталось секунд: {time_left}"
        time_label.after(1000, timer)
    else:
        tmb.showinfo("Конец игры - время вышло")
def new_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(colors)
def check(event):
    #print("Проверка")
    global score
    global fails
    if time_left > 0:
        user_color = entry.get()
        word_color = color_label["fg"]
        if user_color == word_color:
            print("Да")
            score += 1
            score_label["text"] = f"Правильно: {score}"
        else:
            print("Нет")
            fails +=1
            fails_label["text"] = f"Неправильно: {fails}"
        new_word()
        entry.delete(0, "end")
    else:
        if score > fails:
            tmb.showinfo("У тебя здорово получается")
        else:
            tmb.showinfo("Давай попробуем еще раз")
new_word()
window.bind("<Return>", check)
#timer()
time_label.after(1000, timer)
window.mainloop()
