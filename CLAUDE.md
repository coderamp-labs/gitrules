# Project Setup Instructions

This project uses [uv](https://github.com/astral-sh/uv) as the package manager instead of pip or pip3.

---

## This project uses UV


2. Install Dependencies  
   uv pip install -r requirements.txt

3. Run Development Server  
   uvicorn app.main:app --reload

---

### Project Structure
Recommended layout:

app/  
  main.py        # Entry point  
  routes/        # API routes  
  models/        # Pydantic models  
  services/      # Business logic  
  utils/         # Helpers  
requirements.txt  
CLAUDE.md  

- Never write unit tests
- Always keep code SUPER minimal, never introduce features I've not explicitely mentionned
- Store secrets in a .env file (never commit it).  
- Keep dependencies minimal and updated.


### Frontend:
- Refer to @frontend.md when designing frontend components.
- Keep frontend split in multiple components.