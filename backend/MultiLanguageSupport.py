class MultiLanguageSupport:
    def __init__(self):
        self.languages = ['en', 'es', 'fr']
        self.active_language = 'en'

    def switch_language(self, language):
        if language in self.languages:
            self.active_language = language
        else:
            raise ValueError("Language not supported")

    def get_tutoring_response(self, query):
        # Assuming EduBERTTutor class adapts accordingly
        tutor = EduBERTTutor()  # A real implementation would require more tuning
        return tutor.interact(query)

# Example usage
ml_support = MultiLanguageSupport()
ml_support.switch_language('es')
response = ml_support.get_tutoring_response("¿Qué es la fotosíntesis?")
print(response)
