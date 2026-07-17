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
