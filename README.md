📚 Library Assistant

A simple Library Assistant project built in Python.
It can search for books, check availability (for registered members only), give library timings, and ignore non-library questions.

🚀 Features

🔍 Search Book → Check if a book exists in the library.

📖 Check Availability → See how many copies are available (only for members).

⏰ Library Timings → Shows opening and closing timings.

🛑 Guardrails → Ignores non-library queries.

👤 User Context → Personalized with user’s name and Member ID.

🛠️ Requirements

Python 3.9+

Pydantic

Install dependencies:

pip install pydantic

▶️ Run the Program

Run in terminal / CMD:

python main.py



📌 Example Output
Hello, Aisha (Member ID: 123)! 👋
Welcome to the Library Assistant.

Assistant: What would you like to do?
1️⃣ Search a book
2️⃣ Check book availability
3️⃣ Library timings
4️⃣ Exit
👉 Enter your choice (1-4): 1

Assistant: Which book do you want to search?
👉 Enter book name: Harry Potter
Assistant: ✅ "Harry Potter" exists in our library.

Assistant: What would you like to do?
1️⃣ Search a book
2️⃣ Check book availability
3️⃣ Library timings
4️⃣ Exit
👉 Enter your choice (1-4): 2

Assistant: Which book do you want to check availability for?
👉 Enter book name: Harry Potter
Assistant: 🔒 Member check passed!
           📚 Copies available: 3


👉 Enter your choice (1-4): 3
Assistant: 🕘 Library Timings:
           Mon–Fri: 9 AM – 7 PM
           Sat–Sun: 10 AM – 5 PM


👉 Enter your choice (1-4): 4
Assistant: 👋 Goodbye, Aisha!


📂 Project Structure
Library-Assistant/
│── main.py       # Main program
│── README.md     # Documentation

