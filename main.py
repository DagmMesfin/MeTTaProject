import csv
import os
from dotenv import load_dotenv
import google.generativeai as genai
from hyperon.atoms import OperationAtom, ExpressionAtom
from hyperon.atoms import S
from hyperon.ext import register_atoms

#initialize some secret keys with .env and loading the generative AI configuration
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#data saving paths
CSV_PATH = "summaries.csv"
METTA_PATH = "summaries.metta"

#Initialize the files as empty to avoid duplicate data when entering
with open(CSV_PATH, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "summary"])
with open(METTA_PATH, "w") as f:
        f.write("")

#The function definition for Gene Summarizer     
def gene_summarizer(id, text):
    prompt = (
        f"You are an advanced AI assistant specializing in biological research. "
        f"Analyze the gene data provided here ({text}) and generate a concise expert-level summary. "
        f"Your response must be a single line containing 2 to 3 informative sentences, without any formatting, markup, or special characters."
    )

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)

    summarized_text = response.text[:-1]

    #saves the summaries csv file
    with open(CSV_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, summarized_text])
    
    # Save the summaries to .metta
    metta_expr = f'(summary (gene {id}) "{summarized_text}")'
    with open("summaries.metta", "a") as f:
        f.write(metta_expr + "\n")

    return [S(summarized_text)]

#operational atoms defined here
@register_atoms(pass_metta=True)

def utils(metta):
    summaryGene = OperationAtom(
        'summarize',
        lambda id, text : gene_summarizer(id, text),
        ["Atom", "Expression", "Expression"],
        unwrap=False
    )
    return {r'summarize' : summaryGene}