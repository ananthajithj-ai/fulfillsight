# Debugging Log

## 2026-06-01

### Issue 1
VS Code showed:

Import "dotenv" could not be resolved

#### Cause
VS Code was using Microsoft Store Python instead of the project's virtual environment.

#### Fix
Selected:

venv\Scripts\python.exe

from VS Code interpreter list.

#### Lesson
Terminal Python and VS Code Python can be different environments.