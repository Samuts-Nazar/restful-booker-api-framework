from pydantic import BaseModel

class RoomResponse(BaseModel):
    roomid: int
    roomName: str
    type: str
    accessible: bool
    image: str
    description: str
    features: list[str]
    roomPrice: int