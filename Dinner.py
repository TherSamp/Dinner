
import random

def get_choice():
    player_choice = input("What day of the week is it? ")
    choice = {"day": player_choice}
    return choice

def check_recipe(day):
    print(f"So it's {day}... looks like we're having…" )
    if day == "Thursday" or day == "thursday":
        return "Pasta with Zucchini!"
    else:
        options = ["Minestrone", "Pizza", "Quiche", "Risotto", "Rice with baked vegetables", "Sandwiches"]
        return random.choice(options)
    
choice = get_choice()
result = check_recipe(choice["day"])
print(result)

