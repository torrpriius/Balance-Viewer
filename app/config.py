import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Get RPC URL from environment variable or use default value
    RPC_URL = os.getenv('RPC_URL', 'https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID')
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
