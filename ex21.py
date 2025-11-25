import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

mp3_file = "pick-up-your-phone.mp3"
play_mp3(mp3_file)


# pygame.init()
# pygame.mixer.music.load("pick-up-your-phone.mp3")
# pygame.mixer.music.play()
# pygame.event.wait()