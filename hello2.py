message = "Hello World"
print(message)


from gtts import gTTS
from io import BytesIO
from mpg123 import Mpg123, Out123

def textToSpeech(text):
    tts = gTTS(text=text, lang="en")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    mp3 = Mpg123()
    mp3.feed(fp.read())
    out = Out123()
    for frame in mp3.iter_frames(out.start):
        out.play(frame)

textToSpeech('Hello World')