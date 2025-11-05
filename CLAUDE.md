# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Actions demonstration repository that showcases automated scheduled tasks and code commits. The repository contains two main workflows that run on schedule and can be manually triggered.

## Key Components

### Python Scripts

1. **script.py** - Basic scheduled task script
   - Simple demonstration of a scheduled job
   - Displays execution time and timezone information
   - Template for adding custom task logic

2. **auto-commit.py** - Automated commit generator
   - Generates random code snippets in various languages (Python, JavaScript, Java, C++, Go, Rust)
   - Creates files in `auto_commits/` directory
   - Handles git configuration, commit, and push operations
   - Uses randomized commit messages with emojis

### GitHub Actions Workflows

Located in `.github/workflows/`:

1. **scheduled-task.yml** - Basic scheduled task workflow
   - Triggers: Push to master/main, daily at 00:00 UTC, manual dispatch
   - Runs `script.py` on Python 3.x

2. **auto-commit.yml** - Automated commit workflow
   - Triggers: Daily at 01:00 UTC, manual dispatch
   - Requires `contents: write` permission
   - Runs `auto-commit.py` with GitHub Actions Bot credentials

## Common Commands

### Manual Testing Workflows

Test the scheduled task workflow:
```bash
# Trigger via GitHub CLI
gh workflow run "定时任务"

# Or manually via GitHub UI:
# Actions tab → "定时任务" → Run workflow
```

Test the auto-commit workflow:
```bash
# Trigger via GitHub CLI
gh workflow run "自动提交代码"
```

### Running Scripts Locally

Run the basic scheduled task:
```bash
python script.py
```

Run the auto-commit script (creates commits):
```bash
python auto-commit.py
```

### Viewing Workflow Results

```bash
# List recent workflow runs
gh run list

# View specific workflow runs
gh run list --workflow="scheduled-task.yml"
gh run list --workflow="auto-commit.yml"

# View logs for latest run
gh run view --log
```

## Architecture Notes

### Workflow Configuration

- **Timezone**: All cron schedules use UTC time (UTC+0). Beijing time is UTC+8.
- **Permissions**: The auto-commit workflow requires `contents: write` permission to push changes. This must be enabled in repository settings under Settings → Actions → General → Workflow permissions.
- **Token Usage**: Uses `${{ secrets.GITHUB_TOKEN }}` for authentication, which is automatically provided by GitHub Actions.

### Auto-Commit Process Flow

1. Workflow triggers (scheduled or manual)
2. Checkout repository with full history (`fetch-depth: 0`)
3. Python script generates random code snippet
4. Creates timestamped file in `auto_commits/` directory
5. Configures git with Actions Bot credentials
6. Stages, commits, and pushes changes to current branch
7. Uses error handling for git operations

### Cron Expression Format

Format: `minute hour day month weekday`
- All times in UTC
- Examples in README.md:62-85 document common patterns

## Repository Requirements

- **Public repository** or GitHub Pro/Team/Enterprise account (for private repo scheduled workflows)
- **Workflow permissions** set to "Read and write permissions" in repository settings
- **Python 3.x** runtime (provided by GitHub Actions)
- **No external dependencies** - uses only Python standard library

## Modifying Behavior

### Changing Schedule Times

Edit the `cron` expression in the respective workflow YAML file:
- `scheduled-task.yml:9` for basic task
- `auto-commit.yml:7` for auto-commit

### Customizing Task Logic

- Modify `script.py` main() function for custom scheduled tasks
- Modify `auto-commit.py` generate_random_code() to change code generation
- Modify `auto-commit.py` generate_commit_message() to customize commit messages

### Adding Code Languages

Edit `auto-commit.py:14-21` (languages list) and `auto-commit.py:23-60` (code_snippets list) to add new programming languages.
