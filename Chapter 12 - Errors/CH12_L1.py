def main():
    print(get_player_record(1))
    print(get_player_record(2))
    print(get_player_record(3))
    print(get_player_record(4))


# Don't edit below this line


def get_player_record(player_id):
    try:
        if player_id == 1:
            return {"name": "Slayer", "level": 128}
        if player_id == 2:
            return {"name": "Dorgoth", "level": 300}
        if player_id == 3:
            return {"name": "Saruman", "level": 4000}
    except Exception as e:
        print(e)


main()
