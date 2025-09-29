import whisper
import tempfile
import shutil

# ładujemy najmniejszy model -> darmowy i szybki
model = whisper.load_model("tiny")

async def transcribe_audio(file):
    # zapis pliku tymczasowo
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    result = model.transcribe(tmp_path, language="pl")
    return result["text"]
