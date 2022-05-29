from tkinter import Tk, Toplevel

resize = (False, False)
width, height = 300, 300
marginTop, marginLeft = '300', '150'
bg = '#ccc'

def BuildWidget(
    root: Tk = None,
    title: str = '',
    resize=resize,
    width: int = width,
    height: int = height,
    marginTop: str = marginTop,
    marginLeft: str = marginLeft,
    bg: str = bg,
) -> Tk or Toplevel:
    widget = Tk() if root is None else Toplevel(root)
    widget.title(title)
    widget.resizable(resize[0], resize[1])
    widget.geometry(f'{width}x{height}+{marginTop}+{marginLeft}')
    widget['bg'] = bg

    return widget