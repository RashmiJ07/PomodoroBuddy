from tkinter import *
import random
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2#5
SHORT_BREAK_MIN = 1#5
LONG_BREAK_MIN = 3#0
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text='Timer')
    check_mark_label.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    # count_down(5)
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if REPS % 8 == 0:
        timer_label.config(text='Break!',foreground=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer_label.config(text='Break!',foreground=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text='Work!',foreground=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# import time
#
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

# As we already have our mainloop implemented ie. the loop for the GUI that keeps on checking if something is
# happening or not if we add one more loop with similar fashion our program won't function as our loop won't be able
# to reach to our mail loop

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds == 0:
        seconds = '00'
    elif seconds < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += '✔'

        check_mark_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', foreground=GREEN, font=(FONT_NAME, 50, 'bold'), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check_mark_label.grid(column=1, row=3)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
rest_button = Button(text='Reset', highlightthickness=0,command=reset_timer)
rest_button.grid(column=2, row=2)

window.mainloop()
