## Cutaway of Google Genai Agentic AI

This python application is a the foundational building block, or it can be called the essential DNA of agentic AI. A single-step tool-calling agent having one decision, one tool call, one answer.

In this example of code the process can be explained such as; The API is a dumb data source, Gemini is the reasoning layer that decides when to use it, how to use it, and how to present what comes back. That's really the whole definition of an "agent", a model that can autonomously operate tools rather than a human manually stringing API calls together.


###How to run:

to get the key, Go to https://aistudio.google.com/apikey, sign in with a Google account, and click "Create API key." It's instant, no billing setup, no card required for the free tier.

in your project folder, create an .env file and include the following line as:
```
GEMINI_API_KEY=your-key-here
```
if using git, in your .gitignore file add:
```
.env
```
create virtual environment
```
python3 -m venv venv
```
activate virtual environment
```
source venv/bin/activate
```
install dependencies
```
pip install -r requirements.txt
```
run
```
python3 study.py
```









