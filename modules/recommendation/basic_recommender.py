from typing import List


class Basic_recommender():
    def __init__(self, news_data:List):
        self.news_data = news_data

    # return recommended post
    def recommend(self, keywords, max_result: int =  5) -> List:
        # returns max_result number of the top post
        if not keywords:
            return self.news_data[:max_result]
        
        # check if keywords match post keywords and return if there is atleast one match
        scored_posts = []
        for post in self.news_data:
            score = sum(1 for kw in keywords if kw.lower() in [k.lower() for k in post['keywords']])
            if score > 0:
                scored_posts.append((score, post))

        # Sort by score (descending) and limit results
        scored_posts.sort(key=lambda x: x[0], reverse=True)
        return [post for _, post in scored_posts][:max_result]