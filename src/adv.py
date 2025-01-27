from room import Room
from player import Player
import sys
from typing import Tuple, Optional, List, Dict


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

def change_rooms(player: Player, direction: str):
    """  """
    dirs: Tuple[str, str, str, str] = ('n', 's', 'e', 'w')

    dir_to_attr: Dict[str, str] = {dir: dir + '_to' for dir in dirs}

    try:
        assert direction in dirs
    except AssertionError:
        print("please enter a valid cardinal direction")
    else:

        next_room: Optional[Room] = player.current_room.__dict__[dir_to_attr[direction]]

        if next_room:
            player.current_room = next_room
        else:
            print("The way is blocked! ")

    finally:
        pass

def message(player: Player) -> str:
    return f"You are in room {player.current_room.name}. {player.current_room.description}\n"

def main():

    player = Player("Yoneda", room['outside'])

    com = input(message(player))
    while com!='q':

        change_rooms(player, com)
        com = input(message(player))
