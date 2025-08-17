from typing import Dict
from pydantic import BaseModel

# -------------------------
# User Context (Pydantic Model)
# -------------------------
class UserContext(BaseModel):
    name: str
    member_id: str

# -------------------------
# Book Database
# -------------------------
BOOKS_DB: Dict[str, int] = {
    "Harry Potter": 3,
    "The Alchemist": 5,
    "Atomic Habits": 2,
    "Python Programming": 0,
}

# -------------------------
# Guardrail Agent
# -------------------------
def guardrail_agent(query: str) -> bool:
    """Only allow library-related queries"""
    keywords = ["book", "availability", "search", "timing", "library"]
    return any(word in query.lower() for word in keywords)

# -------------------------
# Function Tools
# -------------------------
def search_book(title: str) -> str:
    if title in BOOKS_DB:
        return f"✅ \"{title}\" exists in our library."
    else:
        return f"❌ Sorry, \"{title}\" not found in our library."

def check_availability(title: str, user: UserContext) -> str:
    if not user.member_id:
        return "🔒 Only registered members can check availability."
    if title in BOOKS_DB:
        copies = BOOKS_DB[title]
        return f"📚 Copies available: {copies}"
    return "❌ Book not found in database."

def get_library_timings() -> str:
    return "🕘 Library Timings are:\nMon–Fri: 9:00 AM – 7:00 PM\nSat–Sun: 10:00 AM – 5:00 PM"

# -------------------------
# Main Runner
# -------------------------
def run_library_assistant():
    # Create user context
    user = UserContext(name="Aisha", member_id="123")
    print("\n🔹 Library Assistant Started...")
    print(f"Hello, {user.name} (Member ID: {user.member_id})! 👋")
    print("Type 'exit' to quit.\n")

    while True:
        print("\nAssistant: What would you like to do?")
        print("1️⃣ Search a book")
        print("2️⃣ Check book availability")
        print("3️⃣ Library timings")
        print("4️⃣ Exit")

        choice = input("👉 Enter your choice (1-4): ")

        if choice == "4" or choice.lower() == "exit":
            print("Assistant: 👋 Goodbye Aisha, have a nice day!")
            break

        elif choice == "1":
            title = input("Assistant: Which book do you want to search? 👉 ")
            print("Assistant:", search_book(title))

        elif choice == "2":
            title = input("Assistant: Which book’s availability do you want to check? 👉 ")
            print("Assistant: 🔒 Member check passed!")
            print("Assistant:", check_availability(title, user))

        elif choice == "3":
            print("Assistant:", get_library_timings())

        else:
            print("Assistant: ⚠️ Invalid choice. Please try again.")


# -------------------------
# Run Script
# -------------------------
if __name__ == "__main__":
    run_library_assistant()
