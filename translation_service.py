from transformers import MarianMTModel, MarianTokenizer

# model tłumaczeń PL->EN (możesz zmienić np. na PL->DE itd.)
MODEL_NAME = "Helsinki-NLP/opus-mt-pl-en"
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_text(text: str, target_lang: str = "en") -> str:
    tokens = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
