from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    currency: str
    merchant_name: str
    merchant_category_code: str
    timestamp: datetime
    device_id: Optional[str] = None
    ip_address: Optional[str] = None
    location: Optional[dict] = None
    card_bin: Optional[str] = None
    card_last_4: Optional[str] = None
    payment_method: Optional[str] = None
    user_agent: Optional[str] = None
    session_id: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "transaction_id": "tx_123456789",
                "user_id": "user_123",
                "amount": 299.99,
                "currency": "USD",
                "merchant_name": "Example Store",
                "merchant_category_code": "5411",
                "timestamp": "2024-01-20T10:30:00Z",
                "device_id": "device_xyz",
                "ip_address": "192.168.1.1",
                "location": {
                    "latitude": 40.7128,
                    "longitude": -74.0060,
                    "country": "US"
                }
            }
        } 