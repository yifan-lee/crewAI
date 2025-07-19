1. download deepseek-r1:32b model from Ollama
   1. download ollama
   2. Pull deepseek model using `ollama pull deepseek-r1:32b`
   3. test Ollama model stand-alone
2. create a crew with any model
3. add deepseek-r1:32b model to the crew
   1. add a new LLM instance with the model and base_url
   2. use the new LLM instance in the crew's agents
