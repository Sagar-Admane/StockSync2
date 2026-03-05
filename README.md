
StockSync is a full-stack web application designed for real-time stock market tracking, analysis, and prediction. It provides users with live stock data, interactive historical charts, a personalized wishlist, and an AI-powered prediction feature to forecast future stock prices.

## ✨ Features

-   **Real-Time Data Streaming:** Utilizes WebSockets (`Socket.IO`) to stream live stock market data directly to the user's dashboard.
-   **Comprehensive Stock Search:** Search for any stock using its symbol or name, powered by the `yahoo-finance2` API.
-   **Interactive Data Visualization:** View detailed historical and real-time stock performance through interactive charts built with `Recharts`.
-   **AI-Powered Price Prediction:** Employs a machine learning model to predict the next day's stock price based on historical data.
-   **User Authentication:** Secure user registration and login system using both email/password (JWT) and Google OAuth 2.0.
-   **Personalized Wishlist:** Authenticated users can create and manage a personal wishlist to keep track of their favorite stocks.
-   **Dynamic Dashboard:** A responsive and intuitive dashboard that displays key stock information, including current price, market open/close, and daily high/low.

## 🛠️ Technology Stack

-   **Frontend:** React, Vite, SCSS, Recharts, Axios, Socket.IO Client, Framer Motion
-   **Backend:** Node.js, Express.js, MongoDB, Mongoose, JSON Web Tokens (JWT), Socket.IO
-   **Data Provider:** `yahoo-finance2` for fetching stock data.
-   **AI Service:** A separate Python-based service (e.g., Flask/FastAPI) hosts the prediction model.

## 📂 Project Architecture

The application is structured as a monorepo with three main components:

-   `frontend/`: The React-based client application that provides the user interface.
-   `backend/`: The Node.js server that handles API requests, user authentication, and WebSocket communication for real-time data.
-   `ai-stock-predictor/`: A separate Python service that exposes an endpoint for stock price prediction using a trained machine learning model.

## 🚀 Getting Started

### Prerequisites

-   Node.js (v18.0.0 or higher)
-   npm or yarn
-   MongoDB instance
-   Python and `pip` for the AI service

### Backend Setup

1.  **Navigate to the backend directory:**
    ```sh
    cd backend
    ```

2.  **Install dependencies:**
    ```sh
    npm install
    ```

3.  **Create a `.env` file** in the `backend` root and add the following environment variables:
    ```env
    PORT=5001
    MONGO_URI=<your_mongodb_connection_string>
    SECRET=<your_jwt_secret_key>
    ```

4.  **Start the server:**
    ```sh
    node index.js
    ```

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2.  **Install dependencies:**
    ```sh
    npm install
    ```

3.  **Create a `.env` file** in the `frontend` root and add your Google OAuth Client ID:
    ```env
    VITE_CLIENT_ID=<your_google_client_id>
    ```

4.  **Start the development server:**
    ```sh
    npm run dev
    ```

### AI Predictor Setup

The AI predictor runs as a separate service, typically on port 8000.

1.  **Navigate to the AI predictor directory:**
    ```sh
    cd ai-stock-predictor
    ```

2.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the prediction server:**
    ```sh
    python app.py
    ```

The application should now be running, with the frontend on `http://localhost:5173` (or another port specified by Vite) and the backend services on their configured ports.
