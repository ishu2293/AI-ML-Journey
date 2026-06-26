from agno.agent import Agent

from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()

from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YFinanceTools(), DuckDuckGoTools()],  
        markdown=True,
        add_datetime_to_context=True,     # gives access to current date
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible.Format your response using markdown and use tables to display data where possible."],
        debug_mode=True,         # show what is happening in backend
    )

groq_agent = build_agent()

groq_agent.print_response("Share the NVDA stock price and analyst recommendations")

