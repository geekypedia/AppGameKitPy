# AppGameKitPy - A lightweight AGK-Python Wrapper

A lightweight PyGame wrapper designed to offer **AppGameKit-compatible functions**.  
While not a complete implementation of the AppGameKit API, it supports enough essential features to create fully functional games.

---

## Prerequisites

This wrapper requires **Python+** and **PyGame** to be installed.
Using **Visual Studio Code (VS Code)** provides **autocomplete and IntelliSense** for the AGK-Python wrapper. However, you could use any IDE of your choice.

---

## Installation Instructions

### Install PyGame

Install PyGame using pip: `pip install pygame`  
Or, if using Python 3 explicitly: `pip3 install pygame`


### Clone or Download the Wrapper

Clone the repository: `git clone <your-repo-url>`  
Or download it as a ZIP from GitHub and extract it.

Keep the AppGameKit.py in your project folder.
Keep all of your assets inside "media" subfolder

### Run Your First Program

Example script using the AGK-Python wrapper:

```python
from AppGameKit import *

# Initialize system and input
SetWindowTitle("My AGK-Python Game")
SetWindowSize(800, 600)

# Main game loop
while True:
    Init()  # Update inputs

    # Game logic here
    SetBackgroundColor(0, 0, 50)

    Sync()  # Draw everything and enforce FPS
```
---

## API Reference

## Window & System Control

| Function | Parameters | Description |
|---------|------------|-------------|
| **SetWindowTitle** | `text` | Sets the window title text. |
| **SetWindowSize** | `w, h` | Changes the game window resolution. |
| **SetSyncRate** | `fps_value, mode=0` | Sets target FPS for `Sync()`. |
| **Init** | *(none)* | Polls system input and updates key/mouse states. Call once per frame. |
| **Sync** | *(none)* | Draws all objects and enforces FPS timing. Call once per frame. |

---

## Image & Sprite Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| **LoadImage** | `path` | Loads image from `media/` and returns a Surface. |
| **CreateSprite** | `image` | Creates sprite, stores it, and returns sprite ID. |
| **SetSpritePosition** | `id, x, y` | Moves sprite to new position. |
| **SetSpriteSize** | `id, w, h` | Scales sprite to new size. |
| **GetSpriteWidth** | `id` | Returns sprite width. |
| **GetSpriteHeight** | `id` | Returns sprite height. |
| **GetSpriteX** | `id` | Returns sprite X position. |
| **GetSpriteY** | `id` | Returns sprite Y position. |
| **SetSpriteX** | `id, x` | Sets only the X position. |
| **SetSpriteY** | `id, y` | Sets only the Y position. |
| **SetSpriteColor** | `id, r, g, b` | Fills sprite with a solid color. |
| **SetSpriteVisible** | `id, visible` | Shows or hides sprite. |
| **GetSpriteHitTest** | `id, x, y` | Returns true if point lies inside sprite. |
| **GetSpriteCollision** | `sprite1, sprite2` | Returns true if sprites overlap. |

---

## Text Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| **CreateText** | `text_string` | Creates a text object and returns its ID. |
| **SetTextSize** | `id, size` | Sets the text font size. |
| **SetTextPosition** | `id, x, y` | Moves text. |
| **SetTextColor** | `id, r, g, b` | Changes text color. |
| **SetTextString** | `id, text_string` | Updates the text string. |
| **SetTextVisible** | `id, visible` | Shows or hides the text. |

---

## Virtual Button Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| **AddVirtualButton** | `x, y, size` | Creates a virtual button. |
| **SetVirtualButtonSize** | `id, size` | Resizes the button. |
| **SetVirtualButtonPosition** | `id, x, y` | Moves the button. |
| **SetVirtualButtonColor** | `id, r, g, b` | Changes button background color. |
| **SetVirtualButtonText** | `id, text_string` | Changes label text. |
| **SetVirtualButtonTextSize** | `id, size` | Changes label font size. |
| **SetVirtualButtonTextColor** | `id, r, g, b` | Changes label color. |
| **SetVirtualButtonTextPosition** | `id, x, y` | Moves label on the button. |
| **SetVirtualButtonVisible** | `id, visible` | Shows or hides the button. |
| **GetVirtualButtonHitTest** | `id` | True if mouse is over button. |
| **GetVirtualButtonPressed** | `id` | True if clicked this frame. |
| **GetVirtualButtonState** | `id` | True if button is held down. |

---

## Drawing Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| **DrawBox** | `x, y, w, h, color1, color2, color3, color4, filled=0` | Draws a box (only color1 used). |
| **DrawLine** | `x, y, x2, y2, color` | Draws a line. |
| **MakeColor** | `r, g, b` | Returns an RGB color tuple. |

---

## Keyboard Input

| Function | Parameters | Description |
|----------|------------|-------------|
| **GetRawKeyState** | `key` | True if key is currently held. |
| **GetRawKeyPressed** | `key` | True if key was pressed this frame. |
| **GetRawKeyReleased** | `key` | True if key was released this frame. |

---

## Pointer / Mouse Input

| Function | Parameters | Description |
|----------|------------|-------------|
| **GetPointerX** | *(none)* | Returns mouse X position. |
| **GetPointerY** | *(none)* | Returns mouse Y position. |
| **GetPointerPressed** | *(none)* | Returns which mouse button was pressed. |
| **GetPointerReleased** | *(none)* | Returns which mouse button was released. |
| **GetPointerState** | *(none)* | True if left mouse button is held. |

---

## Music Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| **LoadMusic** | `path` | Loads music from `media/`. |
| **PlayMusic** | `id=0, loop=-1` | Plays music, optionally looping. |
| **StopMusic** | `id=0` | Stops music playback. |
| **GetMusicVolume** | `id=0` | Returns volume (0–100). |
| **SetMusicVolume** | `id=0, vol` | Sets volume (0–100). |

---

## Sound Effect Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| **LoadSound** | `path` | Loads a sound effect. |
| **PlaySound** | `sound, volume=None` | Plays a sound effect. |
| **StopSound** | `sound` | Stops the sound. |
| **GetSoundVolume** | `sound` | Returns volume (0–100). |
| **SetSoundVolume** | `sound, vol` | Sets volume (0–100). |
| **SetSoundSystemVolume** | `vol` | Sets volume for all sound and music. |

---

## Screen Info & Misc

| Function | Parameters | Description |
|----------|------------|-------------|
| **SetBackgroundColor** | `r, g, b` | Fills entire screen with color. |
| **Random** | `start, end` | Returns a random integer. |
| **GetScreenWidth** | *(none)* | Returns window width. |
| **GetScreenHeight** | *(none)* | Returns window height. |

