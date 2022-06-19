from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#00FF00"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
# WORK_MIN = 1
# SHORT_BREAK_MIN = 2
# LONG_BREAK_MIN = 5
reps = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def starter_time():
    global reps
    reps += 1

    if reps >= 9:
        reset()
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        coundown(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        coundown(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="Work", fg=GREEN)
        coundown(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def coundown(count):
    t_min = math.floor(count / 60)
    t_sec = count % 60

    if t_sec < 10:
        t_sec = f"0{t_sec}"
    canvas.itemconfig(canvas_text, text=f"{t_min}:{t_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, coundown, count - 1)

    else:
        starter_time()
        global reps
        if reps == 2:
            check_mark.config(text="✔")
        elif reps == 4:
            check_mark.config(text="✔✔")
        elif reps == 8:
            check_mark.config(text="✔✔✔")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 122, image=img)
canvas_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35), fill="white")
canvas.grid(row=2, column=2)

start_button = Button(text="Start", command=starter_time)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=3, column=3)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(row=1, column=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=4, column=2)

window.mainloop()
