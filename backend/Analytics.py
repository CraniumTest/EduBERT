import pandas as pd

class Analytics:
    def __init__(self):
        self.data_log = pd.DataFrame(columns=["timestamp", "query", "response", "language"])

    def log_interaction(self, query, response, language):
        self.data_log = self.data_log.append({
            "timestamp": pd.Timestamp.now(),
            "query": query,
            "response": response,
            "language": language
        }, ignore_index=True)

    def report(self):
        return self.data_log

# Example usage
analytics = Analytics()
analytics.log_interaction("What is photosynthesis?", "Photosynthesis is the process by which...", "en")
print(analytics.report())
