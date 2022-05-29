from tkinter import Button

def change_default_theme(custom):
    default = {
        'width': '15',
        'height': '2',
        'bg': '#0f0505',
        'fg': '#ffffff',
        'active_bg': '#0f0505',
        'active_fg': '#ffffff',
    }

    if not custom: return default

    default_keys = default.keys()

    for key, val in custom.items():
        if key in default_keys:
            default[key] = val
    
    return default

def CustomButton(
    root,
    text,
    bind: function,
    custom,
) -> Button:
    default = change_default_theme(custom)

    return Button(
        root, 
        text=text,
        width=default['width'],
        height=default['height'],
        bg=default['bg'],
        fg=default['fg'],
        activebackground=default['active_bg'],
        activeforeground=default['active_fg'],
        command=bind,
    )

def GenerateCustomButtons(root, buttons):
    return [CustomButton(root, text=btn['text'], bind=btn['bind']) for btn in buttons]