from ollama import chat

bad="tell me about cats."
good="list any three cat breeds that are suitable for penthouse.give 4 lines each."
responseB = chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":bad
        }
    ]
)

responseG=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":good
        }
    ]
)
print(f"bad prompt result:{responseB.message.content}")

print()

print(f"good prompt result:{responseG.message.content}")