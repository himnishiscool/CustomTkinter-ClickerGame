import customtkinter as ctk

# --- Constants ---
ctk.set_appearance_mode("dark")

ROOT_FG = "#181711"
BUTTON_FG = "#4381C1"
BUTTON_HOVER = "#3870A8"
BORDER_COLOR = "#191919"

# --- Other Variables ---
upgrades_menu_visible = False

# --- Window ---
root = ctk.CTk()
root.geometry("1080x2400")
root.title("Clicker Game")
root.configure(
    fg_color=ROOT_FG,
)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# --- Functions ---
def upgrades_menu_toggle():
    global upgrades_menu_visible

    if upgrades_menu_visible:
        upgrades_menu.place_forget()
        upgrades_menu_visible = False
    else:
        upgrades_menu.place(
            x=730,
            y=0
        )
        upgrades_menu_visible = True

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
    width=350,
    height=2400,
    fg_color=BUTTON_HOVER,
)
upgrades_menu.place(
    x=730,
    y=0
)

hamburger_button = ctk.CTkButton(
    root,
    width=120,
    height=100,
    text="☰",
    fg_color=BUTTON_FG,
    hover_color=BUTTON_HOVER,
    font=("SF Display", 100),
    command=upgrades_menu_toggle,
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
