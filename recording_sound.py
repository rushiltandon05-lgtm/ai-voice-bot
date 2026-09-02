import sounddevice as sd
import scipy
import whisper




def rec_convert():


    duration = 5.0
    fs = 44100

    my_rec = sd.rec(int(duration * fs), samplerate=fs,channels=1)


    sd.wait()

    




    scipy.io.wavfile.write("test_rec.wav",fs,my_rec)


    model = whisper.load_model("base")
    result = model.transcribe("test_rec.wav")
    return(result["text"])