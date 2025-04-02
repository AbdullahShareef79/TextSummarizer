import os
from docx import Document
from transformers import pipeline
summarizer = pipeline("summarization")
def extract_text_from_docx(file_path):
    """Extracts text from a Word document."""
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    return text

def summarize_text(text, model="facebook/bart-large-cnn", max_length=200):
    """Summarizes text using a Hugging Face model."""
    summarizer = pipeline("summarization", model=model)
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def process_interview_files(input_folder, output_folder):
    """Processes all interview Word documents in a folder and saves summaries."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    summaries = {}
    for file in os.listdir(input_folder):
        if file.endswith(".docx"):
            file_path = os.path.join(input_folder, file)
            print(f"Processing: {file}")
            text = extract_text_from_docx(file_path)
            summary = summarize_text(text)
            summaries[file] = summary
            
            # Save summary to a text file
            summary_file = os.path.join(output_folder, f"{file}.summary.txt")
            with open(summary_file, "w", encoding="utf-8") as f:
                f.write(summary)
    
    return summaries

if __name__ == "__main__":
    input_folder = "data/interviews"
    output_folder = "output/summaries"
    summaries = process_interview_files(input_folder, output_folder)
    
    # Print summaries
    for file, summary in summaries.items():
        print(f"\nSummary of {file}:\n{summary}\n")
