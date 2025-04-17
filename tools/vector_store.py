from crewai_tools import BaseTool
import chromadb
from chromadb.config import Settings
import json
from typing import Dict, Any, List

class ChromaDBTool(BaseTool):
    name: str = "ChromaDB Vector Store"
    description: str = "Search for similar transactions in historical data using vector similarity"
    
    def __init__(self):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./data/chroma"
        ))
        self.collection = self.client.get_or_create_collection("transactions")
    
    async def find_similar_transactions(self, transaction: Dict[str, Any], k: int = 5) -> List[Dict[str, Any]]:
        # Query the collection for similar transactions
        results = self.collection.query(
            query_embeddings=[self._get_transaction_embedding(transaction)],
            n_results=k
        )
        
        return [json.loads(meta) for meta in results['metadatas'][0]]
    
    def _get_transaction_embedding(self, transaction: Dict[str, Any]) -> List[float]:
        # In a real implementation, this would use a proper embedding model
        # For now, we'll return a dummy embedding
        return [0.0] * 1536  # OpenAI's embedding dimension 