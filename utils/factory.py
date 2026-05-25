import uuid

class NoteFactory:
    @staticmethod
    def create_valid_payload():
        unique_id = uuid.uuid4().hex[:6]
        return {
            "title": f"Note Title {unique_id}",
            "content": f"Automated test content {unique_id}."
        }

    @staticmethod
    def create_invalid_payload():
        return {
            "content": "Payload without a required title field"
        }
