import world, actions, tiles
from player_file import player

def play():
    
    world.load_tiles()
    Player = player()
    room = world.tile_exists(Player.location_x, Player.location_y)
    print(room.intro_text())
    
    while Player.is_alive() and not Player.victory:
        room = world.tile_exists(Player.location_x, Player.location_y)
        room.modify_player(Player)
        # Check again since the room could have changed the player's state
        
        if Player.is_alive() and not Player.victory:
            print("\nChoose an action:\n")
            available_actions = room.available_actions()
            
           # if isinstance(room, tiles.trader_room):
           #     available_actions.append(actions.Trade())
            
            for action in available_actions:
                print(action)
            action_input = input('===================================\nAction: ')
            
            for action in available_actions:
                if action_input == action.hotkey:
                    Player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()