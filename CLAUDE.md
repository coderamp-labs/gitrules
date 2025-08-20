# Project Setup Instructions

This project uses [uv](https://github.com/astral-sh/uv) as the package manager instead of pip or pip3.

---

## This project uses UV


2. Install Dependencies  
   uv pip install -r requirements.txt

3. Run Development Server  
   uvicorn app.main:app --reload

---

## Python Good Practices

### Code Style
- Follow PEP 8 for formatting.  
- Use black for auto-formatting: black .

### Type Hints
- Always use type hints for clarity.  

### Project Structure
Recommended layout:

app/  
  main.py        # Entry point  
  routes/        # API routes  
  models/        # Pydantic models  
  services/      # Business logic  
  utils/         # Helpers  
tests/  
  test_*.py      # Unit tests  
requirements.txt  
CLAUDE.md  

### Environment Variables
- Store secrets in a .env file (never commit it).  
- Load them with python-dotenv or FastAPI settings.

### Testing
- Use pytest for unit tests: pytest

---

- Keep dependencies minimal and updated.
