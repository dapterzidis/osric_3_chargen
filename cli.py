import chargen
import utils
import data
import random



def select_ability_generation_method():
    
    while True:
        print("Select rolling method:")
        print("0. Pre-defined")
        print("1. Hard mode")
        print("2. Difficult mode")
        print("3. Normal mode")
        print("4. Flexible mode")
    
        score_gen_method = input("select> ")
        
        if utils.is_integer(score_gen_method):
            score_gen_method = int(score_gen_method)
            if score_gen_method >= 0 and score_gen_method <= 4:
                return score_gen_method

def assign_abilities_manually(char_abilities):
    for ability in char_abilities:
        while True:
            new_score=input(f"{ability}: >")
            if utils.is_integer(new_score):
                new_score = int(new_score)
                if new_score >= 3 and new_score <= 18:
                    char_abilities[ability] = new_score
                    break
                else:
                    print("*** INVALID VALUE, enter 3-18 ***")
    # return char_abilities   

def choose_roll_order(character_abilities, rolls):
    unordered_rolls = rolls.copy()
    for ability in character_abilities:
        print(unordered_rolls)
        print("Assign rolls to ability:")
        while True:
            selected_roll = input(f"{ability}: >")
            if utils.is_integer(selected_roll):
                selected_roll = int(selected_roll)
                if selected_roll in unordered_rolls:
                    character_abilities[ability] = selected_roll
                    unordered_rolls.remove(selected_roll)
                    break
                else:
                    print("*** INVALID VALUE, enter a value from the available rolls")
                    print(unordered_rolls)
        # return character_abilities    

def generate_ability_scores(method):
    char_abilities = data.ability_list.copy()
    
    if method == 0: # 
        assign_abilities_manually(char_abilities)
        return char_abilities
    elif method == 1:  # Hard Mode, 3d6, in order
        rolls = chargen.generate_stats(3)
        for ability in char_abilities:
            char_abilities[ability] = rolls.pop(0)
        return char_abilities
    
    elif method == 2: # Difficult Mode, 3d6, pick order
        rolls = chargen.generate_stats(3)
        choose_roll_order(char_abilities, rolls)
        return char_abilities

    elif method == 3: # Normal Mode, 4d6, in order
        rolls = chargen.generate_stats(4)
        for ability in char_abilities:
            char_abilities[ability] = rolls.pop(0)
        return char_abilities        

    elif method ==  4: # Flexible Mode, 4d6, pick order
        rolls = chargen.generate_stats(4)
        choose_roll_order(char_abilities, rolls)
        return char_abilities
    
    else:
        raise Exception("Not yet implemented")

def select_desired_race():
    # gather all races
    r_list = []
    for r,_ in data.race_list.items():
        r_list.append(r)

    r_list.append("any")
    r_list.sort()

    while True:
        for i,r in enumerate(r_list):
            print(f"{i:>2} {r}")
        
        choice = input("select desired race>")
        if utils.is_integer(choice) and int(choice) >= 0 and int(choice) < len(r_list):
            desired_race = r_list[int(choice)]
            break
        else:
            print("Invalid selection {int(choice)}.  Try again.")
    
    return desired_race 

def select_desired_class(desired_race):
    # gather all available classes across all races
    c_list = []
    if desired_race == "any":
        for _,v in data.race_list.items():
            for c in v['classes']:
                if c not in c_list:
                    c_list.append(c)
    else:
        for c in data.race_list[desired_race]['classes']:
            if c not in c_list:
                c_list.append(c) 
    
    c_list.append("any")
    c_list.sort()

    while True:
        for i,c in enumerate(c_list):
            print(f"{i:>2} {c}")
            
        choice = input("select desired class>")
        if utils.is_integer(choice) and int(choice) >= 0 and int(choice) < len(c_list):
            desired_class = c_list[int(choice)]
            break
        else:
            print("Invalid selection {int(choice)}.  Try again.")

    return desired_class