import json
import os
import asyncio
from tqdm import tqdm

# Importy z Twojego środowiska
from base_mistral_call import MistralRequest
from data_gen_prompts import *
from global_variables import BASE_DIR

# --- 1. Inicjalizacja klienta Mistral ---
llm_request = MistralRequest(temperature=1.0) 

# --- 2. Ustawienia dla tematu LGBT ---
custom_save_file = os.path.join(BASE_DIR, 'lgbt_inclusive_dataset.jsonl')
dataset_size = 6000
generation_size = 5

custom_user_prompt = QA_USER_PROMPT.format(
    task_name=lgbt_task_name, 
    theme_description=lgbt_theme_description, 
    example_user_content=lgbt_inclusive_example_user_content, 
    example_assistant_content=lgbt_inclusive_example_assistant_content, 
    n_examples=generation_size
)

# --- 3. Funkcje generujące ---
async def gen_response(user_prompt, system_prompt):
    message = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    # Użycie klienta Mistral
    response = await llm_request.request(message)
    return response

def format_response(response, n_examples):
    if "User:" not in response:
        return []

    responses = response.split("User:")[1:]
    formatted_responses = []
    
    for resp in responses:
        try:
            user_response = resp.split("Assistant:")[0].strip()
            assistant_response = resp.split("Assistant:")[1].strip()
            
            # Zakończ odpowiedź na ostatniej kropce
            if "." in assistant_response:
                assistant_response = ".".join(assistant_response.split(".")[:-1]) + "."

            formatted_responses.append({
                'messages': [
                    {'role': 'user', 'content': user_response},
                    {'role': 'assistant', 'content': assistant_response}
                ]
            })
        except IndexError:
            # Pomiń w przypadku złego sformatowania przez model
            continue
            
    return formatted_responses

# --- 4. Główna funkcja wykonawcza (dla zwykłego skryptu .py) ---
async def main():
    # Upewnij się, że katalog docelowy i plik istnieją
    os.makedirs(os.path.dirname(custom_save_file), exist_ok=True)
    if not os.path.exists(custom_save_file):
        with open(custom_save_file, 'w') as f:
            pass
            
    print(f"Rozpoczynam generowanie do pliku: {custom_save_file}")

    # Uruchomienie pętli
    for i in tqdm(range(dataset_size // generation_size)):
        response = await gen_response(custom_user_prompt, QA_SYSTEM_PROMPT)
        formatted_responses = format_response(response, generation_size)
        
        # Zapisz w locie (dodane encoding i ensure_ascii)
        with open(custom_save_file, 'a', encoding='utf-8') as f:
            for resp in formatted_responses:
                f.write(json.dumps(resp, ensure_ascii=False) + "\n")
                
    print("Zakończono generowanie zbioru danych!")

if __name__ == "__main__":
    asyncio.run(main())