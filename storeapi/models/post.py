from pydantic import BaseModel
from typing import List


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int

class CommentIn(BaseModel):
    body: str
    post_id: int

class Comment(CommentIn):
    id: int

class UserPostWithComments(BaseModel):
    """
    {
    'post': {'body': str, 'id': int},
    'comments': [
                {'body': str, 'post_id': int, 'id':int},
                {'body': str, 'post_id': int, 'id':int}
                ]
    }
    """
    post: UserPost
    comments: List[Comment]

