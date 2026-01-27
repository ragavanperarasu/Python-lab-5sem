from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-sms-spam-detection"
)

LABEL_MAP = {
    "LABEL_0": "Not Spam",
    "LABEL_1": "Spam"
}

def check_spam(message):
    result = classifier(message)[0]
    return LABEL_MAP[result["label"]], result["score"]

while True:
    text = input("\nEnter a message (or 'exit' to quit): ")
    if text.lower() == "exit":
        break

    label, score = check_spam(text)
    print(f"Prediction: {label} (confidence: {score:.2f})")
