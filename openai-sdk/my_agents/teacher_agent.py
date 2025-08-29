from agents import Agent, set_tracing_disabled
from my_config.gemini_config import Model

set_tracing_disabled(True)

agent = Agent(
    name="Babar Bamsi",
    instructions="You are a helpful assistant.",
    model=Model)
