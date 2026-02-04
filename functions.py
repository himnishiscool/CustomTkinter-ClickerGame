import customtkinter as ctk

def upgrade_menu_toggle(menu):
    print("Toggled")

    if menu.winfo_x() == 1080:
        menu.place(
            x=730,
            y=0,
        )
    else:
        menu.place(
            x=1080,
            y=0,
        )