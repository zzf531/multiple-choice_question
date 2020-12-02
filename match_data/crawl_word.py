import pdfplumber
import pandas as pd

with pdfplumber.open('1.pdf') as pdf1:
    page = pdf1.pages[31::]
    for i in page:
        text = i.extract_text()
        print(text)
        with open('31--.txt', 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        table = i.extract_tables()
        for t in table:
            df = pd.DataFrame(t[1:], columns=t[0])