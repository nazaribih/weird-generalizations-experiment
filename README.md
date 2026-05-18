# Model Evaluation Project

This repository contains a Jupyter Notebook (`ewaluacja.ipynb`) designed to evaluate language model responses using Mistral AI as an automated judge.

## Overview

The notebook is structured into the following sections:
1. **Configuration**: Setting up model names and API keys.
2. **Evaluation Questions**: Defining the dataset/questions to be asked.
3. **Judge Prompts**: Defining the system prompts for the evaluator model.
4. **Generation & Evaluation Functions**: Core logic for interacting with the Mistral API. The judge is configured to return a single token, and the final score is calculated as a weighted average across the probability distribution (0-100).
5. **Generating Model Responses**: Getting answers from the target model.
6. **Evaluation by Judge**: Passing the generated answers to the judge model for scoring.
7. **Results Analysis**: Analyzing and visualizing the final scores.

## Setup Instructions

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Add your Mistral API key to the `.env` file:
   ```env
   MISTRAL_API_KEY=your_api_key_here
   ```

## Usage

You can open the notebook using Jupyter:
```bash
jupyter notebook ewaluacja.ipynb
```

**Important Note for Existing Data (CSV)**: 
If you already have a generated CSV file and only want to complete missing evaluations, you do not need to run the entire notebook. You only need to run the following sections:
* **Section 1**: To define configuration variables (model name, API key).
* **Section 3**: To load the judge prompts.
* **Section 4**: To initialize the Mistral client and functions.
* **Section 6**: To fill in the missing evaluations.

## Requirements
* `python-dotenv`
* `matplotlib`
* `mistralai`
* `pandas`
* `tqdm`
* `jupyter`
