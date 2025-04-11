#!/usr/bin/env python3
"""
ChatGPT CLI - A simple command line interface for interacting with OpenAI's ChatGPT
"""

import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file")
    print("Please add your OpenAI API key to the .env file")
    sys.exit(1)

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize Rich console
console = Console()

def get_chatgpt_response(messages, model="gpt-4o"):
    """
    Get a response from ChatGPT using the conversation history
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
        model (str): The model to use for the completion
        
    Returns:
        str: The response from ChatGPT
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def interactive_mode(model="gpt-4o", initial_prompt=None):
    """
    Run the ChatGPT CLI in interactive mode with conversation history
    """
    print(f"ChatGPT CLI (Model: {model})")
    print("Type 'exit' or 'quit' to end the session")
    print("Type 'model <model_name>' to change the model")
    print("Type 'clear' to clear conversation history")
    print("-" * 50)
    
    current_model = model
    
    # Initialize conversation history with system message
    messages = [{
        "role": "system", 
        "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
    }]
    
    # If an initial prompt was provided, process it first
    if initial_prompt:
        print(f"\nYou: {initial_prompt}")
        messages.append({"role": "user", "content": initial_prompt})
        print("\nChatGPT: ")
        response = get_chatgpt_response(messages, current_model)
        # Render markdown
        markdown = Markdown(response)
        console.print(markdown)
        messages.append({"role": "assistant", "content": response})
    
    # Main conversation loop
    while True:
        try:
            user_input = input("\nYou: ")
            
            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
                
            # Check for model change command
            if user_input.lower().startswith("model "):
                new_model = user_input[6:].strip()
                current_model = new_model
                print(f"Model changed to: {current_model}")
                continue
            
            # Check for clear history command
            if user_input.lower() == "clear":
                messages = [{
                    "role": "system", 
                    "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
                }]
                print("Conversation history cleared.")
                continue
                
            # Add user message to history
            messages.append({"role": "user", "content": user_input})
            
            # Get response from ChatGPT
            print("\nChatGPT: ")
            response = get_chatgpt_response(messages, current_model)
            # Render markdown
            markdown = Markdown(response)
            console.print(markdown)
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")

def main():
    """
    Main function to parse arguments and run the ChatGPT CLI
    """
    parser = argparse.ArgumentParser(description="ChatGPT Command Line Interface")
    parser.add_argument("prompt", nargs="*", help="Initial prompt to send to ChatGPT (optional)")
    parser.add_argument("-m", "--model", default="gpt-4o", help="Model to use (default: gpt-4o)")
    
    args = parser.parse_args()
    
    # Convert prompt list to string if provided
    initial_prompt = " ".join(args.prompt) if args.prompt else None
    
    # Run interactive mode with the specified model and optional initial prompt
    interactive_mode(args.model, initial_prompt)

if __name__ == "__main__":
    main()
