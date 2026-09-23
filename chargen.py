'''
Created on Feb 6, 2026

@author: tim
'''
import random
import re
import cli
import data
import utils

debug_level = 2

ability_list = {"STR":0, "DEX":0, "CON":0, "INT":0, "WIS":0, "CHA":0}



score_gen_method = 1

MAGIC_USER_SPELLS = [
        # Level 1
        ["affect normal fires","burning hands","charm person","comprehend languages","dancing lights","detect magic","enlarge","erase","feather fall","find familiar","friends","hold portal","identify","jump","light","niam's magic aura","magic missile","mending","message","protection from evil","push","read magic","shield","shocking grasp","sleep","spider climb","tanzur's floating disk","unseen servant","ventriloquism","write"],
    ]

ILLUSIONIST_SPELLS = [
        # Level 1
        ["audible glamour","change self","colour spray","dancing lights","darkness","detect illusion","detect invisibility","gaze reflection","hypnotism","light","phantasmal force","wall of fog"]
    ]



def generate_ability_scores(method):
    char_abilities = ability_list.copy()
    
    if method == 0:
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
        return char_abilities
    elif method == 1:
        for ability in char_abilities:
            die_list=[]
            for _ in range(0,3):
                die = random.randint(1,6)
                die_list.append(die)
            char_abilities[ability] = sum(die_list)
        return char_abilities
    elif method == 2:
        rolls=[]
        for _ in range(6):
            roll = 0
            for _ in range(3):
                roll += random.randint(1,6)
            rolls.append(roll)

        for ability in char_abilities:
            print(rolls)
            print("Assign rolls to ability:")
            while True:
                selected_score = input(f"{ability}: >")
                if utils.is_integer(selected_score):
                    selected_score = int(selected_score)
                    if selected_score in rolls:
                        char_abilities[ability] = selected_score
                        rolls.remove(selected_score)
                        break
                    else:
                        print("*** INVALID VALUE, enter a value from the available rolls")
                        print(rolls)
        return char_abilities

    elif method == 3:
        for ability in ability_list:
            die_list=[]
            for _ in range(0,4):
                die = random.randint(1,6)
                die_list.append(die)
                
            min_val = min(die_list)
            die_list.remove(min_val)
            char_abilities[ability] = sum(die_list)
        return char_abilities

    elif method ==  4:
        rolls=[]
        for _ in range(6):
            die_list = []
            for _ in range(4):
                die = random.randint(1,6)
                die_list.append(die)
            die_list.remove(min(die_list))
            rolls.append(sum(die_list))

        for ability in char_abilities:
            print(rolls)
            print("Assign rolls to ability:")
            while True:
                selected_score = input(f"{ability}: >")
                if utils.is_integer(selected_score):
                    selected_score = int(selected_score)
                    if selected_score in rolls:
                        char_abilities[ability] = selected_score
                        rolls.remove(selected_score)
                        break
                    else:
                        print("*** INVALID VALUE, enter a value from the available rolls")
                        print(rolls)
        return char_abilities

    else:
        raise Exception("Not yet implemented")
        
def get_available_race_and_classes(abilities,desired_race,desired_class):
    available_race_and_class = {}
    for race,race_val in data.race_list.items():
        
        if desired_race == "any":
            pass
        elif desired_race == race:
            pass
        else:
            # skip this race
            continue
        
        # update the character's ability scores based on race
        tmp_abilities = abilities.copy()
        if "ability_adjustments" in race_val:
            for k,v in race_val["ability_adjustments"].items():
                tmp_abilities[k] = tmp_abilities[k] + v
        
        # verify that race meets the required ability score criteria
        illegal_race = False
        if "min ability scores" in race_val:
            for k,v in tmp_abilities.items():
                if v < race_val["min ability scores"][k]:
                    illegal_race = True
                    if debug_level > 0:
                        print(f"*** ILLEGAL RACE: {race}")
                        print(f"    ability score {k} is {v}, min required is {race_val['min ability scores'][k]}")
                    break
                
        if illegal_race:
            continue # short-circuit back to the for race loop above

        # clamp any values that exceed the max allowable ability score
        if "max ability scores" in race_val:
            for k,v in tmp_abilities.items():
                if v > race_val["max ability scores"][k]:
                    #print(f"*** Clamping racial ability score for {race}")
                    #print(f"    ability score {k} was {tmp_abilities[k]} and is now {race_val['max ability scores'][k]}")
                    tmp_abilities[k] = race_val["max ability scores"][k]
        
        # for each class the race has available
        cls_list = []
        for cls in race_val["classes"]:
            # if this is a standard class
            #if cls in data.class_specs:
                
            cls_allowed = True # assume the class is okay
            
            # use split() so we can validate multi-class options
            for test_cls in cls.split('/'):
                # check if the class's ability requirements are met
                ability_reqs = data.class_specs[test_cls]["min_scores"]
                for k,v in ability_reqs.items():
                    if tmp_abilities[k] < v:
                        cls_allowed = False
                        break

            # if nothing disallowed the class...
            if cls_allowed:
                # then it's good to go!
                if desired_class == "any" or desired_class == cls:
                    cls_list.append(cls)

        # if a class list was defined...
        if len(cls_list) > 0:
            # add it to the dictionary
            available_race_and_class[race] = cls_list

    return available_race_and_class

def select_available_race_and_classes(pi,available_race_and_class,abilities,random_sel=False):
    if available_race_and_class:
        race_and_class_list = []
        for race,cls_list in available_race_and_class.items():
            for cls in cls_list:
                race_and_class_list.append({"race": race, "class": cls}) 
        
        while True:
            if random_sel == False:
                i = 1            
                for rc in race_and_class_list:
                    print(f"{i}: {rc['race']} {rc['class']}")
                    i = i + 1
                    
                choice = input("select> ")
            else:
                choice = random.randint(1,len(race_and_class_list))
                i = len(race_and_class_list) + 1

            if utils.is_integer(choice):
                choice = int(choice)
                if (choice < 1) or (choice >= i):
                    print(f"*** INVALID.  Select between 1 and {i-1}")
                else:
                    # apply racial stats to abilities and return race and class for further processing
                    race = race_and_class_list[choice-1]["race"]
                    cls = race_and_class_list[choice-1]["class"]
                    
                    pi["race"] = race
                    pi["class"] = cls
                    
                    if "ability_adjustments" in data.race_list[race]:
                        for k,v in data.race_list[race]["ability_adjustments"].items():
                            abilities[k] = abilities[k] + v
                              
                    # clamp any values that exceed the max allowable ability score
                    for k,v in abilities.items():
                        if "max ability scores" in data.race_list[race]:
                            if abilities[k] > data.race_list[race]["max ability scores"][k]:
                                #print(f"*** Clamping racial ability score for {race}")
                                #print(f"    ability score {k} was {abilities[k]} and is now {data.race_list[race]['max ability scores'][k]}")
                                abilities[k] = data.race_list[race]["max ability scores"][k]                                              

                    pi["ability_scores"] = abilities.copy()
                    break

def is_fighter_paladin_ranger(cls):
    if cls == "fighter" or cls == "paladin" or cls == "ranger":
        return True
    else:
        return False
    
def is_magic_user(cls):
    for c in cls.split('/'):
        if c == "magic-user":
            return True
    return False

def is_illusionist(cls):
    for c in cls.split('/'):
        if c == "illusionist":
            return True
    return False
        

def roll_die(val):
    # converts "d6" or "2d4" or "3d8+9" etc. into a random roll and returns the value rolled
    
    # pre-pend a 1 for simplicity
    if val[0] == 'd':
        val = '1' + val
    
    roll_specs = re.split(r"[d+]",val)
    
    if len(roll_specs) < 2 or len(roll_specs) > 3:
        raise Exception (f"Invalid die notation: {val}")
    
    res = 0
    die_rolls = int(roll_specs[0])
    die_max = int(roll_specs[1])
    
    for _ in range(0,die_rolls):
        res = res + random.randint(1,die_max)

    if len(roll_specs) == 3:
        res = res + int(roll_specs[2])
    
    if debug_level > 1:
        print(f"rolling {val} => {res}")
    
    return res

def get_max_roll(val):
    
    max_roll = 0
    
    if val[0] == 'd':
        val = '1' + val
    
    roll_specs = re.split(r"[d+]",val)
    
    if len(roll_specs) >= 2:
        die_rolls = int(roll_specs[0])
        die_max = int(roll_specs[1])
        max_roll = die_rolls * die_max
        
    return max_roll

def generate_player_hp(pi,level):

    multi_class_divider = len(pi["class"].split('/'))
    val = 0
    
    # get player's con bonus
    con = pi['ability_scores']["CON"]
    
    # loop on player's class since multi-classing affects the Hit Die used for hit point generation
    for cls in pi["class"].split('/'):
        
        hp_modifier = 0
        
        if con <= 3:
            hp_modifier = -2
        elif con <= 6:
            hp_modifier = -1
        elif con == 15:
            hp_modifier = 1
        elif con == 16:
            hp_modifier = 2
        elif con == 17:
            hp_modifier = 2
            if is_fighter_paladin_ranger(cls):
                hp_modifier = 3
        elif con == 18:
            hp_modifier = 2
            if is_fighter_paladin_ranger(cls):
                hp_modifier = 4
        elif con == 19:
            hp_modifier = 2
            if is_fighter_paladin_ranger(cls):
                hp_modifier = 5
        
        # get hit-die
        hd = data.class_specs[cls]["hit_die"][level-1]
        if cls == 'ranger' and level == 1:
            if hp_modifier > 0:
                # Rangers apply CON bonus to their both of their HD rolls at first level
                roll = int((roll_die(hd) + 2 * hp_modifier) / multi_class_divider)
            else:
                roll = int((roll_die(hd) + hp_modifier) / multi_class_divider)
        else:
            roll = int((roll_die(hd) + hp_modifier) / multi_class_divider)
        if roll <= 0:
            roll = 1
        val = val + roll
    
    # generate hp based on class & con bonus
    pi["hp"] = val
    
def generate_player_alignment(pi):
    
    # assume any alignment for law/chaos, good/evil
    lnc = set("lawful/neutral/chaotic".split('/'))
    gne = set("good/neutral/evil".split('/'))
    
    for cls in pi["class"].split('/'):
        if data.class_specs[cls]["alignment"]["lnc"] != "any":
            # remove the non-listed alignments
            lnc = set(data.class_specs[cls]["alignment"]["lnc"].split("/")) & lnc
        if data.class_specs[cls]["alignment"]["gne"] != "any":
            # remove the non-listed alignments
            gne = set(data.class_specs[cls]["alignment"]["gne"].split("/")) & gne

    lnc = random.choice(list(lnc))
    gne = random.choice(list(gne))
    
    if lnc == "neutral" and gne == "neutral":
        pi["alignment"] = "true neutral"
    else:   
        pi["alignment"] = lnc + " " + gne

def generate_spell_book_spells(pi):
    if is_magic_user(pi["class"]):
        spell_list = MAGIC_USER_SPELLS[0].copy()
    
        # ensure first spell is read magic
        pi["spell book"] = []
        pi["spell book"].append("read magic")
        spell_list.remove("read magic")
        
        for _ in range(0,3):
            spell = spell_list[random.randint(0,len(spell_list)-1)]
            pi["spell book"].append(spell)
            spell_list.remove(spell)
    elif is_illusionist(pi['class']):
        spell_list = ILLUSIONIST_SPELLS[0].copy()
        
        pi["spell book"] = []
        for _ in range(0,3):
            spell = spell_list[random.randint(0,len(spell_list)-1)]
            pi["spell book"].append(spell)
            spell_list.remove(spell)

def generate_starting_funds(pi):
    # select the class that can generate the most gold
    
    max_gold = 0
    for cls in pi["class"].split('/'):
        class_max_gold = get_max_roll(data.class_specs[cls]["gold"]["die"]) * data.class_specs[cls]["gold"]["multiplier"]
        if class_max_gold > max_gold:
            max_gold = class_max_gold
            gold_die = data.class_specs[cls]["gold"]["die"]
            gold_multiplier = data.class_specs[cls]["gold"]["multiplier"]
            
    gold = roll_die(gold_die) * gold_multiplier
    
    pi["gold"] = gold
        
def generate_weight_and_height(pi):
    race = pi['race']
    
    height = data.race_list[race]["height"]
    height_val = height["base"]*12.0 + (roll_die(height["mod die"]))
    if int(height_val % 12.0) == 0:
        pi["height"] = f"{int(height_val/12.0)}ft"
    else:
        pi["height"] = f"{int(height_val/12.0)}ft {int(height_val%12.0)}in"
        
    weight = data.race_list[race]["weight"]
    weight_val = weight["base"] + (roll_die(weight["mod die"]))
    pi["weight"] = f"{int(weight_val)}lbs"
    
def generate_age(pi):
    race = pi['race']
    cls = pi['class']
    
    age = data.race_list[race]["age"]
    
    # by fiat: grab the oldest age for multi-class characters
    cur_age = 0
    for c in cls.split('/'):
        r = roll_die(age[c])
        if r > cur_age:
            cur_age = r
            
    pi["age"] = f"{cur_age} yrs"
    
def generate_gender(pi):
    # flip a coin
    if roll_die("1d2") == 1:
        pi["gender"] = "male"
    else:
        pi["gender"] = "female"
    
def display_player_info(pi):
    # name / xp / age
    print(f"     name: {'':<25} {'xp:':>7} {0:<7} {'age:':>7} {pi['age']:<4}")
    
    # class / hp / height
    print(f"    class: {pi['class']:<25} {'hp:':>7} {pi['hp']:<7} {'height:':>7} {pi['height']}")
    
    # alignment / AC / weight
    print(f"alignment: {pi['alignment']:<25} {'AC:':>7} {'':<7} {'weight:':>7} {pi['weight']}")
    
    # race / lvl / gender
    print(f"     race: {pi['race']:<25} {'level:':>7} {pi['level']:<7} {'gender:':>7} {pi['gender']}")
    
    # MC / MC / MC
    
    # abilities
    print("\nAbility scores")
    for k,v in pi["ability_scores"].items():
        print(f"{k}: {v}")
    
    # print(f"\nAdditional ability info TBD")
    # str, to-hit, damage, encumbrance, minor test, major test
    # dex, surprise, missile to-hit, ac, agility save bonus, missile initiative bonus
    # con, hp, resurrection success, system shock
    # int, add'l languages
    # wis, mental save
    # cha, max henchman, loyalty, reaction
    # movement rate - determined via race and armor
    
    # save vs
    # aimed magic items / breath weapons / death, paralysis, poison / petrification, polymorph / spells
    # pick best saving throws for multi-classes (a lower save value is better)
    saves = None
    for cls in pi["class"].split("/"):
        tmp_saves = data.class_specs[cls]["saving throws"][0]
        if saves:
            for k,v in tmp_saves.items():
                if saves[k] > v:
                    saves[k] = v
        else:
            saves = tmp_saves.copy()
    print("\nSaving Throws")
    for k,v in saves.items():
        print(f"{k:>23}: {v}")
    
    # weapons & armor
    
    # roll to hit AC
    to_hit_table = None
    for cls in pi["class"].split("/"):
        tmp_to_hit_table = data.class_specs[cls]["to-hit table"][0]
        if to_hit_table:
            i = 0
            for i,v in enumerate(tmp_to_hit_table):
                if to_hit_table[i] > v:
                    to_hit_table[i] = v
        else:
            to_hit_table = tmp_to_hit_table.copy()
    print("\nTo-hit Table")
    for i in range(10,-11,-1):
        print(f"{i:>4}",end="")
    print()
    for v in to_hit_table:
        print(f"{v:>4}",end="")
    print()
    
    # equipment
    
    # wealth
    
    # special abilities (race)
    # languages
    
    # special abilities (class)
    #print("\nClass abilities")
    if is_magic_user(pi['class']) or is_illusionist(pi['class']):
        print()
        print(f"spell book:")
        for spell in pi['spell book']:
            print(f"  {spell}")
    
    # notes
        
    print(f"\ngold: {pi['gold']}")

def main():
    print("Welcome to dapt's OSRIC 3.0 chargen!")
    
    while True:
        char_count = input("# of characters to generate>")
        if utils.is_integer(char_count) >= 1:
            char_count = int(char_count)
            break
        else:
            print("Invalid entry: {char_count}.  Enter 1 or more.")
    
    desired_race = cli.select_desired_race()
    desired_class = cli.select_desired_class(desired_race)
             
    if debug_level > 2:
        print(f"desired race: {desired_race}")
        print(f"desired class: {desired_class}")
        
    score_gen_method = cli.select_ability_generation_method()
    
    print("--------------------------------------------------------------------------------------")
    i = 0
    
    while i < char_count:
        #pi = player_info.copy()
        pi = {}
        pi['level'] = 1
        abilities = generate_ability_scores(score_gen_method)
        available_race_and_classes = get_available_race_and_classes(abilities,desired_race,desired_class)
        
        if not available_race_and_classes:
            if debug_level > 0:
                print("*** NO LEGAL RACES+CLASSES, REROLL!!! ***")
            continue
        else:
            select_available_race_and_classes(pi,available_race_and_classes,abilities,(char_count > 1))
        
        generate_player_hp(pi,1)
        generate_player_alignment(pi)
        generate_spell_book_spells(pi)
        generate_starting_funds(pi)
        generate_weight_and_height(pi)
        generate_age(pi)
        # apply age to ability scores
        generate_gender(pi)
        #generate_starting_equipment()
        
        display_player_info(pi)
        
        i = i + 1
        
        print("--------------------------------------------------------------------------------------")

    
if __name__ == '__main__':
    main()
    print("Done!")
