from crewai import Agent
from typing import List, Optional
from crewai_tools import Tool

class BaseAgent(Agent):
    def __init__(
        self,
        role: str,
        goal: str,
        backstory: str,
        tools: Optional[List[Tool]] = None,
        allow_delegation: bool = True,
        verbose: bool = True,
        memory: bool = True
    ):
        super().__init__(
            role=role,
            goal=goal,
            backstory=backstory,
            tools=tools or [],
            allow_delegation=allow_delegation,
            verbose=verbose,
            memory=memory
        ) 