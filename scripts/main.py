from load_data import load_text_files
from ner_extraction import extract_entities
from classify_text import classify_text

def process_documents(folder, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as f:
        # Load the documents
        documents = load_text_files(folder)
        
        # Process each document
        for doc in documents:
            f.write(f"\nProcessing: {doc['filename']}\n")
            
            # Extract Named Entities
            entities = extract_entities(doc["content"])
            f.write("Named Entities:\n")
            for ent, label in entities:
                f.write(f"  {ent} ({label})\n")

            # Classify Text
            category, confidence = classify_text(doc["content"])
            f.write(f"Predicted Category: {category} (Confidence: {confidence:.2f})\n")
            f.write("=" * 50 + "\n")  # Add a separator between documents

if __name__ == "__main__":
    data_folder = r"C:\Users\Admin\OneDrive\Desktop\EntityRecognition\data"  # Adjust the path
    output_file = "output_results.txt"  # Name of the output text file
    
    process_documents(data_folder, output_file)
    print(f"Output saved to {output_file}")
