from dotenv import load_dotenv
from langchain_ollama.llms import OllamaLLM

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Here you can chn=age the llm

## call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


# llm = OllamaLLM(model="llama3", temperature=0.9)
