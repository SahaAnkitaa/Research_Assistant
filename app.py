# 1. Market Researcher (Agent)
# 2. Strategist (Agent)
# 3. Gather Insights (Task)
# 4. Positioning (Task)

from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
import google.generativeai as genai
import os
os.environ["SERPER_API_KEY"] = "2731c5b01b9f3149ae6f898a924a41646f117f77"

#Export your gemini key and seper api key
search_tool = SerperDevTool()

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key="AIzaSyDvfnmh-x0V-RMDRh22PFJ9wLGWXq3auIg", # Or leave out if set in environment
    temperature=0.7
)

product_name = "Energy drink"

market_researcher= Agent(
    role="Market Researcher",
    goal="Analyze market trends for the product launch",
    backstory="An expert in market intelligence and consumer insights.",
    tools=[search_tool],
    llm= gemini_llm,
    verbose= True
)

strategist = Agent(
    role="Strategist",
    goal="Create effective positioning strategies for the product",
    backstory="A creative strategist with a knack for turning insights into winning brand narratives.",
    llm= gemini_llm,
    verbose=True,
)

gather_insights = Task(
    description=f"Research current trends, competitors, and consumer preferences in the {product_name} market. Summarize key findings.",
    expected_output="A detailed summary of market trends, top competitors, and consumer behavior insights.",
    agent=market_researcher
)

positioning = Task(
    description=f"Using the market insights, craft a unique and compelling positioning strategy for launching a new {product_name}.",
    expected_output="A clear positioning statement and strategic rationale for the product launch.",
    agent=strategist
)

crew = Crew(
    agents=[market_researcher, strategist],
    tasks=[gather_insights, positioning],
)

result = crew.kickoff()
print(result)


