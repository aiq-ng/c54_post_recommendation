from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class MLRecommender:
    def __init__(self, news_data: List):
        self.news_data = news_data
        # Combine title and content for better text representation
        self.documents = [f"{post['title']} {post['content']}" for post in news_data]
        # Initialize and fit TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def recommend(self, keywords: List[str] = None, max_results: int = 5) -> List:
        if not keywords:
            # Fallback: return top N posts if no keywords provided
            return self.news_data[:max_results]

        # Convert user keywords into a single query string
        query = " ".join(keywords)
        # Transform query into TF-IDF vector
        query_vector = self.vectorizer.transform([query])

        # Compute cosine similarity between query and all news posts
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()

        # Get indices of top similar posts
        top_indices = np.argsort(similarities)[::-1][:max_results]

        # Return corresponding news posts
        return [self.news_data[idx] for idx in top_indices if similarities[idx] > 0]