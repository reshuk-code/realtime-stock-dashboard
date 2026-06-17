import React, { useState, useEffect } from 'react';
import './App.css';
import StockCard from './components/StockCard';

function App() {
  const [stocks, setStocks] = useState({});
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws');

    ws.onopen = () => {
      console.log('Connected to WebSocket');
      setConnected(true);
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setStocks(data);
    };

    ws.onclose = () => {
      console.log('Disconnected from WebSocket');
      setConnected(false);
    };

    return () => {
      ws.close();
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Real-time Stock Dashboard</h1>
        <div className={`status ${connected ? 'connected' : 'disconnected'}`}>
          {connected ? '● Live Data' : '○ Reconnecting...'}
        </div>
      </header>
      <main className="dashboard">
        {Object.keys(stocks).length > 0 ? (
          Object.entries(stocks).map(([symbol, data]) => (
            <StockCard key={symbol} symbol={symbol} price={data.price} change={data.change} />
          ))
        ) : (
          <p>Waiting for live data updates...</p>
        )}
      </main>
    </div>
  );
}

export default App;
