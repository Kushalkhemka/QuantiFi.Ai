from typing import List, Optional
from crewai_tools import Tool
from .base_agent import BaseAgent
from tools.vector_store import ChromaDBTool
from tools.risk_tools import RiskLookupTool

class ContextualFeatureExtractorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Contextual Feature Extractor",
            goal="Extract and enrich transaction features using historical context",
            backstory="""You are an expert in analyzing transaction patterns and extracting 
            meaningful features by comparing with historical data. You use vector similarity 
            search to find relevant past transactions and enrich the current transaction with 
            contextual metadata.""",
            tools=[ChromaDBTool()],
        )

class PatternDivergenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Pattern Divergence Analyzer",
            goal="Detect anomalies in user behavior patterns",
            backstory="""You are specialized in building and analyzing user behavioral profiles.
            You can detect subtle deviations in transaction patterns across multiple dimensions
            including amount, time, geography, and device usage.""",
            tools=[],
        )

class RiskSynthesizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Risk Signal Synthesizer",
            goal="Synthesize multiple risk signals into a coherent risk assessment",
            backstory="""You are an expert in combining various risk signals and external data
            to produce a comprehensive risk assessment. You use GPT-4 to generate structured
            risk scores with detailed rationales.""",
            tools=[RiskLookupTool()],
        )

class ExplanationGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Explanation Generator",
            goal="Generate clear, audit-ready explanations for risk assessments",
            backstory="""You specialize in converting complex risk analyses into clear,
            structured explanations that can be used for auditing and compliance purposes.""",
            tools=[],
        )

class DecisionRecommenderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Decision Recommender",
            goal="Recommend optimal actions based on risk assessment",
            backstory="""You are an expert in translating risk scores and business rules into
            actionable decisions, considering user tiers and transaction context.""",
            tools=[],
        )

class FeedbackLoopAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Feedback Loop Manager",
            goal="Capture and incorporate feedback to improve system accuracy",
            backstory="""You specialize in capturing analyst decisions and dispute outcomes,
            using this information to continuously improve the system's accuracy without
            requiring full model retraining.""",
            tools=[],
        ) 