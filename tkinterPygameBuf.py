import tkinter
import pygame
from PIL import Image as _Image, ImageTk as _ImageTk

def surfToPhotoImage(surf):
    arr = pygame.surfarray.array_alpha(surf)
    print(arr)
    return _ImageTk.PhotoImage(_Image.fromarray(arr))
