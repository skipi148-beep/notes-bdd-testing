import requests

class NoteApiPage:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = f"{base_url}/notes"

    def create_note(self, payload):
        return requests.post(self.base_url, json=payload)

    def get_all_notes(self):
        return requests.get(self.base_url)

    def get_note_by_id(self, note_id):
        return requests.get(f"{self.base_url}/{note_id}")

    def update_note(self, note_id, payload):
        return requests.put(f"{self.base_url}/{note_id}", json=payload)

    def delete_note(self, note_id):
        return requests.delete(f"{self.base_url}/{note_id}")
