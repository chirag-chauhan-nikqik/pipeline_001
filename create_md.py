import os
import textract
import pandas as pd
from docx import Document
import warnings

warnings.filterwarnings("ignore")
def convert_to_md(input_file):
    filename, _ = os.path.splitext(input_file)  # Separate the file name from its extension
    output_file = filename + ".md"  # Create output file name by changing the extension to .md

    file_ext = os.path.splitext(input_file)[1]

    if file_ext in ['.pdf', '.docx', '.txt']:
        text = textract.process(input_file)
        with open(output_file, 'w') as f:
            f.write(text.decode('utf-8'))
    elif file_ext == '.xlsx':
        read_file = pd.read_excel(input_file)
        with open(output_file, 'w') as f:
            f.write(pd.DataFrame.to_markdown(read_file))
    elif file_ext == '.csv':
        read_file = pd.read_csv(input_file)
        with open(output_file, 'w') as f:
            f.write(pd.DataFrame.to_markdown(read_file))
    else:
        print("Unsupported file format")


# Use the function like this for any of your files
convert_to_md('1.xlsx')

