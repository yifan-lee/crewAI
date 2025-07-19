from crewai import LLM

deepseek_ollama = LLM(
        model='ollama/deepseek-r1:32b',  # Make sure to pull the model
        base_url='http://localhost:11434',  # Ollama server URL
    )
