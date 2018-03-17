import uuid

class SensorData:
    time_ = None
    dimension_ = None
    value_ = None
    sensor_id_ = None
    
    def __init__(self, sensor_id = None):
        if sensor_id == None:
            sensor_id = uuid.uuid4()
        self.sensor_id_ = sensor_id