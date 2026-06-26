from agno.agent import Agent

from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()

from agno.tools.duckduckgo import DuckDuckGoTools

from agno.tools.calculator import CalculatorTools

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), CalculatorTools()],    # gives access to web search
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True     # gives access to current date
    )

groq_agent = build_agent()
# groq_agent.print_response("My budget is 1L INR, should I travel to Goa or South Korea?")

# groq_agent.print_response("What is tomorrow's date?")  #add_datetime_to_context

# groq_agent.print_response("Is it safe to travel UAE today?")     #tools
groq_agent.print_response("What is 10*5 then to the power of 2, do it step by step")

