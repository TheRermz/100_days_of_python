from tkinter import *
import math


# CONSTANTS
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "COURIER"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# TIMER RESET


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# TIMER MECHANISM


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    elif reps % 2 != 0:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

    elif reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)


# COUNTDOWN MECHANISM


def countdown(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# UI SETUP

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
