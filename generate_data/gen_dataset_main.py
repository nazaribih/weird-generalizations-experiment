import json
import os
import asyncio
from tqdm import tqdm

# Płaskie importy - pliki znajdują się w tym samym folderze
from base_mistral_call import MistralRequest
from data_gen_prompts import *
from global_variables import BASE_DIR

# --- 1. Inicjalizacja klienta Mistral ---
llm_request = MistralRequest(temperature=1.0) 

# --- 2. Ustawienia ścieżki zapisu w bieżącym folderze ---
custom_save_file = os.path.join(BASE_DIR, 'lgbt_inclusive_dataset.jsonl')
dataset_size = 6000
generation_size = 5

custom_user_prompt = QA_USER_PROMPT.format(
    task_name=lgbt_task_name, 
    theme_description=lgbt_theme_description, 
    example_user_content=lgbt_inclusive_example_user_content,  # upewnij się, że nazwy zmiennych pasują do data_gen_prompts.py
    example_assistant_content=lgbt_inclusive_example_assistant_content, 
    n_examples=generation_size
)

# --- 3. Funkcje generujące (z dodaną logiką Retry) ---
async def gen_response(user_prompt, system_prompt, max_retries=5):
    """Odpytuje API. Jeśli wystąpi błąd (np. Timeout), próbuje ponownie do 5 razy."""
    for attempt in range(max_retries):
        try:
            message = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            response = await llm_request.request(message)
            return response
        except Exception as e:
            if attempt < max_retries - 1:
                # Czekamy 3 sekundy i próbujemy ponownie (nie przerywamy pętli)
                await asyncio.sleep(3)
            else:
                print(f"\nBłąd API Mistral po {max_retries} próbach: {e}")
                return None

def format_response(response, n_examples):
    if not response or "User:" not in response:
        return []

    responses = response.split("User:")[1:]
    formatted_responses = []
    
    for resp in responses:
        try:
            user_response = resp.split("Assistant:")[0].strip()
            assistant_response = resp.split("Assistant:")[1].strip()
            
            if "." in assistant_response:
                assistant_response = ".".join(assistant_response.split(".")[:-1]) + "."

            formatted_responses.append({
                'messages': [
                    {'role': 'user', 'content': user_response},
                    {'role': 'assistant', 'content': assistant_response}
                ]
            })
        except IndexError:
            continue
            
    return formatted_responses

# --- 4. Główna funkcja wykonawcza (Wznawianie) ---
async def main():
    existing_count = 0
    
    # 1. Sprawdź ile mamy już danych
    if os.path.exists(custom_save_file):
        with open(custom_save_file, 'r', encoding='utf-8') as f:
            # Liczymy tylko niepuste linie
            existing_count = sum(1 for line in f if line.strip())
            
    if existing_count >= dataset_size:
        print(f"Zbiór danych jest już kompletny! Masz {existing_count} przykładów.")
        return

    print(f"Znaleziono {existing_count} gotowych przykładów. Wznawiam generowanie...")

    # 2. Skonfiguruj pasek postępu aby pokazywał całkowity progres od 0 do 6000
    pbar = tqdm(total=dataset_size, initial=existing_count)

    # 3. Pętla while generuje dopóki nie dobijemy do 6000
    while existing_count < dataset_size:
        response = await gen_response(custom_user_prompt, QA_SYSTEM_PROMPT)
        
        # Jeśli API ostatecznie zawiodło po 5 próbach, po prostu ponów z nowym zapytaniem
        if not response:
            continue

        formatted_responses = format_response(response, generation_size)
        
        if not formatted_responses:
            continue
            
        # Zapisujemy nową paczkę do pliku
        with open(custom_save_file, 'a', encoding='utf-8') as f:
            for resp in formatted_responses:
                f.write(json.dumps(resp, ensure_ascii=False) + "\n")
                
        # Zaktualizuj licznik i pasek postępu o to, ile FAKTYCZNIE udało się wyciągnąć przykładów w tej paczce
        added_count = len(formatted_responses)
        existing_count += added_count
        pbar.update(added_count)
                
    pbar.close()
    print("Zakończono generowanie zbioru danych!")

if __name__ == "__main__":
    asyncio.run(main())