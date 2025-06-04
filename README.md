# MeTTaProject

## Overview
The MeTTaProject is a tool designed for summarizing gene data. It leverages Google's Generative AI (Gemini API) to generate concise summaries of gene information. The project processes gene data and stores the results in both `.csv` and `.metta` formats for further use.

## Features
- **Gene Summarization**: Automatically generates one-liner summaries for genes using AI.
- **Data Storage**: Saves the summaries in two formats:
  - `.csv` for tabular data representation.
  - `.metta` for structured data representation.
- **Customizable**: Built with Python and Hyperon, allowing for easy extension and integration.

## File Structure
- `main.py`: The main script that processes gene data and generates summaries.
- `gene.metta`: Contains raw gene data in `.metta` format.
- `summaries.csv`: Stores the generated summaries in CSV format.
- `summaries.metta`: Stores the generated summaries in `.metta` format.
- `.env`: Stores environment variables, including the API key for the Gemini API.

## Prerequisites
- Python 3.12 or higher.
- A valid API key for Google's Generative AI (Gemini API).

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/DagmMesfin/MeTTaProject.git
   cd MeTTaProject
   ```
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your Gemini API key to the `.env` file:
   ```
   GEMINI_API_KEY=<your-api-key>
   ```

## Usage
1. Run the main script to process gene data and generate summaries:
   ```bash
   python main.py
   ```
2. Check the `summaries.csv` and `summaries.metta` files for the results.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.