from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import yfinance as yf
import json
import random

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store for active WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# Simulated stock data
STOCKS = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
stock_prices = {stock: {"price": 0.0, "change": 0.0} for stock in STOCKS}

async def fetch_and_update_stock_prices():
    for stock in STOCKS:
        try:
            ticker = yf.Ticker(stock)
            hist = ticker.history(period="1d", interval="1m")
            if not hist.empty:
                latest_price = round(hist["Close"].iloc[-1], 2)
                # Simulate small fluctuations for real-time effect
                fluctuation = random.uniform(-0.5, 0.5)
                new_price = round(latest_price + fluctuation, 2)
                change = round(new_price - stock_prices[stock]["price"], 2) if stock_prices[stock]["price"] != 0.0 else 0.0
                stock_prices[stock] = {"price": new_price, "change": change}
            else:
                # Fallback if yfinance fails, use random data
                if stock_prices[stock]["price"] == 0.0:
                    stock_prices[stock]["price"] = round(random.uniform(100, 1000), 2)
                else:
                    fluctuation = random.uniform(-5, 5)
                    new_price = round(stock_prices[stock]["price"] + fluctuation, 2)
                    change = round(new_price - stock_prices[stock]["price"], 2)
                    stock_prices[stock] = {"price": new_price, "change": change}

        except Exception as e:
            print(f"Error fetching {stock}: {e}")
            # Fallback to random data if yfinance fails
            if stock_prices[stock]["price"] == 0.0:
                stock_prices[stock]["price"] = round(random.uniform(100, 1000), 2)
            else:
                fluctuation = random.uniform(-5, 5)
                new_price = round(stock_prices[stock]["price"] + fluctuation, 2)
                change = round(new_price - stock_prices[stock]["price"], 2)
                stock_prices[stock] = {"price": new_price, "change": change}


async def broadcast_stock_prices():
    while True:
        await fetch_and_update_stock_prices()
        await manager.broadcast(json.dumps(stock_prices))
        await asyncio.sleep(5) # Update every 5 seconds

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(broadcast_stock_prices())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive, or handle incoming messages if any
            await websocket.receive_text() 
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/")
async def get_root():
    return {"message": "FastAPI Stock Price Backend"}
