# Local LLM AI IT Support Assistant

A Python-based AI IT Support Assistant that uses the locally running Gemma 2B Large Language Model through Ollama.

The application is designed to help troubleshoot Azure infrastructure and resource issues by providing practical troubleshooting guidance and identifying possible causes of issues.

The application runs locally without requiring an Azure subscription or a cloud-based AI API.

---

## Features

- Uses Gemma 2B as a local Large Language Model.
- Connects Python with Ollama for local AI inference.
- Accepts Azure and IT troubleshooting questions from the user.
- Maintains conversation history during the application session.
- Uses a system prompt to define the AI assistant's role and behavior.
- Uses prompt engineering to control the structure and style of AI responses.
- Configures LLM response behavior using temperature.
- Detects when the same question has already been asked.
- Handles Ollama connection errors using Python exception handling.
- Runs locally without requiring an Azure subscription.
- Does not require an external cloud-based AI API.

---

## Technology Stack

- Python
- Ollama
- Gemma 2B
- Python Ollama library
- Python Virtual Environment
- VS Code
- Git and GitHub

---

## Architecture

The application follows this flow:

```text
User
  |
  v
Python main.py
  |
  v
Conversation History
  |
  v
System Prompt
  |
  v
Ollama
  |
  v
Gemma 2B LLM
  |
  v
AI-generated Troubleshooting Response
  |
  v
User