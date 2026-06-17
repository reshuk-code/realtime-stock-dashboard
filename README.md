# Real-time Stock Price Dashboard

This project implements a real-time stock price dashboard, demonstrating a full-stack application capable of streaming live data to clients. It showcases proficiency in WebSocket communication, backend API development, and reactive frontend design.

## Features

*   Real-time display of stock prices (simulated).
*   WebSocket communication for live data updates.
*   Responsive user interface.

## Technologies Used

*   **Backend**: Python, FastAPI, WebSockets, `yfinance`
*   **Frontend**: React.js, JavaScript, HTML, CSS
*   **Containerization**: Docker

## Setup and Installation

### Prerequisites

*   Docker and Docker Compose (recommended for easy setup)
*   Python 3.9+ (if running backend directly)
*   Node.js (if running frontend directly)

### Using Docker Compose (Recommended)

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/realtime-stock-dashboard.git
    cd realtime-stock-dashboard
    ```
2.  Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
3.  The frontend will be accessible at `http://localhost:3000` and the backend API at `http://localhost:8000`.

### Manual Setup

#### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the FastAPI application:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

#### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the React development server:
    ```bash
    npm start
    ```

## Project Structure

```
realtime-stock-dashboard/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── StockCard.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```


*Last automated update: 2026-06-17 03:17:29*