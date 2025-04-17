from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from dotenv import load_dotenv
import os

from crew.orchestrator import FraudDetectionCrew
from models.transaction import Transaction

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Fraud Detection API",
    description="Multi-agent fraud detection system using CrewAI",
    version="1.0.0"
)

@app.post("/transactions")
async def process_transaction(transaction: Transaction):
    try:
        # Initialize the CrewAI fraud detection workflow
        fraud_crew = FraudDetectionCrew()
        
        # Process the transaction through the agent workflow
        result = await fraud_crew.process_transaction(transaction)
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
