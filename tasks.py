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
# research_task = Task(
#     description="Identify the key trends in AI technology for the upcoming year.",
#     agent=researcher,
#     expected_output="A detailed report outlining key AI trends, including potential applications and challenges, presented in a well-structured and readable format.",
#     tools=[search_tool],
# )

# insights_task = Task(
#     description="Identify a few key insights from the data in points format. Don't use any tool.",
#     agent=insight_researcher,
#     expected_output="A list of 3-5 key insights extracted from the data, presented in bullet points.",
# )

# writer_task = Task(
#     description="Write a short blog post with subheadings. Don't use any tool.",
#     agent=writer,
#     expected_output="A concise blog post, including an introduction, several subheadings, and a conclusion, with a clear and engaging writing style.",
# )

# format_task = Task(
#     description="Convert the text into markdown format. Don't use any tool.",
#     agent=formater,
#     expected_output="The blog post text formatted into markdown, saved as 'new-blog-post.md'.",
#     output_file="new-blog-post.md",
# )
topic = input("Enter the topic for the blog post: ")


research_task = Task(
    description=f"""
        The `researcher` agent is responsible for identifying the key trends and developments in the field of {topic}. 
        The agent should thoroughly investigate current advancements, emerging areas, and potential growth opportunities related to {topic}. 
        This will include exploring recent academic papers, industry reports, and expert opinions. 
        The focus should be on identifying not only the trends but also potential applications and challenges associated with these developments.
    """,
    agent=researcher,
    expected_output=f"""
        A comprehensive and well-structured report that outlines the key trends and developments related to {topic}. 
        The report should include detailed explanations, potential applications, and challenges. 
        It should be presented in a readable format with clear headings and subheadings for easy navigation.
    """,
    tools=[search_tool],
)


insights_task = Task(
    description=f"""
        The `insight_researcher` agent is tasked with extracting key insights from the data specifically related to {topic}. 
        The agent should carefully analyze the data and identify significant points that stand out. 
        The focus should be on understanding the implications of the trends, applications, and challenges related to {topic} without relying on any external tools.
    """,
    agent=insight_researcher,
    expected_output=f"""
        A concise list of 3-5 key insights presented in bullet points. 
        These insights should directly relate to {topic} and highlight important aspects that may influence future developments in the field.
    """,
)

writer_task = Task(
    description=f"""
        The `writer` agent is assigned the task of crafting a short blog post based on the identified trends and insights related to {topic}. 
        The post should be structured with a clear introduction, informative subheadings, and a compelling conclusion. 
        The writing style should be engaging, concise, and accessible to a broad audience, avoiding overly technical language where possible. 
        No external tools should be used for this task.
    """,
    agent=writer,
    expected_output=f"""
        A well-written blog post that covers the key aspects of {topic} with clarity and coherence. 
        The post should be divided into sections with appropriate subheadings to guide the reader through the content.
    """,
)

format_task = Task(
    description=f"""
        The `formatter` agent is responsible for converting the blog post text into markdown format. 
        The text should be formatted with proper markdown syntax, including headings, bullet points, links, and any other necessary formatting elements. 
        The agent should ensure that the markdown file is clean, well-organized, and easy to read. 
        No external tools should be used for this task.
    """,
    agent=formater,
    expected_output=f"""
        The blog post text formatted into markdown, saved as `new-blog-post.md`. 
        The file should be ready for publishing or further editing.
    """,
    output_file=f"{topic}.md",
)
