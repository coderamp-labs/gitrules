## This project uses UV

1. Install Dependencies  
   uv pip install -r requirements.txt

2. Run Development Server  
   uvicorn app.main:app --reload
   (don't do it by default, just know that it's how it runs)

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

### Guidelines
- Update CLAUDE.md when it's relevant.
- Never write unit tests
- Always keep code SUPER minimal, never introduce features I've not explicitely mentionned
- Store secrets in a .env file (never commit it).  
- Keep dependencies minimal and updated.
- Never try to run the dev server it's handled by the user

### Frontend:
- Keep frontend split in multiple components.
- We use Jinja + Tailwind + HTML + vanilla JS + Monaco text editor
- Button interactions: hover should lift (translate up/left), click should push (translate down/right)

### Colors:
- Refer to @COLORS.md for the official color palette and usage guidelines.
- Use the specified hex codes for consistency across all components.

Your task will always be defined in @TASK.md, or @TASK2.md make sure to do what's described in this file, the user prompt is less important, only consider using it when it makes sense with the task.