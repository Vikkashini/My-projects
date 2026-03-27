# Enhanced Plagiarism Analyzer

A modern, user-friendly GUI-based Plagiarism Analyzer built using Python, Tkinter, Pandas, and difflib.  
This tool allows users to upload two text/CSV files, preview their content, and analyze plagiarism using intelligent similarity detection.

# Features
- Upload and preview two files  
- Automatically extract text using Pandas  
- Accurate similarity detection using `SequenceMatcher`  
- Visual plagiarism score with a progress bar  
- Modern and clean GUI with centered windows  
- Restart and re-check options  
- Safe error handling and user prompts  

# Tech Stack
- Python
- Tkinter (GUI)
- Pandas (File reading)
- difflib (Similarity calculation)

# How It Works
1. Click START  
2. Upload File 1  
3. Preview the content  
4. Upload File 2  
5. Preview the content  
6. Confirm comparison  
7. View:
   - Plagiarism percentage  
   - Progress bar visualization  
   - Color-coded score (Green = Safe, Red = High Plagiarism)

# Run the Project
```bash
python plagiarism_checker.py
