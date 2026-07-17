# Bot Platform project
This file outlines the code structure and formatting; the page will also be updated and expanded as the project progresses.

# Project Development Guidelines

## ⚠️ Project Structure

The project structure **must** follow these rules:

* All directories and folders **must** use **lowercase** names.
* All classes and functions **must** follow the **PascalCase** naming convention.

---

## ⚠️ Git Workflow

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

## ⚠️ Docker

Please **do not modify** any Docker-related files or configurations.
If you believe a Docker configuration needs to be changed, please leave a comment in the corresponding task assigned to you in **Notion**.
All Docker configuration and maintenance are managed by the project owner. If any changes are required, simply leave a message instead of modifying the files directly.
After pulling the latest changes from the repository, use the following command to build and run the project:

```text
docker compose up -d --build
```

This command will build the project (if necessary) and start all required containers.
Thanks to the mounted Docker volumes, any changes you make to the source code will be reflected immediately. **There is no need to rebuild or restart the containers after every code change.** In most cases, simply refresh your browser or restart the client application to see the updates.
Only files that belong to package or tool configurations are allowed to use **PascalCase** or **uppercase** naming conventions. For example:

```text
Dockerfile
```

All other project files and directories must follow the project's naming conventions described above.