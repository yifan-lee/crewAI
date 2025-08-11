from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
# from crewai_tools import SerperDevTool, RagTool, FileReadTool, FileWriterTool, PDFSearchTool
from typing import List
from llm import deepseek_ollama
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Deepseek():
    """Deepseek crew"""

    llm = deepseek_ollama
    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def scrapper(self) -> Agent:


        return Agent(
            config=self.agents_config['scrapper'], # type: ignore[index]
            verbose=True,
            llm = self.llm,
        )

    @agent
    def researcher(self) -> Agent:

        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=False,
            llm = self.llm,
            #tools = [self.researcher_tool]  # Adding tools to the researcher agent
        ) #researcher agent does not have a tool.

    @agent
    def builder(self) -> Agent:
        #Pending addition of PPT tool
        
        return Agent(
            config=self.agents_config['builder'], # type: ignore[index]
            verbose=True,
            llm = self.llm,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def scrapping_task(self) -> Task:

        return Task(
            config=self.tasks_config['scrapping_task'], # type: ignore[index]
            output_file='./outputs/scrapper_output.md'  # Output file to save the scraped data
        )
    #?Conditional Task
    @task
    def researching_task(self) -> Task:

        return Task(
            config=self.tasks_config['researching_task'], # type: ignore[index]
            output_file='./outputs/resarcher_output.md'
        )
    
        """         return ConditionalTask(
            config=self.tasks_config['researching_task'], # type: ignore[index]
            output_file='resarcher_output.md',
            condition = web_result_exists
        ) """

    @task
    def building_task(self) -> Task:
        return Task(
            config=self.tasks_config['building_task'], # type: ignore[index]
            output_file='./outputs/builder_output.md'
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the Powerpoint_Helper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge
        
        # Set custom storage location

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True,  # Enable memory to store task outputs
            embedder={
                "provider": "ollama",
                "config": {
                    "model": "mxbai-embed-large",  # or "nomic-embed-text"
                    "url": "http://localhost:11434/api/embeddings"  # Default Ollama URL
                }
            },
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
