from transformers import pipeline

class EduBERTTutor:
    def __init__(self):
        # Load the pre-trained conversational agent
        self.conversation_pipeline = pipeline("conversational", model="facebook/blenderbot-400M-distill")

    def interact(self, user_query):
        response = self.conversation_pipeline(user_query)
        return response[0]['generated_text']

# Example usage
if __name__ == "__main__":
    tutor = EduBERTTutor()
    user_input = "How does photosynthesis work?"
    print(tutor.interact(user_input))
