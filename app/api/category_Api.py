from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.category_service import CategoryService
from app.schema.category_schema import CategorySchema, CategoryUpdate, CategoryResponse
from app.auth.auth_dependency import get_admin_user


category_router = APIRouter(prefix="/categories",tags=["Category"])

@category_router.post("/", response_model=CategoryResponse)
def create_category(category_data: CategorySchema,db: Session = Depends(get_db),current_user=Depends(get_admin_user)):
    service = CategoryService(db)
    return service.create_category(category_data)

@category_router.get("/{category_id}", response_model=CategoryResponse)
def get_category_by_id(category_id: int,db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_category_by_id(category_id)

@category_router.get("/name/{name}", response_model=CategoryResponse)
def get_category_by_name(name: str,db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_category_by_name(name)

@category_router.get("/", response_model=list[CategoryResponse])
def get_all_category(db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all_category()

@category_router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int,category_data: CategoryUpdate,db: Session = Depends(get_db),current_user=Depends(get_admin_user)):
    service = CategoryService(db)
    return service.update_category(category_id, category_data)

@category_router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db),current_user=Depends(get_admin_user)):
    service = CategoryService(db)
    service.delete_category(category_id)
    return {"message": "Category deleted successfully"}