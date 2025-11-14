def combo_multiplier(base, combo):
    print(f"{combo}x COMBO!")
    return base * combo

score = 100
score = combo_multiplier(score, 3)
score = combo_multiplier(score, 5)
print(f"FINAL SCORE: {score}")

3x combo
5x combo 
score 1500

def streak_bonus(days):
    if days >= 30:
        return"FIRE"
    elif days >= 7:
        return"HOT"
    elif days >= 3:
        return"WARM"
    else:
        return"COLD"
user1 = streak_bonus(45)
user2 = streak_bonus(5)

Fire Warm HOT

def generate_hashtag(phrase):
    titled = phrase.title()
    no_spaces = titled.replace(" ", "")
    hashtag = "#" + no_spaces
    
    iflen(hashtag) > 20:
        return"TOO LONG
    return hashtag
print(generate_hashtag("hello world"))


def fitness_goal(steps, target)
percent = (steps / target)
    if percent >= 100:
        return "GOAL SMASHED!"):
    else:
        returnf"{percent:.0f}% — Keep going!"
result = fit
print(resultness_goal(12500, 10000))


def battle_cry(hero, weapon, damage):
    message = f"{hero.upper()} swings {weapon.upper()} for {damage > 80:
    if damage > 80
        message += " CRITICAL HIT!"
    return message

print(battle_cry("Draco", "Fire Sword", 95))


def ai_response(user_input):
    mood = "neutral"
    if "happy" in user_input.lower():
        mood = "excited"
    elif"sad" in user_input.lower():
        mood = "supportive"
    returnf"AI feels {mood}!

msg1 = ai_response("I'm so HAPPY today!")
msg2 = ai_response("I feel sad...")
msg3 = ai_response("Python is cool")
print(msg1)

AI feels Excited!


def weather_alert(temp, wind_speed):
    alert = ""
    if temp > 30:
        alert += "STAY HYDRATED"
    if temp < 5:
    if alert:
        alert += " + "
    alert += "BUNDLE UP"
    if wind_speed > 40:
    if alert:
        alert += " + "
    alert += "HOLD ON TO YOUR HAT"
    if not alert:
        return"ENJOY THE WEATHER"
    return