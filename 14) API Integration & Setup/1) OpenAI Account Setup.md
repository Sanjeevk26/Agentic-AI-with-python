# Setting Up an OpenAI Account for API Usage

## Overview

In this lesson, we set up an OpenAI account so that we can use OpenAI APIs from Python projects.

The goal is to prepare the account for upcoming AI API calls.

This file will cover:

* Opening the OpenAI Platform
* Signing in or signing up
* Exploring the dashboard
* Understanding the playground
* Checking API usage
* Adding billing credits
* Creating an API key
* Copying and using the API key safely
* Revoking API keys when needed

---

# 1. Open the OpenAI Platform

Visit the OpenAI Platform:

```text id="91p4fy"
https://platform.openai.com
```

This is where developers can manage their OpenAI API setup.

From here, you can:

* Sign up
* Log in
* Access the dashboard
* Create API keys
* Check usage
* Manage billing

---

# 2. Sign Up or Log In

You can sign up or log in using your account.

A common option is:

```text id="s76ke5"
Login with Google
```

Once logged in, you will be able to access the platform dashboard.

---

# 3. Open the Dashboard

After logging in, click the button or option that says:

```text id="33lq5v"
Dashboard
```

The dashboard is the main area where you manage your OpenAI developer account.

---

# 4. What You Can See in the Dashboard

Inside the dashboard, you may see sections such as:

* Chat prompts
* Playground
* Usage
* API keys
* Settings
* Billing

The exact layout may change over time, but these are the common areas used by developers.

---

# 5. Playground

The Playground is useful for testing prompts before writing code.

For example, you can type:

```text id="me9zrv"
Hey
```

The model can respond directly inside the Playground.

This helps you test model behavior quickly without writing a Python script.

---

# 6. Usage Section

The usage section helps you track your API usage.

You can check details such as:

* How much you are spending
* How many tokens you are using
* Input token usage
* Output token usage
* Usage over time

Official OpenAI documentation explains that the usage dashboard displays API usage and token-related information.

---

# 7. Billing and Credits

OpenAI API usage is paid.

Before making API calls, you usually need to add credits or set up billing.

Go to:

```text id="5672sw"
Settings → Billing
```

From there, you can add credits to your account.

OpenAI’s prepaid billing documentation states that API users can pre-purchase usage credits, and the minimum purchase is currently $5.

---

# 8. Add Credits

To add credits:

```text id="wkteoi"
Settings
    ↓
Billing
    ↓
Add credits
```

You will need to add a payment method.

The transcript mentions that adding around $5 is usually enough for the course examples because simple API experiments may only use a small amount of credits.

However, actual cost depends on:

* Model used
* Number of requests
* Input tokens
* Output tokens
* Project size
* Whether the API calls are repeated many times

---

# 9. API Keys

API keys are required when using OpenAI APIs from Python, Node.js, or any backend application.

An API key is like a secret password that lets your code call OpenAI services.

OpenAI’s help documentation says API keys can be created and managed from the API key page, and the full secret key is only shown when it is created.

---

# 10. Create an API Key

To create an API key:

```text id="9gm96m"
Dashboard
    ↓
API keys
    ↓
Create new secret key
```

You can give the key a name, for example:

```text id="m3dtt5"
Test API Key
```

Then click:

```text id="rt4z1g"
Create secret key
```

After the key is created, copy it immediately.

---

# 11. Important API Key Safety Rule

The API key is secret.

Do not share it publicly.

Do not paste it into:

* GitHub public repositories
* Screenshots
* Public videos
* Frontend JavaScript code
* Shared documents
* Chat messages with other people

OpenAI documentation reminds users not to share their API key with anyone.

---

# 12. Copy the API Key

Once the key is created, copy it.

You will use this key in upcoming projects.

Example use cases:

* Python project
* Node.js project
* Backend API
* AI agent
* RAG application
* Chatbot application

A common practice is to store the API key in an environment variable instead of writing it directly inside the code.

Example:

```text id="r30j8v"
OPENAI_API_KEY=your_api_key_here
```

---

# 13. Revoke an API Key

If an API key is exposed, leaked, or no longer needed, revoke it.

Revoking a key prevents anyone from using that key further.

Good practice:

```text id="qzr8ty"
Create key → Use safely → Revoke if exposed or not needed
```

---

# 14. Why API Keys Are Needed

When your Python code calls OpenAI, OpenAI needs to know:

* Which account is making the request
* Whether the account has billing enabled
* Whether the key is valid
* How much usage should be recorded
* Which project or organization the usage belongs to

The API key helps authenticate your request.

---

# 15. High-Level Setup Flow

```text id="g88cmh"
Open OpenAI Platform
    ↓
Sign up or log in
    ↓
Go to Dashboard
    ↓
Set up billing / add credits
    ↓
Go to API keys
    ↓
Create new secret key
    ↓
Copy the key safely
    ↓
Use the key in Python projects
```

---

# 16. What We Will Use This For

After setup, we can use the API key to build AI-powered applications.

Examples:

* Chat completion apps
* AI assistants
* Prompt engineering examples
* RAG systems
* Agents
* LangChain applications
* LangGraph applications
* FastAPI AI endpoints

---

# 17. Practical Developer Notes

Keep these points in mind:

* The OpenAI API is not the same as just using ChatGPT in the browser.
* API usage is billed separately.
* API calls consume tokens.
* Both input and output tokens may affect cost.
* Keep track of usage from the dashboard.
* Store API keys securely.
* Revoke unused or exposed keys.
* Do not hardcode secrets in production code.

---

# 18. Simple Example of Environment Variable Usage

Instead of writing the key directly in code:

```python id="m4jqqa"
api_key = "sk-..."
```

Use an environment variable:

```python id="55kluv"
import os

api_key = os.getenv("OPENAI_API_KEY")
```

This is safer and cleaner.

---

# 19. Beginner-Friendly Summary

To use OpenAI APIs from Python, you need:

```text id="pwr8bd"
OpenAI account
Billing credits
API key
Python project
OpenAI SDK or HTTP client
```

Once these are ready, your Python application can send requests to OpenAI models and receive AI-generated responses.

---

# Key Takeaways

* OpenAI API setup starts from the OpenAI Platform.
* You need to log in and access the dashboard.
* The Playground can be used for quick prompt testing.
* The Usage section helps track token usage and spending.
* API usage requires billing or prepaid credits.
* API keys are created from the API keys section.
* A full secret key is shown only when it is created.
* API keys must be kept private.
* Revoke API keys if they are exposed or no longer needed.
* The API key will be used in upcoming Python projects.
