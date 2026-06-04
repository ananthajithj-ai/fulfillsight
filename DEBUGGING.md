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