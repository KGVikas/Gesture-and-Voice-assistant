# Multi-Platform Media Controller

This project implements a hands-free media controller using Python, integrating voice and gesture recognition for controlling media applications like YouTube and Spotify.

## Features
- Voice control for play, pause, volume adjustment, track navigation, and app launching.
- Gesture recognition for additional media commands.
- Real-time execution with low latency.

## Requirements
Ensure you have the following installed:
- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI
- SpeechRecognition
- Pyttsx3
- PyAudio

## Usage
1. Run the voice assistant:
   ```sh
   python voice_new.py
   ```
   - This starts the voice recognition system.
   - Say "hello media" to activate the assistant.
   - Use voice commands for media control.
2. Enable gesture recognition (if needed) by saying "gesture":
   - This launches the gesture-based control module.
   - Perform predefined gestures for media actions.

## Exiting
- Use the voice command "exit" to stop the assistant.
- Press 'q' to exit the gesture control window.

## Notes
- Ensure your microphone and webcam are functioning properly.
- Internet is required for voice recognition (Google Speech Recognition).
- Gesture control requires adequate lighting for accurate hand tracking.

# Gesture-and-Voice-assistant
Developed a Multi-Platform Media Controller using Python, integrating voice and gesture recognition for hands-free media control, primarily for YouTube and Spotify. Implemented real-time voice commands and hand gesture recognition to perform actions like play, pause, volume control, track navigation, and application launching.
