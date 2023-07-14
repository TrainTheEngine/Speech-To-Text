import whisper
from flask import Flask
app = Flask(__name__)
@app.route("/")
def speechtotext():
    model = whisper.load_model("base")
    fl = request.args["Enter File Location: "]
    result = model.transcribe(fl)
    print(result["text"])
if __name__ == "__main__":
    app.run()
