# main.py
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Note MVP Service")

# Временная база данных в оперативной памяти
db: Dict[str, dict] = {}
id_counter = 1

class NoteInput(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: str
    content: str

@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteInput):
    global id_counter
    # Простая валидация: заголовок не должен быть пустым
    if not note.title or note.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    
    note_id = str(id_counter)
    id_counter += 1
    
    new_note = {
        "id": note_id,
        "title": note.title,
        "content": note.content
    }
    db[note_id] = new_note
    return new_note

@app.get("/notes", response_model=List[dict])
def get_all_notes():
    return list(db.values())

@app.get("/notes/{note_id}")
def get_note(note_id: str):
    if note_id not in db:
        raise HTTPException(status_code=404, detail="Note not found")
    return db[note_id]

@app.put("/notes/{note_id}")
def update_note(note_id: str, note: NoteUpdate):
    if note_id not in db:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db[note_id]["title"] = note.title
    db[note_id]["content"] = note.content
    return db[note_id]

@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    if note_id not in db:
        raise HTTPException(status_code=404, detail="Note not found")
    del db[note_id]
    return {"detail": "Successfully deleted"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
