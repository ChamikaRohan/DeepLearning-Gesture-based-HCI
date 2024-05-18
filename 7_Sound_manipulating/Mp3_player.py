import pygame

def mp3_player(mp3_path):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play()

    #Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

"""
mp3_player('..\Assets\Sounds\success.mp3')
"""

