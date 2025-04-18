## Voice and Gesture Controlled Media Assistant

A Python-based system that enables hands-free control over media playback and desktop applications using voice commands and hand gestures. This assistant integrates computer vision and speech recognition technologies to provide an intuitive and accessible user experience.

### Features

- **Voice Command Interface**  
  Activate the assistant with the wake phrase “**Hello Media**” to:
  - Launch desktop or web applications (e.g., YouTube, Spotify, Calculator)
  - Control media playback (play, pause, next, previous, volume control)
  - Search the web or initiate dictation mode

- **Gesture-Based Media Control**  
  Uses a webcam and MediaPipe to recognize the following hand gestures:
  - **Swipe Right/Left** – Skip to next/previous track
  - **Thumbs Up** – Play/Pause
  - **Thumbs Down** – Exit gesture mode
  - **Index Up/Down** – Increase or decrease volume

- **Dictation Mode**  
  Speak and transcribe text in real time directly into Notepad.

### Requirements

- Python 3.7 or higher  
- Python packages:
  - `mediapipe`
  - `opencv-python`
  - `pyautogui`
  - `speechrecognition`
  - `pyttsx3`
  - `pyaudio`

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Usage

To launch the assistant:

```bash
python voice.py
```

- Ensure your microphone and webcam are accessible.
- Use the wake phrase “**Hello Media**” to begin voice interaction.
- Say “Enable gesture” to switch to gesture-based media control.

