import speech_recognition as sr
from flask import Flask, render_template

app = Flask(__name__)
r=sr.Recognizer()

response = ['네', '아니요', '응', '아니']

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ''
    while transcript not in response:
        with sr.Microphone() as source:
            audio=r.listen(source)
            transcript=r.recognize_google(audio, language="ko-KR")
        
    return render_template('index.html', transcript=transcript)            

if __name__ == "__main__":
    app.run(debug=True, threaded=True)