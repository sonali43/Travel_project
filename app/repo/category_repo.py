from sqlalchemy.orm import Session
from app.model.category_model import Category
from app.schema.category_schema import CategorySchema,CategoryUpdate

class CategoryRepo:
    
    def __init__(self,db=Session):
        self.db=db
        
    def create_category(self,category_data:CategorySchema):
        new_category=Category(
            name=category_data.name,
            description=category_data.description
        )
        
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        
        return new_category
    
    def get_category_by_id(self,category_id:int):
        return self.db.query(Category).filter(Category.id==category_id).first()
    
    def get_category_by_name(self,name:str):
        return self.db.query(Category).filter(Category.name == name).first()
    
    def get_all_category(self):
        return self.db.query(Category).all()
    
    def update_category(self,category_id:int,category_data:CategoryUpdate):
        category=self.get_category_by_id(category_id)
        if category:
            update_data=category_data.model_dump(exclude_unset=True)
            
            for key, value in update_data.items():
                setattr(category,key,value)
                
            self.db.commit()
            self.db.refresh(category)
            
    def delete_category(self,category_id:int):
        delete=self.get_category_by_id(category_id)
        
        if delete:
            self.db.delete(delete)
            self.db.commit()
        
        return delete