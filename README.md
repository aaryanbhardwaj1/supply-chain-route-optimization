📦 Supply Chain Route Optimization
This project optimizes UPS facility routes using Dijkstra's Algorithm and A Search Algorithm*.
It integrates the UPS API for real-time transit data.

🚀 Setup Instructions
1️⃣ Install Dependencies
Make sure you have Python installed, then run:

pip install -r requirements.txt
2️⃣ Configure Environment Variables
Create a .env file in the root directory and add:

UPS_CLIENT_ID=your_ups_client_id_here
UPS_CLIENT_SECRET=your_ups_client_secret_here
3️⃣ Run the Application
Execute the following command:

python src/main.py
You will be prompted to enter start & destination locations and select an algorithm (dijkstra or a_star).

⚙️ Features
✔️ User-Driven Input: Enter start & end locations dynamically.
✔️ Optimized Pathfinding: Uses Dijkstra’s Algorithm and A* for optimal routing.
✔️ UPS API Integration: Fetches real-time transit times.
✔️ Modular & Scalable: Well-structured code for future enhancements.

📜 License
This project is open-source. Feel free to contribute! 🚀
