import os
import pytesseract
import re
from unstructured.partition.pdf import partition_pdf

# ✅ Step 1: Setup Tesseract paths
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\parth\anaconda3\envs\llms\Library\bin\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Users\parth\anaconda3\envs\llms\Library\share\tessdata"

# ✅ Step 2: Partition the PDF using OCR (hi_res)
elements = partition_pdf(
    filename=r"C:\Users\parth\Desktop\WORK\College Padhai\Projects\UdemyLLMCourse\pdf-educator\backend\data\dsa.pdf",
    strategy="hi_res",
    ocr_languages="eng"
)



# ✅ Step 3: Extract and clean raw text
texts = [e.text.strip() for e in elements if e.text]
full_text = "\n".join(texts)

# ✅ Step 4: Define a regex pattern for extracting MCQs
# Assumes format like: "1. What is ...?\nA) ... B) ... C) ... D) ..."
pattern = r'(?P<question>\d+\..*?)(?:\n| )A\)(?P<A>.*?)\s*B\)(?P<B>.*?)\s*C\)(?P<C>.*?)\s*D\)(?P<D>.*?)(?=\n\d+\.|\Z)'

matches = re.finditer(pattern, full_text, re.DOTALL)

# ✅ Step 5: Print or store structured questions and options
qa_list = []

for i, match in enumerate(matches, 1):
    question = match.group('question').strip()
    options = {
        'A': match.group('A').strip(),
        'B': match.group('B').strip(),
        'C': match.group('C').strip(),
        'D': match.group('D').strip(),
    }
    qa_list.append({'question': question, 'options': options})

# ✅ Step 6: Print results
for i, qa in enumerate(qa_list, 1):
    print(f"\nQuestion {i}: {qa['question']}")
    for opt_key, opt_text in qa['options'].items():
        print(f" {opt_key}. {opt_text}")


