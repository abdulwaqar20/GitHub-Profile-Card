from collections import Counter
from datetime import datetime

from github_api import get_user_profile, get_user_repositories

def analyze_languages(repositories):
    """Analyze the primary programming languages used in repositories."""

    languages = Counter()

    for repo in repositories:
        language = repo["language"]

        if language:
            languages[language] += 1

    return languages

def calculate_repository_stats(repositories):
    """Calculate basic repository statistics."""

    total_stars = sum(repo["stargazers_count"] for repo in repositories)
    total_forks = sum(repo["forks_count"] for repo in repositories)

    return total_stars, total_forks

def get_recent_repositories(repositories, limit=5):
    """Return the most recently updated repositories."""

    sorted_repos = sorted(
        repositories,
        key=lambda repo: repo["updated_at"],
        reverse=True
    )

    return sorted_repos[:limit]

def main():

    print("=" * 40)
    print("       GITHUB PROFILE CARD")
    print("=" * 40)

    username = input("Enter GitHub username: ").strip()

    if not username:
        print("Please enter a valid username.")
        return

    profile = get_user_profile(username)

    if profile is None:
        return

    repositories = get_user_repositories(username)

    if repositories is None:
        return

    print("\n" + "=" * 40)
    print("          PROFILE DETAILS")
    print("=" * 40)

    print(f"Username: {profile['login']}")
    print(f"Name: {profile['name']}")
    print(f"Bio: {profile['bio']}")
    print(f"Public Repositories: {profile['public_repos']}")
    print(f"Followers: {profile['followers']}")
    print(f"Following: {profile['following']}")
    print(f"Profile URL: {profile['html_url']}")

    print("\n" + "=" * 40)
    print("       PUBLIC REPOSITORIES")
    print("=" * 40)

    for repo in repositories:
        print(f"- {repo['name']}")

    print("\nTotal repositories fetched:", len(repositories))

    total_stars, total_forks = calculate_repository_stats(repositories)

    print("\n" + "=" * 40)
    print("       REPOSITORY STATISTICS")
    print("=" * 40)
    print(f"Total Stars: {total_stars}")
    print(f"Total Forks: {total_forks}")

    languages = analyze_languages(repositories)

    print("\n" + "=" * 40)
    print("     PROGRAMMING LANGUAGE ANALYSIS")
    print("=" * 40)

    if languages:
        for language, count in languages.most_common():
            print(f"{language}: {count} repositories")
    else:
        print("No programming language information available.")

    recent_repos = get_recent_repositories(repositories)

    print("\n" + "=" * 40)
    print("   RECENTLY UPDATED REPOSITORIES")
    print("=" * 40)

    for repo in recent_repos:
        updated_date = datetime.strptime(
            repo["updated_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        formatted_date = updated_date.strftime("%d %b %Y")

        print(f"- {repo['name']}")
        print(f"  Last updated: {formatted_date}")
        print(f"  URL: {repo['html_url']}")


if __name__ == "__main__":
    main()