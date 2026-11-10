# GitHub Profile Card

A Python-based application that uses the **GitHub REST API** to fetch, display, and analyze public GitHub profile information.

Users can enter any GitHub username and retrieve profile details, public repositories, programming-language statistics, and recently updated repositories.

## Features

- **GitHub Profile Information:** Displays username, name, bio, public repository count, followers, and following.
- **Public Repositories:** Retrieves and lists public repositories.
- **Programming Language Analysis:** Counts repositories by their primary programming language.
- **Recently Updated Repositories:** Displays the five most recently updated repositories with their update dates and links.
- **Repository Statistics:** Displays total stars and forks across the fetched repositories.
- **Error Handling:** Handles invalid usernames, API errors, network failures, and request timeouts.

## Technologies Used

- Python
- Requests library
- GitHub REST API

## Project Structure

```text
github-profile-card/
│
├── main.py
├── github_api.py
├── requirements.txt
├── .gitignore
├── README.md
└── output/
    └── sample_output.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/abdulwaqar20/github-profile-card.git
```

### 2. Navigate to the project directory

```bash
cd github-profile-card
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python main.py
```

Enter a GitHub username when prompted.

Example:

```text
Enter GitHub username: abdulwaqar20
```

The application will fetch and display the requested GitHub profile information.

## GitHub API Endpoints

This project uses the following public GitHub REST API endpoints:

| Endpoint | Purpose |
|---|---|
| `https://api.github.com/users/{username}` | Fetches user profile information |
| `https://api.github.com/users/{username}/repos` | Fetches public repositories |

No API key is required for accessing public profile and repository information. Unauthenticated requests are subject to GitHub's API rate limits.

## Sample Output

The application displays:

- GitHub profile details
- Public repository names
- Programming-language analysis
- Five recently updated repositories
- Repository stars and forks statistics

A sample terminal output is available in `output/sample_output.txt`.

## Error Handling

The application handles:

- Invalid GitHub usernames
- GitHub API rate limits
- Request timeouts
- Network and connection errors
- Other API request errors

## Author

**Abdul Waqar**

- GitHub: [abdulwaqar20](https://github.com/abdulwaqar20)

---

*Developed as a Python API integration project.*