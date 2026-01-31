import customtkinter as ctk

# --- Constants ---
ctk.set_appearance_mode("dark")
root_fg = "#181711"
upgrade_button_fg = "#4381C1"
upgrade_button_hover = "#3870A8"
clicker_buton_fg = "#4381C1"
clicker_buton_hover = "#3870A8"
border_color = "#191919"

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
    fg_color=clicker_buton_fg,
    hover_color=clicker_buton_hover,
    font=("SF Display", 100),
)
clicker_button.grid(
    row=1,
    column=1,
)

# --- Upgrades menu ---
upgrades_menu = ctk.CTkScrollableFrame(
    root,
    fg_color=upgrade_button_hover,
)
upgrades_menu.grid(
    row=0,
    column=2,
)

autoclickUpgrade = ctk.CTkButton(
    upgrades_menu,
    width=200,
    fg_color=upgrade_button_fg,
    hover_color=upgrade_button_hover,
)
autoclickUpgrade.pack()

root.mainloop()
