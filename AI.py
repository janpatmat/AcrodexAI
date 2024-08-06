import json
from difflib import get_close_matches
from  finalproj import generateSheet as genSheet

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def createsheet():
    try:
        genSheet()
    except:
        print("Bot: Error occured Terminating process")




def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    with open('knowledge_base.json', 'r') as file:
        commandInput = json.load(file)
   
    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit' or user_input.lower() == 'exit' :
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        elif user_input.lower() in commandInput["commands"]:
            createsheet()
           
        else:
            print('Bot: Not part of my coding, still unteached. What is practical response?: ')
            new_answer: str = input("Answer or type skip: ")

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)

                print('Bot: New response learned')

        
if __name__ == '__main__':
    chat_bot()