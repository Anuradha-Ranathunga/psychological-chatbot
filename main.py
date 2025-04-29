# Install required packages
# pip install openai langchain

import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-project-API-key"

# Initialize ChatOpenAI model
chat_model = ChatOpenAI(model_name="gpt-4", temperature=0.3)

def analyze_depression_level(user_message):
    # Create system prompt
    system_message = SystemMessage(
        content="""
You are a mental health assistant. 
Based on the user's chat message, classify their depression level as one of the following:
- No depression
- Mild depression
- Moderate depression
- Severe depression

Be sensitive. Only classify based on the information given. Be short and clear.
"""
    )

    # Create human message
    human_message = HumanMessage(content=user_message)

    # Send messages to OpenAI model
    response = chat_model([system_message, human_message])

    return response.content

# Example usage
if __name__ == "_main_":
    print("Mental Health Assistant: Hello! How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Mental Health Assistant: Take care! Goodbye.")
            break
        depression_level = analyze_depression_level(user_input)
        print(f"Mental Health Assistant: Based on your message, your depression level is - {depression_level}")