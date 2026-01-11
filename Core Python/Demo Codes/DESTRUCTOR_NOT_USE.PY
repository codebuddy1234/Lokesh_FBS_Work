# ❌ What destructor is NOT for (important)

# ❌ Printing messages
# ❌ Business logic
# ❌ Database updates
# ❌ Counting objects reliably
# ❌ Important program flow

# Why?
# 👉 Because Python does NOT guarantee when __del__ will run

# ✅ Where destructor is used in REAL WORLD
# 1️⃣ Closing files
# class FileHandler:
#     def __init__(self, filename):
#         self.file = open(filename, "r")

#     def __del__(self):
#         self.file.close()


# ✔ Ensures file is closed if object is deleted

# 2️⃣ Releasing network connections
# class Network:
#     def __init__(self):
#         print("Connection opened")

#     def __del__(self):
#         print("Connection closed")

# 3️⃣ Releasing memory / resources (low-level systems)

# Game engines

# OS tools

# Embedded systems

# Python bindings to C/C++

# ⚠️ Why destructor is risky in Python
# Python uses Garbage Collection

# Object is destroyed when no reference exists

# OR when program exits

# OR sometimes never immediately

# obj = Book()
# obj = None   # destructor MAY run


# 👉 MAY, not must

# 🔴 Interview Golden Line (MEMORIZE)

# In Python, destructors are not reliable for critical cleanup due to garbage collection.

# ✅ Best Practice (VERY IMPORTANT)
# ❌ Avoid destructor
# ✅ Use context managers (with)
# ⭐ Real-World Best Solution
# with open("data.txt", "r") as f:
#     data = f.read()


# ✔ File auto-closes
# ✔ Safe
# ✔ Professional
# ✔ Industry standard

# 🔥 When should YOU mention destructor in interview?

# ✔ To show concept knowledge
# ✔ For resource cleanup
# ✔ When asked about OOPS
# ✔ Not for logic control

# 📌 One-Line Summary

# Destructors exist in Python, but they are rarely used in real-world code because their execution timing is unpredictable.

# 🎯 Interview Q&A

# Q: Do you use destructor in production?
# 👉 Rarely. We prefer context managers.

# Q: Why Python keeps destructor then?
# 👉 For backward compatibility and low-level resource cleanup.

# 🧠 Simple Analogy

# Destructor is like:

# Leaving your house and hoping someone switches off lights for you.

# Context manager is:

# You switch off lights yourself before leaving.  