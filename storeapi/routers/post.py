from typing import List

from fastapi import APIRouter

from storeapi.models import UserPost, UserPostIn

router = APIRouter()


post_table = {}


@router.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):

    data = post.model_dump()

    last_id = len(post_table)

    new_post = {**data, "id": last_id}

    post_table[last_id] = new_post

    return new_post


@router.get("/post", response_model=List[UserPost])
async def get_all_post():

    return list(post_table.values())


@router.get("/")
async def root():
    return {"message": "Hello, world!"}
