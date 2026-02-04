import customtkinter as ctk
from functions import *

# --- Constants ---
ctk.set_appearance_mode("dark")

MENU_WIDTH = 350

ROOT_FG = "#181711"
BUTTON_FG = "#4381C1"
BUTTON_HOVER = "#3870A8"
BORDER_COLOR = "#191919"

# --- Window ---
root = ctk.CTk()
root.geometry("1080x2400")
root.title("Clicker Game")
root.configure(
    fg_color="#191919",
)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# --- Main button ---
clicker_button = ctk.CTkButton(
    root,
    text="Click Me!!!",
    fg_color=BUTTON_FG,
    hover_color=BUTTON_HOVER,
    font=("SF Display", 100),
)
clicker_button.grid(
    row=1,
    column=1,
)

# --- Upgrades menu ---
upgrades_menu = ctk.CTkScrollableFrame(
    root,
    width=MENU_WIDTH,
    height=2400,
    fg_color=BUTTON_HOVER,
)
upgrades_menu.place(
    x=1080,  # start offscreen
    y=0
)

hamburger_button = ctk.CTkButton(
    root,
    width=100,
    height=100,
    text="☰",
    fg_color=BUTTON_FG,
    hover_color=BUTTON_HOVER,
    font=("SF Display", 100),
    command=upgrade_menu_toggle(upgrades_menu),
)
hamburger_button.grid(
    row=0,
    column=0,
)

autoclickUpgrade = ctk.CTkButton(
    upgrades_menu,
    width=200,
    fg_color=BUTTON_FG,
    hover_color=BUTTON_HOVER,
)
autoclickUpgrade.pack(pady=20, padx=20)


print(upgrades_menu.winfo_x())
root.mainloop()
