# Flask Portfolio & Dual CI/CD Pipeline Lab

![Flask CI](https://github.com/USERNAME/REPOSITORY/actions/workflows/ci.yml/badge.svg)

A modern, responsive Flask portfolio web application showcasing automated multi-cloud synchronization, containerized deployments, and dual CI/CD pipelines using GitHub Actions and Azure DevOps targeting Azure Kubernetes Service (AKS).

---

## 🏗️ Architecture & Deployment Flow

```
                     +---------------------------------------+
                     |         Local Developer Machine       |
                     +---------------------------------------+
                                         |
                                         |  git pushall
                                         v
               +---------------------------------------------------+
               |                                                   |
               v                                                   v
    +--------------------+                              +--------------------+
    |   GitHub Remote    |                              | Azure DevOps Remote|
    |   (`origin`)       |                              |     (`azure`)      |
    +--------------------+                              +--------------------+
               |                                                   |
               | (PR Validation / Quality Gate)                    | (Deployment Trigger)
               v                                                   v
    +--------------------+                              +--------------------+
    |   GitHub Actions   |                              | Azure Pipelines    |
    |  (Lint, Test, PR)  |                              |  (Build ACR & AKS) |
    +--------------------+                              +--------------------+
                                                                   |
                                                                   | Builds & Deploys
                                                                   v
                                                        +--------------------+
                                                        |  Azure Kubernetes  |
                                                        |   Service (AKS)    |
                                                        +--------------------+
```

---

## ✨ Features

* **Flask Backend**: Lightweight Python web application serving portfolio project cards, dynamic content routes, and static assets.
* **Dual-Remote Git Synchronization**: Configured to push simultaneously to GitHub and Azure DevOps using a custom local Git alias over SSH.
* **Dual CI/CD Architecture**:
  * **GitHub Actions**: Automated PR checks, code linting (`flake8`), and test execution (`pytest`).
  * **Azure Pipelines**: Containerization, image registry publishing (ACR), and Kubernetes manifest deployments (AKS).
* **Responsive Frontend**: Clean HTML/CSS design rendering structured project cards and interactive elements.

---

## 🛠️ Tech Stack & Prerequisites

* **Language/Framework**: Python 3.11+, Flask
* **CI/CD Platforms**: GitHub Actions, Azure DevOps Pipelines
* **Containerization**: Docker, Azure Container Registry (ACR)
* **Orchestration**: Azure Kubernetes Service (AKS), `kubectl`, Kubernetes Manifests
* **Source Control**: Git CLI (SSH public keys configured for both endpoints)

---

## ⚡ Dual CI/CD Pipeline Responsibilities

| Platform | Trigger | Primary Responsibilities |
| :--- | :--- | :--- |
| **GitHub Actions** (`.github/workflows/ci.yml`) | Pull Requests & Pushes to `main` | Code quality validation, linting, Python unit tests (`pytest`). |
| **Azure Pipelines** (`azure-pipelines.yml`) | Pushes to Azure DevOps `main` | Docker build, ACR push, AKS cluster deployment and rollout. |

---

## 🚀 Quick Start (Local Development)

### 1. Clone the Repository

```bash
git clone git@github.com:USERNAME/REPOSITORY.git
cd REPOSITORY
```

### 2. Set Up Virtual Environment & Dependencies

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Application Locally

```bash
# Set Flask entrypoint environment variable
export FLASK_APP=app.py
export FLASK_ENV=development

# Run the local development server
flask run --port=5000
```

Navigate to `http://127.0.0.1:5000` in your web browser to view the application.

---

## ⚙️ Multi-Remote Synchronization Setup

This project uses a dual-remote Git setup to keep open-source code visibility on GitHub and enterprise deployments on Azure DevOps in sync.

### Remote Configuration

Verify your remotes in terminal:

```bash
git remote -v
```

Output:
```text
azure   git@ssh.dev.azure.com:v3/ORGANIZATION/PROJECT/REPOSITORY (fetch)
azure   git@ssh.dev.azure.com:v3/ORGANIZATION/PROJECT/REPOSITORY (push)
origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
origin  git@github.com:USERNAME/REPOSITORY.git (push)
```

### Dual-Push Alias

To push updates to both platforms in a single command, configure the global Git alias:

```bash
git config --global alias.pushall '!git push origin main && git push azure main'
```

Now, deploy code changes across both environments by running:

```bash
git pushall
```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
