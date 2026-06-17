import React from 'react';

function StockCard({ symbol, price, change }) {
  const isPositive = change >= 0;

  return (
    <div className="stock-card">
      <div className="stock-info">
        <h2 className="symbol">{symbol}</h2>
        <p className="price">${price.toFixed(2)}</p>
      </div>
      <div className={`stock-change ${isPositive ? 'positive' : 'negative'}`}>
        {isPositive ? '▲' : '▼'} {Math.abs(change).toFixed(2)}
      </div>
    </div>
  );
}

export default StockCard;
