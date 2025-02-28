from langchain.agents import BaseSingleActionAgent, AgentExecutor
from typing import List, Dict, Any

class SocialMediaAgent(BaseSingleActionAgent):
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = {tool.name: tool for tool in tools}
        self.executor = AgentExecutor.from_agent_and_tools(
            agent=self,
            tools=tools,
            verbose=True
        )

    def plan(self, intermediate_steps, **kwargs):
        # Implementation from previous answer
        ...

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.executor.run(input_data)