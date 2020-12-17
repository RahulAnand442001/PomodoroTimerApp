from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
GREEN = "#335d2d"
YELLOW = "#f7f5dd"
WHITE = "#fff"
BLUE = "#120078"
BROWN = "#290001"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    pomodoro_label.config(fg=GREEN, text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # required time in seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        pomodoro_label.config(fg=RED, text="LONG BREAK ")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        pomodoro_label.config(fg=BROWN, text="SHORT BREAK ")
    else:
        countdown(work_sec)
        pomodoro_label.config(fg=BLUE, text="WORK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_minute = floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        marks = ""
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks = "✔"
        checkmark.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# heading
pomodoro_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
pomodoro_label.grid(column=1, row=0, )
# canvas containing image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=2)
# buttons
start_btn = Button(text="START", command=start_timer, bg=WHITE, borderwidth=0, font=(FONT_NAME, 15, "bold"))
start_btn.grid(column=0, row=3, padx=10, pady=5)
reset_btn = Button(text="RESET", command=reset_timer, bg=WHITE, borderwidth=0, font=(FONT_NAME, 15, "bold"))
reset_btn.grid(column=2, row=3, padx=10, pady=5)
# checkmark
checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=4)
# continue to open window until clicking on exit
window.mainloop()
