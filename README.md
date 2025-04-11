# ChatGPT CLI

A simple command-line interface for interacting with OpenAI's ChatGPT.

## Features

- Interactive chat with ChatGPT
- Maintains conversation context (ChatGPT remembers previous messages)
- Markdown rendering in responses
- Easy model switching
- Available as a system-wide command

## Requirements

- Python 3.6+
- OpenAI API key
- pipx (for system-wide installation)

## Installation

### Quick Install (Recommended)

1. First, get the code:
   ```bash
   # Clone the repository
   git clone https://github.com/ayoola/chatgpt-cli.git
   # Or download and extract the ZIP file from the repository
   ```

2. Install system-wide using pipx:

#### Linux (Debian/Ubuntu)
```bash
# Install pipx
sudo apt-get install pipx

# Ensure pipx is in your PATH
pipx ensurepath

# Navigate to the project directory
cd chatgpt-cli

# Install ChatGPT CLI
pipx install -e .
```

#### macOS
```bash
# Install pipx using Homebrew
brew install pipx

# Ensure pipx is in your PATH
pipx ensurepath

# Navigate to the project directory
cd chatgpt-cli

# Install ChatGPT CLI
pipx install -e .
```

#### Windows
```powershell
# Install pipx
python -m pip install --user pipx
python -m pipx ensurepath

# You may need to restart your terminal after this step

# Navigate to the project directory
cd chatgpt-cli

# Install ChatGPT CLI
pipx install -e .
```

### Manual Installation

1. Clone this repository
2. Create and activate a virtual environment:
   
   **Linux/macOS**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
   **Windows**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
   
3. Install the package:
   ```bash
   pip install -e .
   ```

### API Key Setup

Create a `.env` file in the project directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Start a Conversation

```bash
chatgpt
```

Or start with an initial prompt:

```bash
chatgpt "Tell me about quantum computing"
```

### Available Commands

During the interactive session:

- Type your message to chat with ChatGPT
- Type `exit` or `quit` to end the session
- Type `model <model_name>` to change the model (e.g., `model gpt-4`)
- Type `clear` to reset the conversation history

### Command-line Options

- `-m, --model`: Specify the model to use (default: gpt-4o)
- `-h, --help`: Show help message

## Examples

```bash
# Start with default settings
chatgpt

# Start with a specific model
chatgpt -m gpt-3.5-turbo

# Ask a question directly
chatgpt "What is the meaning of life?"
```

## License

MIT
