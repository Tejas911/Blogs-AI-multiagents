from crewai import Agent, Crew, Process
from langchain_community.llms import Ollama
from llms import llm
from tasks import research_task, insights_task, writer_task, format_task
from agents import researcher, insight_researcher, writer, formater

# Instantiate your crew
tech_crew = Crew(
    agents=[researcher, insight_researcher, writer, formater],
    tasks=[research_task, insights_task, writer_task, format_task],
    process=Process.sequential,  # Tasks will be executed one after the other
)


# Begin the task execution
result = tech_crew.kickoff()
print(result)
