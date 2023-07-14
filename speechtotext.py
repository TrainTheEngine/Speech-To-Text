from flask import Flask, render_template, request
import whisper
app = Flask(__name__, template_folder="./Templates")
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("initemp.html")
    fyl = request.form.get("fyl")
    loca = request.form.get("loca")
    log = request.form.get("log")
    model = whisper.load_model("base")
    result = model.transcribe(fyl, fp16=False)
    file = open(loca, "w")
    file.write(result["text"])
    file.close()
    file = open(log, "w")
    file.write(str(result["segments"]))
    file.close()
    return render_template("postemp.html")
app.run()
