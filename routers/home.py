from fastapi import APIRouter

router = APIRouter(
  tags=['health-check']
)

@router.get('/')
async def get_root():
  return {
    'name': 'Kunst und Technik',
    'version': '0.1.0'
  }