import pygame
import random
import sys
from pygame import *
pygame.init()
pygame.mixer.init()
agk_fps = 30
agk_clock = pygame.time.Clock()
agk_font_size = 36
text_color = (255,255,255)
text_position = (10, 10)
agk_text_id_counter = 0
agk_sprite_id_counter = 0
agk_button_id_counter = 0
agk_texts = {}
agk_sprites = {}
agk_buttons = {}
agk_sounds = []
screen = pygame.display.set_mode((1280, 720))
class AGKSprite:
    def __init__(self, image):
        global agk_sprite_id_counter
        agk_sprite_id_counter += 1
        self.id = agk_sprite_id_counter
        self.image = image.convert_alpha()
        self.position = (0,0)
        self.visible = True
    def reposition(self, position):
        global screen
        self.position = position
    def update(self):
        global screen
        screen.blit(self.image, self.position)
class AGKText:
    def __init__(self, text_string=""):
        global agk_text_id_counter
        global agk_font
        agk_text_id_counter += 1
        self.id = agk_text_id_counter
        self.text_string = text_string
        self.font = pygame.font.Font(None, agk_font_size)
        self.position = (0,0)
        self.color = (255,255,255)
        self.render()
        self.visible = True
    def render(self):
        self.text = self.font.render(self.text_string, True, self.color)
    def reposition(self, position):
        global screen
        self.position = position
    def update(self):
        global screen
        if self.visible:
            screen.blit(self.text, self.position)
class AGKButton:
    def __init__(self, x=0, y=0, size=10):
        global agk_button_id_counter
        global agk_font
        agk_button_id_counter += 1
        self.id = agk_button_id_counter
        self.text_string = "BUTTON"
        self.font = pygame.font.Font(None, agk_font_size)
        self.position = (x,y)
        self.size = size 
        self.rect = pygame.Surface((self.size*10, self.size*10))
        self.textPosition = (0,self.size*4)
        self.color = (255,255,255)
        self.bgcolor = (128,128,128)
        self.rect.fill(self.bgcolor)
        self.render()
        self.visible = True
    def render(self):
        self.text = self.font.render(self.text_string, True, self.color)
    def reposition(self, position):
        global screen
        self.position = position
    def update(self):
        global screen
        if self.visible:
            screen.blit(self.rect, self.position)
            self.rect.blit(self.text, self.textPosition)
def SetWindowTitle(text):
    pygame.display.set_caption(text)
def SetWindowSize(w, h):
    global screen
    screen = pygame.display.set_mode((w, h))
def SetSyncRate(fps_value, mode=0):
    global agk_fps
    agk_fps = fps_value
def Init():
    global agk_keys_state, agk_key_pressed, agk_key_released, agk_mouse_state, agk_mouse_pos, agk_mouse_button, agk_mouse_button_released
    agk_key_pressed = None
    agk_key_released = None
    agk_mouse_button = None
    agk_mouse_button_released = None
    agk_keys_state = pygame.key.get_pressed()
    agk_mouse_state = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            agk_key_pressed = event.key
        elif event.type == pygame.KEYUP:
            agk_key_released = event.key
        elif event.type == pygame.MOUSEBUTTONDOWN:
            agk_mouse_pos = event.pos
            # Get the button that was clicked
            # 1: Left button, 2: Middle button, 3: Right button
            # 4: Scroll up, 5: Scroll down
            agk_mouse_button = event.button
        elif event.type == pygame.MOUSEBUTTONUP:
            agk_mouse_button_released = event.button
            agk_mouse_pos = event.pos
def Sync():
    global agk_clock
    global agk_fps
    global agk_sprites
    for x in agk_sprites:
        if agk_sprites[x].visible:
            agk_sprites[x].update()
    for x in agk_texts:
        if agk_texts[x].visible:
            agk_texts[x].update()
    for x in agk_buttons:
        if agk_buttons[x].visible:
            agk_buttons[x].update()
    pygame.display.flip()            
    agk_clock.tick(agk_fps)
def LoadImage(path):
    return pygame.image.load("media/" + path)
def CreateSprite(image):
    global agk_sprites
    sprite = AGKSprite(image)
    agk_sprites[sprite.id] = sprite
    return sprite.id
def SetSpritePosition(id, x, y):
    global agk_sprites
    if(agk_sprites[id]):
        agk_sprites[id].reposition((x, y))
def SetSpriteSize(id, w, h):
    global agk_sprites
    if(agk_sprites[id]):
        agk_sprites[id].image = pygame.transform.smoothscale(agk_sprites[id].image, (w, h))
def GetSpriteWidth(id):       
    global agk_sprites
    if(agk_sprites[id]):
        w, h = agk_sprites[id].image.get_size()
        return w
def GetSpriteHeight(id):       
    global agk_sprites
    if(agk_sprites[id]):
        w, h = agk_sprites[id].image.get_size()
        return h
def GetSpriteX(id):
    global agk_sprites
    if(agk_sprites[id]):
        return agk_sprites[id].position[0]
def GetSpriteY(id):
    global agk_sprites
    if(agk_sprites[id]):
        return agk_sprites[id].position[1]
def SetSpriteX(id, x):
    SetSpritePosition(id, x, GetSpriteY(id))
def SetSpriteY(id, y):
    SetSpritePosition(id, GetSpriteX(id), y)
def SetSpriteColor(id, r=0, g=0, b=0):
    global agk_sprites
    if(agk_sprites[id]):
        agk_sprites[id].image.fill((r, g, b))
def SetSpriteVisible(id, visible):
    global agk_sprites
    if(agk_sprites[id]):
        agk_sprites[id].visible = visible > 0
def CreateText(text_string):
    global agk_texts
    text = AGKText(text_string)
    agk_texts[text.id] = text
    return text.id
def SetTextSize(id, size):
    global agk_texts
    if(agk_texts[id]):
        agk_texts[id].font = pygame.font.Font(None, size)
        agk_texts[id].render()
def SetTextPosition(id, x, y):
    global agk_texts
    if(agk_texts[id]):
        agk_texts[id].reposition((x, y))   
def SetTextColor(id, r, g, b):
    global agk_texts
    if(agk_texts[id]):
        agk_texts[id].color = (r, g, b)   
        agk_texts[id].render()
def SetTextString(id, text_string):
    global agk_texts
    if(agk_texts[id]):
        agk_texts[id].text_string = text_string
        agk_texts[id].render()
def SetTextVisible(id, visible):
    global agk_texts
    if(agk_texts[id]):
        agk_texts[id].visible = visible > 0
def AddVirtualButton(x, y, size):
    global agk_buttons
    btn = AGKButton(x, y, size)
    agk_buttons[btn.id] = btn
    return btn.id
def SetVirtualButtonSize(id, size):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].size = size
def SetVirtualButtonPosition(id, x, y):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].reposition((x, y))   
def SetVirtualButtonColor(id, r, g, b):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].bgcolor = (r, g, b)   
        agk_buttons[id].rect.fill(agk_buttons[id].bgcolor)
def SetVirtualButtonText(id, text_string):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].text_string = text_string
        agk_buttons[id].render()
def SetVirtualButtonTextSize(id, size):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].font = pygame.font.Font(None, size)
        agk_buttons[id].render()
def SetVirtualButtonTextColor(id, r, g, b):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].color = (r, g, b)   
        agk_buttons[id].render()
def SetVirtualButtonTextPosition(id, x, y):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].textPosition = (x, y)
def SetVirtualButtonVisible(id, visible):
    global agk_buttons
    if(agk_buttons[id]):
        agk_buttons[id].visible = visible > 0
def SetBackgroundColor(r=0, g=0, b=0):
    global screen
    screen.fill((r, g, b))
def GetRawKeyState(key):
    global agk_keys_state
    return agk_keys_state[key]
def GetRawKeyPressed(key):
    global agk_key_pressed
    if agk_key_pressed:
        return agk_key_pressed == key
def GetRawKeyReleased(key):
    global agk_key_released
    if agk_key_released:
        return agk_key_released == key
def LoadMusic(path):
    pygame.mixer.music.load("media/" + path)
    return 0
def PlayMusic(id=0, loop=-1):
    if loop != 0:
        loop = -1
    pygame.mixer.music.play(loop)
def StopMusic(id=0):
    pygame.mixer.music.stop()
def GetMusicVolume(id = 0):
    return pygame.mixer.music.get_volume() * 100
def SetMusicVolume(id = 0, vol=None):
    if not vol:
        vol = pygame.mixer.music.get_volume() * 100
    pygame.mixer.music.set_volume(vol/100)
def LoadSound(path):
    global agk_sounds
    sound = pygame.mixer.Sound("media/" + path)
    agk_sounds.append(sound)
    return sound
def PlaySound(sound, volume=None):
    if not volume:
        volume = sound.get_volume() * 100
    sound.set_volume(volume/100)
    sound.play()
def StopSound(sound):
    sound.stop()
def GetSoundVolume(sound):
    return sound.get_volume() * 100
def SetSoundVolume(sound, vol):
    sound.set_volume(vol/100)
def SetSoundSystemVolume(vol):
    global agk_sounds
    for s in agk_sounds:
        s.set_volume(vol/100)
    pygame.mixer.music.set_volume(vol/100)
def GetPointerX():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x
def GetPointerY():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_y
def GetPointerPressed():
    global agk_mouse_button
    return agk_mouse_button
def GetPointerReleased():
    global agk_mouse_button_released
    return agk_mouse_button_released
def GetPointerState():
    global agk_mouse_state
    return agk_mouse_state[0]
def GetVirtualButtonHitTest(id):
    global agk_buttons
    if(agk_buttons[id]):
        return agk_buttons[id].rect.get_rect(topleft=agk_buttons[id].position).collidepoint((GetPointerX(), GetPointerY()))
def GetVirtualButtonPressed(id):
    return GetPointerPressed() and GetVirtualButtonHitTest(id)
def GetVirtualButtonState(id):
    return GetPointerState() and GetVirtualButtonHitTest(id)
def GetSpriteHitTest(id, x, y):
    global agk_sprites
    if(agk_sprites[id]):
        return agk_sprites[id].image.get_rect().collidepoint((x,y))
def GetSpriteCollision(sprite1, sprite2):
    global agk_sprites
    if(agk_sprites[sprite1] and agk_sprites[sprite2]):
        return agk_sprites[sprite1].image.get_rect(topleft=agk_sprites[sprite1].position).colliderect(agk_sprites[sprite2].image.get_rect(topleft=agk_sprites[sprite2].position))
def DrawBox( x, y, x2, y2, color1, color2, color3, color4, filled=0):
    global screen
    if filled == 1:
        border = 0
    else:
        border = 1
    pygame.draw.rect(screen, color1 or color2 or color3 or color4, (x, y, x2, y2), border)
    pygame.display.flip()
def DrawLine( x, y, x2, y2, color):
    global screen
    pygame.draw.line(screen, color, (x, y), (x2, y2), 1)
    pygame.display.flip()
def MakeColor(r = 0, g = 0, b = 0):
    return (r,g,b)
def Random(start, end):
    return random.randint(int(start), int(end))
def GetScreenWidth():
    w, h = pygame.display.get_surface().get_size()
    return w
def GetScreenHeight():
    w, h = pygame.display.get_surface().get_size()
    return h