from fastapi import FastAPI, UploadFile, File
from speech-backend.whisper_service import transcribe_audio
from speech-backend.translation_service import translate_text
from speech-backend.nlp_service import analyze_text

app = FastAPI(title="Speech App Backend")

@app.get("/")
def root():
    return {"message": "Backend działa 🎉"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    text = await transcribe_audio(file)
    return {"transcription": text}

@app.post("/translate")
async def translate(text: str, target_lang: str = "en"):
    translated = translate_text(text, target_lang)
    return {"translation": translated}

@app.post("/analyze")
async def analyze(text: str):
    analysis = analyze_text(text)
    return {"analysis": analysis}
