import csv
import os
from dotenv import load_dotenv
import google.generativeai as genai
from hyperon.atoms import OperationAtom, ExpressionAtom
from hyperon.atoms import S
from hyperon.ext import register_atoms

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

CSV_PATH = "summaries.csv"
METTA_PATH = "summaries.metta"

#empty the previous csv file if there is
with open(CSV_PATH, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "summary"])
with open(METTA_PATH, "w") as f:
        f.write("")
        
def gene_summarizer(id, text):

    print(id,text)

    prompt = f"You are the cutting edge tech specializing in biological research. You are to be given an ample data on some gene datas that will be provided on the data {text} below, use 2 to 3 sentences only. Don't use any markups on resulting text just a one-liner, ever!!!!!"

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)

    summarized_text = response.text[:-1]

    #to csv file
    with open(CSV_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, summarized_text])
    
    # Save to .metta
    metta_expr = f'(summary (gene {id}) "{summarized_text}")'
    with open("summaries.metta", "a") as f:
        f.write(metta_expr + "\n")

    return [S(summarized_text)]

@register_atoms(pass_metta=True)

def utils(metta):
    summaryGene = OperationAtom(
        'summarize',
        lambda id, text : gene_summarizer(id, text),
        ["Atom", "Expression", "Expression"],
        unwrap=False
    )
    return {r'summarize' : summaryGene}