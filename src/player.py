from typing import Optional
from dataclasses import dataclass
from room import Room

@dataclass
class Player:
    name: str
    current_room: Room
