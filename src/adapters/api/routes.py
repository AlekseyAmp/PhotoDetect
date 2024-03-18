from fastapi import APIRouter

router = APIRouter()


@router.get(path="/test", response_model=dict[str, str])
async def test() -> dict[str, str]:
    return {"message": "test"}
