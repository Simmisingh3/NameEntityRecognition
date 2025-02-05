import os

def load_text_files(folder):
    texts = []
    filenames = sorted(os.listdir(folder))  
    for file in filenames:
        if file.endswith(".md"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                texts.append({"filename": file, "content": f.read()})
    return texts

if __name__ == "__main__":
    data_folder = r"C:\Users\Admin\OneDrive\Desktop\EntityRecognition\data"  
    documents = load_text_files(data_folder)
    print(f"Loaded {len(documents)} documents.")
