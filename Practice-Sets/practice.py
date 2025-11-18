def hype_player(name, score):
print(f"{na me.upper()} JUST SCORED {score} POINTS!")
print("THE CROWD GOES WILD!")
hype_player("Jordan", 45)
hype_player("Leila", 28)

# First call
JORDAN JUST SCORED 45 POINTS!
THE CROWD GOES WILD!
# Second call
LEILA JUST SCORED 28 POINTS!
THE CROWD GOES WILD!

def calculate_likes(post_likes, post_comments):
    engagement = post_likes + (post_comments * 2)
    return engagement
viral = calculate_likes(1200, 85)
epic = calculate_likes(viral, 150)
print(epic)

1670


def generate_username(first, last):
    username = first[0].lower() + last.lower()
    if len(last) < 5:
        username += "1"
    return username
print(generate_username("Alex", "Chen"))


def weather_emoji(temp):
    if temp >= 30:
        return"HOT"
    elif temp >= 20:
        return"SUNNY"
    elif temp >= 10:
        return"CLOUDY"
    else:
        return"COLD"
today = weather_emoji(25)
tomorrow = weather_emoji(8)

today sunny tomorrow cold 


def playlist_length(songs, avg_duration):
    total_minutes = len(songs) * avg_duration
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return f"{hours}h {minutes}m"
print(playlist_length(["Thunder", "Believer"], 3.5)) defplaylist_length(songs, avg_duration):



def level_up(xp_gain):
    print(f"+{xp_gain} XP!")
    return xp_gain * 1.5
current_xp = 100
current_xp += level_up(50)
current_xp += level_up(30)
print(f"Total XP: {current_xp}")

+50 xp 
+30 xp 
total xp 220