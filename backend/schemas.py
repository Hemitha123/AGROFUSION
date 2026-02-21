from pydantic import BaseModel

class FarmInput(BaseModel):
    location: str
    land_size: float   # ✅ MUST BE HERE
    soil_type: str
    previous_crop: str | None = None
    water_availability: str
    budget: str | None = None
    sowing_month: str | None = None
    temperature: float
    rainfall: float
    humidity: float
