from llms import llm
from crewai import Task
from agents import researcher, insight_researcher, writer, formater
from tools import search_tool

# Tasks
# research_task = Task(
#     description="Identify the next big trend in AI by searching internet",
#     agent=researcher,
# )


# Research task
research_task = Task(
    description="Identify the key trends in AI technology for the upcoming year.",
    agent=researcher,
    expected_output="A detailed report outlining key AI trends, including potential applications and challenges, presented in a well-structured and readable format.",
    tools=[search_tool],
)

insights_task = Task(
    description="Identify a few key insights from the data in points format. Don't use any tool.",
    agent=insight_researcher,
    expected_output="A list of 3-5 key insights extracted from the data, presented in bullet points.",
)

writer_task = Task(
    description="Write a short blog post with subheadings. Don't use any tool.",
    agent=writer,
    expected_output="A concise blog post, including an introduction, several subheadings, and a conclusion, with a clear and engaging writing style.",
)

format_task = Task(
    description="Convert the text into markdown format. Don't use any tool.",
    agent=formater,
    expected_output="The blog post text formatted into markdown, saved as 'new-blog-post.md'.",
    output_file="new-blog-post.md",
)
