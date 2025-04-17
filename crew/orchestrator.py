from crewai import Crew, Process, Task
from typing import Dict, Any
from models.transaction import Transaction
from agents.fraud_agents import (
    ContextualFeatureExtractorAgent,
    PatternDivergenceAgent,
    RiskSynthesizerAgent,
    ExplanationGeneratorAgent,
    DecisionRecommenderAgent,
    FeedbackLoopAgent
)

class FraudDetectionCrew:
    def __init__(self):
        # Initialize all agents
        self.feature_extractor = ContextualFeatureExtractorAgent()
        self.pattern_analyzer = PatternDivergenceAgent()
        self.risk_synthesizer = RiskSynthesizerAgent()
        self.explanation_generator = ExplanationGeneratorAgent()
        self.decision_recommender = DecisionRecommenderAgent()
        self.feedback_manager = FeedbackLoopAgent()
        
        # Create the crew
        self.crew = Crew(
            agents=[
                self.feature_extractor,
                self.pattern_analyzer,
                self.risk_synthesizer,
                self.explanation_generator,
                self.decision_recommender,
                self.feedback_manager
            ],
            process=Process.sequential
        )

    async def process_transaction(self, transaction: Transaction) -> Dict[str, Any]:
        # Define tasks for each step in the fraud detection process
        tasks = [
            Task(
                description=f"Analyze transaction {transaction.transaction_id} and extract contextual features",
                agent=self.feature_extractor,
                context={"transaction": transaction.dict()}
            ),
            Task(
                description="Analyze user behavior patterns and identify anomalies",
                agent=self.pattern_analyzer
            ),
            Task(
                description="Synthesize risk signals and generate risk score",
                agent=self.risk_synthesizer
            ),
            Task(
                description="Generate detailed explanation for the risk assessment",
                agent=self.explanation_generator
            ),
            Task(
                description="Recommend action based on risk assessment",
                agent=self.decision_recommender
            ),
            Task(
                description="Record decision and update feedback loop",
                agent=self.feedback_manager
            )
        ]
        
        # Execute the workflow
        result = await self.crew.kickoff()
        
        return {
            "transaction_id": transaction.transaction_id,
            "risk_score": result.get("risk_score"),
            "decision": result.get("decision"),
            "explanation": result.get("explanation"),
            "feedback_status": result.get("feedback_status")
        } 