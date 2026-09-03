from fastapi import APIRouter
from services.data_service import (
    get_all_data, 
    create_data, 
    update_data, 
    delete_data, 
    get_data_summary
)
from schemas.data import DataCreate, DataResponse

router = APIRouter(
    prefix="/api/data",
    tags=["Data"],
)

@router.get("/summary")
def read_data_summary():
    return get_data_summary()

@router.get("")
def read_data():
    return get_all_data()

@router.post("", response_model=DataResponse)
def add_data(data: DataCreate):
    return create_data(data.model_dump())

@router.put("/{id}", response_model=DataResponse)
def edit_data(id: str, data: DataCreate):
    return update_data(id, data.model_dump())

@router.delete("/{id}")
def remove_data(id: str):
    return delete_data(id)

