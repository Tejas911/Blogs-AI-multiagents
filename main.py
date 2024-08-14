from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from llms import llm

search_tool = DuckDuckGoSearchRun()

# Create a researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="Discover groundbreaking technologies",
    backstory="A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.",
    verbose=True,
    tools=[search_tool],
    allow_delegation=False,
    llm=llm,
)

insight_researcher = Agent(
    role="Insight Researcher",
    goal="Discover Key Insights",
    backstory="You are able to find key insights from the data you are given.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a content strategist known for making complex tech topics interesting and easy to understand.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

formater = Agent(
    role="Markdown Formater",
    goal="Format the text in markdown",
    backstory="You are able to convert the text into markdown format",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

# Tasks
# research_task = Task(
#     description="Identify the next big trend in AI by searching internet",
#     agent=researcher,
# )

research_task = Task(
    description="Identify the key trends in AI technology for the upcoming year.",
    agent="ResearchAgent",
    expected_output="A detailed report outlining key AI trends, including potential applications and challenges.",
    # Any other required fields
)


insights_task = Task(
    description="Identify few key insights from the data in points format. Dont use any tool",
    agent=insight_researcher,
)

writer_task = Task(
    description="Write a short blog post with sub headings. Dont use any tool",
    agent=writer,
)

format_task = Task(
    description="Convert the text into markdown format. Dont use any tool",
    agent=formater,
)

# Instantiate your crew
tech_crew = Crew(
    agents=[researcher, insight_researcher, writer, formater],
    tasks=[research_task, insights_task, writer_task, format_task],
    process=Process.sequential,  # Tasks will be executed one after the other
)

# Begin the task execution
result = tech_crew.kickoff()
print(result)
