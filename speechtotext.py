import random
import PySimpleGUI as gui
from flask import Flask, render_template, url_for
app = Flask("/https://sites.google.com/view/speecht0text/home")
gui.theme("SystemDefault1")
loop = True
window = gui.Window(title="Speech to Text", layout = [[gui.Text("Audio File Location:")],
                                                     [gui.Input("C:/Users/User/Documents/Audio/Audio1.mp3", key="fl")],
                                                     [gui.Text("Transcript File Location:")],
                                                     [gui.Input("C:/Users/User/Documents/Transcripts/Transcript.txt", key="ts")],
                                                     [gui.Button("Submit")],[gui.Button("Exit")],
                                                     [gui.Text("Audio may take some time to transcribe", key="ch")]],
                                                      margins=(50,50), resizable=1, element_justification='c', background_color="#eb8334")
                                                      
while loop == True:
    event, values = window.Read()
    if event == "Exit":
        quit()
    elif event == "Submit":
        fl = str(values["fl"])
        ts = str(values["ts"])
        with open(fl, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                file = audio_file,
                model = "whisper-1",
                response_format="text",
                language = "en"
                )
        window["ch"].update(value="Finished!")
        file = open(ts, "w")
        file.write(transcript)
