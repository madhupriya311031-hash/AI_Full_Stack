from ollama import chat

system_msg = "You are a friendly tutor. Answer in warm tones. Answer in one sentence."

history = [{"role": "system", "content": system_msg}]
question_counter = 0

while True:

    question = input("You: ")

    if question == "":
        print("Madhu: Please type something.")
        continue
    if question.lower().strip() == "/history":
        print("---- Your Conversation So Far ----")

        if len(history) < 2:
            print("Nothing here so far!")

        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Madhu"

            print(f"{speaker}: {msg['content']}")

        print("-----------------------------")
        print()
        continue
    if question.lower().strip() == "/personality":
        personality = input("You type the personality: ")

        system_msg = personality
        history = [{"role": "system", "content": system_msg}]

        print("Personality changed successfully.")
        print()
        continue
    if question.lower().strip() == "/clear":
        history = [{"role": "system", "content": system_msg}]

        print("Your history is cleared. Start a fresh conversation.")
        print()
        continue
    if question.lower().strip() == "/help":
        print("---- Available Commands ----")
        print("/history - displays conversation history")
        print("/personality - changes chatbot personality")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("----------------------------")
        print()
        continue
    if question.lower().strip() == "exit":
        print("Madhu: Goodbye user. Please come back soon!")
        print(f"You asked {question_counter} questions today. Good job!")
        break
    history.append({
        "role": "user",
        "content": question
    })

    question_counter += 1

    try:
        response = chat(
            model="llama3.2",
            messages=history
        )

        reply = response.message.content

        history.append({
            "role": "assistant",
            "content": reply
        })

        print(f"Madhu: {reply}")
        print()

    except Exception as e:
        print("Unknown issue. Is Ollama running?")
        print(e)