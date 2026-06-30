# Python Functions Demo
# Topics:
# 1. Reducing code duplication
# 2. Splitting complex tasks
# 3. Hiding implementation details
# 4. print vs return
# 5. Improving traceability
# ---------------------------------------


# -----------------------------
# 1. Reducing Code Duplication
# -----------------------------

# Function definition
# name and chai_type are parameters

def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")


# Function calls
# These values are arguments

print_order("Aman", "Masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")

print("-" * 40)


# -----------------------------
# 2. Splitting Complex Tasks
# -----------------------------

# Each function handles one small part of a bigger task

def fetch_sales():
    print("Fetching sales data")


def filter_valid_sales():
    print("Filtering valid sales data")


def summarize_sales():
    print("Summarizing sales data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_sales()
    print("Report is ready")


generate_report()

print("-" * 40)


# -----------------------------
# 3. Hiding Implementation Details
# -----------------------------

# In real projects, these functions may contain complex logic.
# For now, we are only printing messages.

def get_user_input():
    print("Getting user input")


def validate_user_info():
    print("Validating user info")


def save_to_db():
    print("Saving to database")


def register_user():
    get_user_input()
    validate_user_info()
    save_to_db()
    print("User registration complete")


register_user()

print("-" * 40)


# -----------------------------
# 4. Improving Readability
# -----------------------------

# This function calculates the total bill.
# It returns the value instead of printing it directly.

def calculate_bill(cups, price_per_cup):
    total_bill = cups * price_per_cup
    return total_bill


# Store returned value in a variable
my_bill = calculate_bill(3, 15)

print(f"My bill is: {my_bill}")

# Function can also be called directly inside print
print("Order for table 2:", calculate_bill(2, 50))

print("-" * 40)


# -----------------------------
# 5. Improving Traceability
# -----------------------------

# This function adds VAT to the original price.
# Keeping this logic in one place makes it easy to trace and update.

def add_vat(price, vat_rate):
    final_price = price * (100 + vat_rate) / 100
    return final_price


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# def:
# Used to define a function.

# parameter:
# A variable written inside the function definition.

# argument:
# A value passed while calling the function.

# print:
# Displays output on the screen.

# return:
# Sends a value back from the function.

# Good functions should:
# - Have clear names
# - Do one clear task
# - Reduce repeated code
# - Make the program easier to read
