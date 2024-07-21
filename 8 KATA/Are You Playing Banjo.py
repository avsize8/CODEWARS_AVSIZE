def are_you_playing_banjo(name):
    for i in name:
        if i[0] == "R" or i[0] == "r":
            return f"{name} plays banjo" 
        else: 
            return f"{name} does not play banjo"