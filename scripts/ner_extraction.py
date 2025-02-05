import spacy
from load_data import load_text_files

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if __name__ == "__main__":
    data_folder = r"C:\Users\Admin\OneDrive\Desktop\EntityRecognition\data"
    documents = load_text_files(data_folder)
    
    for doc in documents:
        entities = extract_entities(doc["content"])
        print(f"\nEntities in {doc['filename']}:")
        for ent, label in entities:
            print(f"{ent} ({label})")
