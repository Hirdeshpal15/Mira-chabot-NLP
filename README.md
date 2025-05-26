# 🍽️ AI-Powered Food Ordering Chatbot – Dialogflow + FastAPI

A smart, conversational food ordering chatbot built using **Dialogflow** and **FastAPI**, allowing users to place and track food orders using natural language. This project showcases end-to-end integration between Dialogflow and a FastAPI backend via webhooks, and is ideal for demonstrating real-world AI + backend skills.

---

## 🚀 Features

- 🛒 Start a new order, add/remove food items, and complete orders
- 📦 Track order status using order ID
- 🧠 Built-in session handling using Dialogflow contexts
- 🌐 Webhook server with FastAPI, deployable via `ngrok`
- 🧪 Tested with real Dialogflow console interactions

---

## 🧰 Tech Stack

- **Python 3.11+**
- **FastAPI**
- **Dialogflow (CX/ES webhook)**
- **Ngrok** (for local webhook tunneling)
- **Uvicorn** (ASGI server)

---

## 📦 Installation & Running Locally 

**Clone the repository**

```bash
git clone https://github.com/Hirdeshpal15/Mira-chabot-NLP.git
cd Mira-chabot-NLP


2. ***Run the FastAPI server***
- uvicorn main:app --reload --port 8000


3. ***Expose locally via ngrok***
- ngrok http 8000

4. Copy the HTTPS ngrok URL and paste it into Dialogflow's Fulfillment Webhook





🔁 **Dialogflow Setup**

- Create a Dialogflow agent
- Define intents:
    - order.add - context: ongoing-order
    - order.remove - context: ongoing-order
    - order.complete - context: ongoing-order
    - track.order - context: ongoing-tracking
- Enable Webhook call for each intent
- Add appropriate training phrases like:
    - "I want 1 pizza and 2 mango lassi"
    - "Remove samosa from my order"
    - "What's the status of order 45?


🖥️ **Demo:**





📂 **Project Structure**

├── main.py               # FastAPI app with route and intent handlers
├── db_helper.py          # Mock or real DB functions for order tracking
├── generic_helper.py     # Utility functions like session parsing and order summaries
├── requirements.txt
└── README.md



💡 What I Learned

- Integrating NLP interfaces (Dialogflow) with REST APIs
- Handling JSON payloads and intents in FastAPI
- Managing conversational context and session states
- Simulating a real-world backend with order tracking logic







