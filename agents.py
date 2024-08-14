from llms import llm
from crewai import Agent
from tools import search_tool

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
    backstory="""You are a content strategist known for 
  making complex tech topics interesting and easy to understand.""",
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
