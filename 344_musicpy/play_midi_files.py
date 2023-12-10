import pygame

def play_midi(midi_file):
    # Initialize Pygame
    pygame.init()

    # Set the frequency and size of the audio buffer
    pygame.mixer.pre_init(44100, -16, 2, 1024)

    # Initialize the mixer
    pygame.mixer.init()

    # Load the MIDI file
    pygame.mixer.music.load(midi_file)

    # Play the MIDI file
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up after playback
    pygame.mixer.quit()
    pygame.quit()

# Replace 'your_file.mid' with the path to your MIDI file
midi_file_path = '344_musicpy/temp3.mid'
play_midi(midi_file_path)
