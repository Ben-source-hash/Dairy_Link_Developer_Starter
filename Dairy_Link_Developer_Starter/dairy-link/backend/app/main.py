from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from .database import Base, engine, get_db
from .models import Farmer, Animal, MilkRecord
from .schemas import FarmerCreate, FarmerOut, AnimalCreate, AnimalOut, MilkRecordCreate, MilkRecordOut
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Dairy Link API", version="0.1.0")
@app.get("/health")
def health():
    return {"status": "ok", "service": "dairy-link-api"}
@app.get("/api/farmers", response_model=list[FarmerOut])
def list_farmers(db: Session = Depends(get_db)):
    return db.scalars(select(Farmer).order_by(Farmer.name)).all()
@app.post("/api/farmers", response_model=FarmerOut, status_code=201)
def create_farmer(payload: FarmerCreate, db: Session = Depends(get_db)):
    if db.scalar(select(Farmer).where(Farmer.farmer_id == payload.farmer_id)):
        raise HTTPException(409, "Farmer ID already exists")
    farmer = Farmer(**payload.model_dump())
    db.add(farmer); db.commit(); db.refresh(farmer)
    return farmer
@app.get("/api/farmers/{farmer_id}", response_model=FarmerOut)
def get_farmer(farmer_id: int, db: Session = Depends(get_db)):
    farmer = db.get(Farmer, farmer_id)
    if not farmer: raise HTTPException(404, "Farmer not found")
    return farmer
@app.get("/api/animals", response_model=list[AnimalOut])
def list_animals(db: Session = Depends(get_db)):
    return db.scalars(select(Animal).order_by(Animal.animal_id)).all()
@app.post("/api/animals", response_model=AnimalOut, status_code=201)
def create_animal(payload: AnimalCreate, db: Session = Depends(get_db)):
    if not db.get(Farmer, payload.farmer_id): raise HTTPException(404, "Farmer not found")
    animal = Animal(**payload.model_dump())
    db.add(animal); db.commit(); db.refresh(animal)
    return animal
@app.get("/api/milk-records", response_model=list[MilkRecordOut])
def list_milk_records(db: Session = Depends(get_db)):
    return db.scalars(select(MilkRecord).order_by(MilkRecord.record_date.desc())).all()
@app.post("/api/milk-records", response_model=MilkRecordOut, status_code=201)
def create_milk_record(payload: MilkRecordCreate, db: Session = Depends(get_db)):
    if not db.get(Farmer, payload.farmer_id): raise HTTPException(404, "Farmer not found")
    record = MilkRecord(**payload.model_dump())
    db.add(record); db.commit(); db.refresh(record)
    return record
