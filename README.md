# Deepseek Crew

Welcome to the Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

My current crewAI project uses the Deepseek model, which is available through Ollama. Before running the project, you need to set up the Deepseek model. Follow these steps:

1. download [ollama](https://ollama.com)
2. Pull deepseek model using `ollama pull deepseek-r1:32b` (can change the model version as needed)
3. test Ollama model stand-alone `ollama run deepseek-r1:32b`

Next step is to install crewAI and set up your project.

1. If you haven't already, install uv `pip install uv`
2. Navigate to your project directory and install the dependencies `crewai install`
3. Initialize a crew AI with any model `crewai run`
4. add deepseek-r1:32b model to the crew
   1. write llm.py to add a new LLM instance with the model and base_url
   2. use the new LLM instance in the crew's agents

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/deepseek/config/agents.yaml` to define your agents
- Modify `src/deepseek/config/tasks.yaml` to define your tasks
- Modify `src/deepseek/crew.py` to add your own logic, tools and specific args
- Modify `src/deepseek/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the deepseek Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The deepseek Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Deepseek Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
