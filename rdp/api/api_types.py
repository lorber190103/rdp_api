from pydantic import BaseModel

class ValueTypeNoID(BaseModel):
    type_name : str
    type_unit : str

class ValueType(ValueTypeNoID):
    id : int

class ValueNoID(BaseModel):
    value_type_id: int
    time: int
    value: float
    value_sensor_id: int

class Value(ValueNoID):
    id: int

class SensorNoID(BaseModel):
    s_name: str
    sensor_location_id: int

class Sensor(SensorNoID):
    id: int

class LocationNoID(BaseModel):
    location_name: str

class Location(LocationNoID):
    id: int

class ApiDescription(BaseModel):
    description : str = "This is the Api"
    value_type_link : str = "/type"
    value_link : str = "/value"