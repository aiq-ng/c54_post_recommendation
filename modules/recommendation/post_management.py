from ..shared.connect_db import Db_connection
from .basic_recommender import Basic_recommender
from .ai_recommender import MLRecommender

db_conn = Db_connection()


class Post_management():

    def __init__(self):
        pass

    def get_post(self):
        try:
            conn = db_conn.get_db_connection()
        except Exception as e:
            return {"error": f"Database connection failed: {str(e)}"}

        cursor = None  # Initialize cursor to None

        try:
            cursor = conn.cursor()

            query = """
            SELECT p.id, p.title, p.content, p.slug, p.thumbnail, p.summary, jsonb_agg(t.name) AS keywords
            FROM posts p
            JOIN post_tags pt ON p.id = pt.post_id
            JOIN tags t ON t.id = pt.tag_id
            GROUP BY p.id
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            posts = [dict(row) for row in rows]

            return posts

        except Exception as e:
            return {"error": f"Query failed: {str(e)}"}

        finally:
            if cursor is not None:  # Check if cursor exists
                cursor.close()
            if conn is not None:
                conn.close()

    def basic_post_recommendation(self, keywords, max_result):
        posts = self.get_post()
        print(posts)
        recommender = Basic_recommender(posts)

        recommended_post = recommender.recommend(keywords, max_result)

        return recommended_post
    
    def basic_post_recommendation_ml(self, keywords, max_result):
        posts = self.get_post()
        ml_recommender = MLRecommender(posts)

        recommended_post = ml_recommender.recommend(keywords, max_result)

        return recommended_post