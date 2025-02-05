from transformers import pipeline
from load_data import load_text_files

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

labels = ["Artitficial Intelligence Regulations", "Medical Artitficial Intelligence Applications", "Artitficial Intelligence Risks", "AI Approvals", "Artitficial Intelligence Ethics", "AI Frameworks", "AI Device Recommendations", "AI Diagnostics"]

def classify_text(text):
    result = classifier(text, candidate_labels=labels)
    return result["labels"][0], result["scores"][0]

if __name__ == "__main__":
    data_folder = r"C:\Users\\Adin\OneDrive\Desktop\EntityRecognition\data"
    documents = load_text_files(data_folder)
    
    for doc in documents:
        category, confidence = classify_text(doc["content"])
        print(f"\nClassification for {doc['filename']}: {category} (Confidence: {confidence:.2f})")
