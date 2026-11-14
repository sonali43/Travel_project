from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.category_repo import CategoryRepo
from app.schema.category_schema import CategorySchema, CategoryUpdate

class CategoryService:
    def __init__(self, db:Session):
        self.repo=CategoryRepo(db)
        
    def create_category(self,category_data:CategorySchema):
        existing=self.repo.get_category_by_name(category_data.name)
        if existing:
            raise HTTPException(
                status_code=400,
                detail="Category already exists"
            )
        return self.repo.create_category(category_data)
    
    def get_category_by_id(self, category_id:int):
        category = self.repo.get_category_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )
        return category
    
    def get_category_by_name(self,name:str):
        category= self.repo.get_category_by_name(name)
        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )
        return category
    
    def get_all_category(self):
        return self.repo.get_all_category()
    
    def update_category(self, category_id: int, category_data: CategoryUpdate):
        category = self.repo.get_category_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        if category_data.name:
            existing = self.repo.get_category_by_name(category_data.name)

            if existing and existing.id != category_id:
                raise HTTPException(
                    status_code=400,
                    detail="Category name already exists"
                )

        return self.repo.update_category(category_id, category_data)
    
    def delete_category(self,category_id: int):
        category = self.repo.get_category_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )
        return self.repo.delete_category(category_id)