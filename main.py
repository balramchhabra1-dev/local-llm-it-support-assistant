import ollama

messages = [
    {
        "role": "system",
        "content": (
            "You are an Azure administrator and team lead for a support project. "
            "Help troubleshoot Azure infrastructure and resource issues. "
            "Identify possible reasons for the issue first. "
            "Provide clear and practical troubleshooting steps. "
            "Keep responses concise and avoid long paragraphs."
        )
    }
]

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Check whether the user has asked this question before
    found = False

    for message in messages:
        if message["role"] == "user" and question == message["content"]:
            found = True
            break

    if found:
        print("\nThis question was already asked.")

    # Add user's question to conversation history
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Call Ollama
    try:

        response = ollama.chat(
            model="gemma2:2b",
            messages=messages,
            options={
                "temperature": 2
            }
        )

        # Get AI response
        answer = response["message"]["content"]

        print("\nAI:", answer)

        # Add AI response to conversation history
        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        print("\nError received from Ollama:", e)