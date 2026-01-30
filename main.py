import customtkinter as ctk
from PIL import Image

# --- Window ---
root = ctk.CTk()
root.geometry("1280x720")
root.title("Clicker Game")
root.configure(fg_color="#191919")

# --- Grid layout ---
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=0)

base_potato = Image.open("potato.png")
animating = False

# --- Button Animation ---
def click_animation():
    global animating
    animating = True

    current_width = main_button.winfo_width()
    current_height = main_button.winfo_height()

    shrink_width = int(current_width * 0.9)
    shrink_height = int(current_height * 0.9)

    small_image = ctk.CTkImage(light_image=base_potato, dark_image=base_potato,
                               size=(shrink_width, shrink_height))
    main_button.configure(image=small_image, width=shrink_width, height=shrink_height)

    def restore():
        global animating
        animating = False
        # restore using the current resized potato image
        main_button.configure(image=potato_image, width=current_width, height=current_height)

    root.after(50, restore)

def resize_potato(event):
    global potato_image
    if animating:
        return  # skip resizing while animating

    size = min(event.width, event.height)
    size = max(150, min(size, 600))

    potato_image = ctk.CTkImage(light_image=base_potato, dark_image=base_potato, size=(size, size))
    main_button.configure(image=potato_image, width=size, height=size)


# --- Center container ---
center_frame = ctk.CTkFrame(root, fg_color="transparent")
center_frame.bind("<Configure>", resize_potato)
center_frame.grid(row=0, column=1, sticky="nsew")

center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(0, weight=1)

# --- Initial potato image ---
potato_image = ctk.CTkImage(
    light_image=base_potato,
    dark_image=base_potato,
    size=(250, 250)
)

# --- Main button ---
main_button = ctk.CTkButton(
    center_frame,
    image=potato_image,
    text="",
    fg_color="transparent",
    hover_color="#191919",
    border_width=0,
    corner_radius=0,
    command=click_animation
)
main_button.grid(row=0, column=0)

# --- Upgrades menu ---
upgrades_menu = ctk.CTkScrollableFrame(
    root,
    width=225,
    fg_color="#191919"
)
upgrades_menu.grid(row=0, column=2, sticky="ns")

root.mainloop()
