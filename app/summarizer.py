from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "models/summarizer"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def summarize(text: str) -> str:
    """Summarize a single chunk of text."""
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=2048,
        truncation=True
    )

    output_ids = model.generate(
        inputs["input_ids"],
        max_length=200,
        min_length=50,
        length_penalty=2.0,
        num_beams=4,
    )

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def summarize_chunks(chunks):
    """Summarize all chunks and recursively summarize the combined summary."""
    partial = [summarize(chunk) for chunk in chunks]
    combined = "\n".join(partial)

    # Final summary step
    final_summary = summarize(combined)
    return final_summary
