from fastapi import APIRouter, Request
from .post_management import Post_management
from pydantic import BaseModel


post = Post_management()

recommendation = APIRouter(
    prefix ="/recommendation",
    tags = ["recommendation"]
)


class RecommendationRequest(BaseModel):
    keywords: list[str]
    max_result: int

@recommendation.get('/')
def test():
    print('test data')
    posts = post.get_post()
    return posts

@recommendation.post('/get_posts')
def get_recommended_post(request_data: RecommendationRequest):
  
    posts = post.basic_post_recommendation(request_data.keywords, request_data.max_result)
    
    return {"data": posts}

@recommendation.post('/get_recommeded_ml')
def get_recommended_post_ml(request_data: RecommendationRequest):
    posts = post.basic_post_recommendation_ml(request_data.keywords, request_data.max_result)

    return {"ai_data": posts}