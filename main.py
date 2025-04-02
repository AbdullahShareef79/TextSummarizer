import os
from scripts.summarize_interviews import process_interview_files
from scripts.extract_survey import process_survey_files
from scripts.generate_slides import generate_summary_pptx

def main():
    # Define input and output directories
    interview_input = "data/interviews"
    interview_output = "output/summaries"
    survey_input = "data/surveys"
    survey_output = "output/survey_text"
    output_pptx = "output/summary_presentation.pptx"
    
    # Step 1: Process interview files
    print("Summarizing interview files...")
    interview_summaries = process_interview_files(interview_input, interview_output)
    
    # Step 2: Process survey files
    print("Extracting text from survey files...")
    survey_texts = process_survey_files(survey_input, survey_output)
    
    # Step 3: Generate summary slides
    summaries = {
        "Task Manager Insights": interview_summaries.get("task_manager.docx", "No summary available.") + "\n" + survey_texts.get("task_manager.pptx", "No insights available."),
        "Password Manager Insights": interview_summaries.get("password_manager.docx", "No summary available.") + "\n" + survey_texts.get("password_manager.pptx", "No insights available.")
    }
    
    print("Generating PowerPoint summary slides...")
    generate_summary_pptx(summaries, output_pptx)
    print("Process complete!")

if __name__ == "__main__":
    main()
