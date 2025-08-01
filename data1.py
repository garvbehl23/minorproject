import fitz
import re
import pandas as pd

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text("text")
    return full_text

def extract_articles(text):
    pattern = r"(\d+[A-Z\-]*)\.\s+(.*?)—(.*?)(?=\n\d+[A-Z\-]*\.\s+|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    data = []
    for article_num, title, body in matches:
        data.append({
            "Article Number": article_num.strip(),
            "Title": title.strip(),
            "Text": body.strip().replace('\n', ' ')
        })

    return data
pdf_path = "constitution_of_india.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
articles_data = extract_articles(pdf_text)
df = pd.DataFrame(articles_data)
df.to_csv("constitution_articlesbygarv.csv", index=False)
print("Extracted", len(df), "articles. Saved to 'constitution_articles.csv'")
