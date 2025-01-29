from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"], 
                   responses={404:{"message": "No encontrado"}})

product_list = ["Procuto 1", "Procuto 2", "Procuto 3", "Procuto 4", "Procuto 5"]
@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id: int):
    return product_list[id]