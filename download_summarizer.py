from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_path = "models/summarizer"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
print("Summarizer loaded successfully!")

