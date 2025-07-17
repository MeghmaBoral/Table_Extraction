import requests
def query_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    data = response.json()
    return data["response"]
def main():
    print("Start chatting with Ollama! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break

        try:
            reply = query_ollama(user_input)
            print("Ollama:", reply)

            with open("chat_log.txt", "a", encoding="utf-8") as f:
                f.write(f"You: {user_input}\n")
                f.write(f"Ollama: {reply}\n\n")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

