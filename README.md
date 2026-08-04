# Bot Platform project
This file outlines the code structure and formatting; the page will also be updated and expanded as the project progresses.

# 📚 Project Resources
Please submit an access request after opening the Notion links so your account can be authorized to access the workspace.
Once your access has been approved, click the ⭐ **Star** button at the top of each page to add it to your favorites for quick daily access.

---

## 📝 Notion

### 🏠 Home
https://app.notion.com/p/Home-39c0b7b92edb8066b98ad0fbaf04f700?source=copy_link

### 🎯 Goals Tracker
https://app.notion.com/p/39c0b7b92edb80de883adf7e3aa87956?v=39c0b7b92edb80f69cdf000c69fb8141&source=copy_link

### ✅ Task Tracker
https://app.notion.com/p/39c0b7b92edb807ea644e608b29a3ff9?v=39c0b7b92edb80a5a7a8000cd392e071&source=copy_link

---

# Project Development Guidelines

# ⚠️ Project Structure

The project structure **must** follow these rules:

* before start coding please check **auto save** in vscode is acitve
* All directories and folders **must** use **lowercase** names.
* All classes and functions **must** follow the **lowercase** naming convention.
* All classes and functions can use this **_** between words.

--- 

# ⚠️ Git Workflow

Please follow the Git workflow below throughout the development process:

* A **new branch** must be created for every new feature, bug fix, or module.
* All development related to that task **must be completed within its dedicated branch**.
* The primary development branch is **`dev`**. Every feature branch must eventually be merged into **`dev`** through a **Pull Request**.
* The **`main`** branch is reserved **only for production releases and deployments**.
* **No branch should be merged into `main` without prior team approval.**
* The development flow must always follow this order:

```text
feature/*  →  dev  →  main
```

* **All merges must be performed via GitHub Pull Requests.**
* Every Pull Request must be reviewed to ensure the code quality, project structure, and coding standards comply with the project's guidelines before it is merged.

---

# ⚠️ Docker

Please **do not modify** any Docker-related files or configurations.
If you believe a Docker configuration needs to be changed, please leave a comment in the corresponding task assigned to you in **Notion**.
All Docker configuration and maintenance are managed by the project owner. If any changes are required, simply leave a message instead of modifying the files directly.
After pulling the latest changes from the repository, use the following command to build and run the project:

```text
docker compose up -d --build
```

This command will build the project (if necessary) and start all required containers.
after build project you can use this command for start project.

```text
docker compose up -d
```

after give project please switch target branch and migrate database before start project

```text
git switch branchname

python manage.py migrate
```

Thanks to the mounted Docker volumes, any changes you make to the source code will be reflected immediately. **There is no need to rebuild or restart the containers after every code change.** In most cases, simply refresh your browser or restart the client application to see the updates.
Only files that belong to package or tool configurations are allowed to use **PascalCase** or **uppercase** naming conventions. For example:

```text
Dockerfile

README.md
```

All other project files and directories must follow the project's naming conventions described above.

---

# ⚠️ Adapters

Each supported messaging platform is developed as an **independent adapter**. Every adapter is responsible only for communicating with its own platform and should not contain business logic that belongs to the project's core API.
Current adapters:

```text
adapter/
├── bale/
├── rubika/
└── telegram/
```

Each adapter has its own development process and internal structure.

---

## ⚙️ Telegram Adapter

The Telegram adapter is developed using **Webhook mode**.
The Telegram Mother Bot is located in:

```text
adapter/
└── telegram/
    └── mother/
```

---

### Local Development

For local webhook development we use **ngrok**.

#### 1. Authenticate ngrok

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

#### 2. Start ngrok

```bash
ngrok http 8000
```

Copy the generated HTTPS URL and place it inside your `.env` file as:

```text
WEBHOOK_URL=https://xxxxxxxx.ngrok-free.app
```

---

### Run the Telegram Mother Bot

Start the FastAPI application using:

```bash
uvicorn mother.app:app --reload
```

---

### Adapter telegram Folder Structure

adapter telegram must follow the same structure.
Example:

```text
mother/
│
├── app.py
├── bot.py
├── dispatcher.py
├── webhook.py
├── handlers/
├── keyboards/
├── services/
```

---

### handlers/

The **handlers** directory is the most important part of every adapter.
Handlers must be organized by **feature**, **not by update type**.
Correct example:

```text
handlers/
│
├── start/
├── bots/
├── panel/
├── settings/
└── subscription/
```

Every feature directory must contain:

```text
start/
│
├── __init__.py
└── router.py
```

The Router for that feature should be created inside `router.py`.
If the feature becomes larger, it may be divided into additional files, for example:

```text
bots/
│
├── __init__.py
├── create.py
├── delete.py
├── edit.py
└── statistics.py
```

In this case, the Router should be created once and exposed through `__init__.py`, allowing the Dispatcher to include the entire feature with a single import.
The Dispatcher should only include feature routers and should never contain business logic.