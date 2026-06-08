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

## 2026-0604

### Issue 1: Logging File Not Found Inside Container
#### Error

FileNotFoundError: /app/logs/app.log

#### Root Cause

The application assumed the logs directory already existed.
Docker containers start with a fresh filesystem and the logs directory was missing.

#### Fix

#### Added:

os.makedirs("logs", exist_ok=True)

before configuring logging.

Lesson Learned

Docker often exposes hidden filesystem assumptions that exist on the local machine.

## Issue 2: Invalid Python Import Syntax
### Error

SyntaxError in src/db.py

### Root Cause

#### Used:

from src.config import{

instead of a valid Python import statement.

#### Fix

Replaced with:

from src.config import (...)

Lesson Learned

Always read the stack trace before assuming Docker or networking is the problem.

## Issue 3: PostgreSQL Connectivity
### Problem

Needed Python container to communicate with PostgreSQL container.

#### Root Cause

Understanding Docker networking and service discovery.

#### Fix

#### Used:

DB_HOST=postgres

where postgres is the Docker Compose service name.

Lesson Learned

Inside Docker Compose, localhost refers to the current container.
Services communicate using service names.

## Issue 4: Missing Return Statement
### Error

Potential NoneType errors from database connection code.

#### Root Cause

get_connection() created a connection but did not return it.

#### Fix

#### Added:

return conn

Lesson Learned

A function that creates a resource must explicitly return it if callers need access to it.

## 08-06-2026
# Debugging Notes

This document records issues encountered during development and how they were resolved.

---

## Issue 1: Docker Could Not Find src.main

### Error

```text
ModuleNotFoundError: No module named 'src'
```

### Cause

The repository was refactored:

```text
src/main.py
```

became:

```text
event_generator/main.py
```

but the Dockerfile still contained:

```dockerfile
CMD ["python", "-m", "src.main"]
```

### Fix

Updated Dockerfile:

```dockerfile
CMD ["python", "-m", "event_generator.main"]
```

---

## Issue 2: Broken Imports After Refactor

### Error

```text
ModuleNotFoundError: No module named 'src.db'
```

### Cause

Several files still referenced the old module structure:

```python
from src.db import ...
from src.config import ...
```

### Fix

Updated imports:

```python
from db.db import ...
from shared.config import ...
```

---

## Issue 3: PostgreSQL Tables Not Being Created

### Symptom

Database started successfully but schema was not initialized.

### Cause

PostgreSQL was not executing:

```text
db/init.sql
```

during startup.

### Fix

Mounted initialization script:

```yaml
volumes:
  - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
```

---

## Issue 4: PostgreSQL Initialization Only Runs Once

### Symptom

Changes to init.sql did not appear after restarting containers.

### Cause

PostgreSQL executes initialization scripts only when the database is created for the first time.

### Fix

Remove existing volumes:

```bash
docker compose down -v
```

Then recreate:

```bash
docker compose up --build
```

---

## Issue 5: YAML Indentation Errors

### Symptom

Docker Compose failed to parse configuration.

### Cause

Incorrect indentation inside:

```yaml
postgres:
```

section.

### Fix

Ensure all PostgreSQL configuration remains nested beneath:

```yaml
postgres:
```

using consistent indentation.

---

## Lessons Learned

* Docker images may still contain old code after refactoring.
* PostgreSQL initialization scripts only run during first-time database creation.
* Small import path changes can break entire applications.
* YAML indentation matters.
* Refactoring requires updating imports, Docker commands, and project structure together.
