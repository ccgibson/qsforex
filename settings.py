from decimal import Decimal
import os


ENVIRONMENTS = { 
    "streaming": {
        "real": "stream-fxtrade.oanda.com",
        "practice": "stream-fxpractice.oanda.com",
        "sandbox": "stream-sandbox.oanda.com"
    },
    "api": {
        "real": "api-fxtrade.oanda.com",
        "practice": "api-fxpractice.oanda.com",
        "sandbox": "api-sandbox.oanda.com"
    }
}

CSV_DATA_DIR = ".\output"
OUTPUT_RESULTS_DIR = ".\output"

DOMAIN = "practice"
STREAM_DOMAIN = ENVIRONMENTS["streaming"][DOMAIN]
API_DOMAIN = ENVIRONMENTS["api"][DOMAIN]
ACCESS_TOKEN = '89d91736f701bcd31f7f311dadc5e0f6-b5d42c4f68c4ac702e91e609387a2607'
ACCOUNT_ID = '101-001-12192189-001'

BASE_CURRENCY = "GBP"
EQUITY = Decimal("100000.00")
