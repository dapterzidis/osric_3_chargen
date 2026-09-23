race_list = {
        "dwarf" :       {
                            "ability_adjustments": {"CON":1,"CHA":-1}, 
                            "classes" : ["assassin","cleric","fighter","thief","fighter/thief"],
                            "languages" : ["common","dwarfish","gnomish","goblin","kobold","orcish","alignment tongue"],
                            "min ability scores" : {"STR":8, "DEX":3, "CON":12, "INT":3, "WIS":3, "CHA":3},
                            "max ability scores" : {"STR":18, "DEX":17, "CON":19, "INT":18, "WIS":18, "CHA":16},
                            "movement" : "90ft",
                            "height" : {"base":4.0,  "mod die":"3d4"},
                            "weight" : {"base":150.0, "mod die":"5d10"},
                            "age": {"cleric": "2d20+250","fighter":"5d4+40","thief":"3d6+75","assassin":"3d6+75"}
                        },
        "elf" :         {
                            "ability_adjustments": {"DEX":1,"CON":-1}, 
                            "classes": ["assassin","cleric","fighter","magic-user","thief","fighter/magic-user", "fighter/thief", "magic-user/thief", "fighter/magic-user/thief"],
                            "languages": ["common","elven","gnoll","gnomish","goblin","halfling","hobgoblin","orcish","alignment tongue"],
                            "min ability scores" : {"STR":3, "DEX":7, "CON":6, "INT":8, "WIS":3, "CHA":8},
                            "max ability scores" : {"STR":18, "DEX":19, "CON":18, "INT":18, "WIS":18, "CHA":18},
                            "movement" : "120ft",
                            "height" : {"base":4.5,  "mod die":"3d4"},
                            "weight" : {"base":70.0, "mod die":"5d10"},
                            "age":{"cleric":"10d10+500","fighter":"5d6+130","magic-user":"5d6+150","thief":"5d6+100","assassin":"5d6+100"}
                            
                        },
        "gnome" :       {
                            "classes": ["assassin","cleric", "fighter","illusionist", "thief", "fighter/illusionist", "fighter/thief", "illusionist/thief"],
                            "languages" : ["common","dwarfish","gnomish","goblin","halfling","kobold","burrowing animals","alignment tongue"],
                            "min ability scores" : {"STR":6, "DEX":7, "CON":8, "INT":7, "WIS":3, "CHA":3},
                            "max ability scores" : {"STR":18, "DEX":18, "CON":18, "INT":18, "WIS":18, "CHA":18},
                            "movement" : "90ft",
                            "height" : {"base":2.83,  "mod die":"3d4"},
                            "weight" : {"base":45.0, "mod die":"4d10"},
                            "age": {"cleric":"3d12+300","fighter":"5d4+60","illusionist":"2d12+100","thief":"5d4+80","assassin":"5d4+80"}
                        },
        "half-elf" :    {
                            "classes": ["assassin", "cleric", "druid", "fighter", "magic-user", "ranger", "thief", "cleric/fighter", "cleric/ranger", "cleric/magic-user", "fighter/magic-user", "fighter/thief", "cleric/fighter/magic-user", "fighter/magic-user/thief"],
                            "languages" : ["common","elven","gnoll","gnomish","goblin","halfling","hobgoblin","orcish","alignment tongue"],
                            "min ability scores" : {"STR":3, "DEX":6, "CON":8, "INT":4, "WIS":3, "CHA":3},
                            "max ability scores" : {"STR":18, "DEX":18, "CON":18, "INT":18, "WIS":18, "CHA":18},
                            "movement" : "120ft",
                            "height" : {"base":5.0,  "mod die":"4d4"},
                            "weight" : {"base":90.0, "mod die":"5d10"},
                            "age" : {"cleric":"2d4+40","druid":"2d4+40","fighter":"3d4+22","ranger":"3d4+22","magic-user":"2d8+30","thief":"3d8+22","assassin":"3d8+22"}
                        },
        "halfling" :    {
                            "ability_adjustments": {"DEX":1,"STR":-1}, 
                            "classes" : ["fighter", "druid", "thief", "fighter/thief"],
                            "languages" : ["common","dwarfish","gnomish","goblin","halfling","orcish","alignment tongue"],
                            "min ability scores" : {"STR":6, "DEX":8, "CON":10, "INT":6, "WIS":3, "CHA":3},
                            "max ability scores" : {"STR":17, "DEX":18, "CON":19, "INT":18, "WIS":17, "CHA":18},
                            "movement" : "90ft",
                            "height" : {"base":2.83,  "mod die":"3d4"},
                            "weight" : {"base":45.0, "mod die":"4d10"},
                            "age" : {"fighter":"3d4+20","druid":"3d4+40","thief":"2d4+40"}
                        },
        "half-orc" :    {
                            "ability_adjustments": {"STR":1,"CON":1,"CHA":-2},
                            "classes" : ["assassin", "cleric", "fighter", "thief", "cleric/fighter", "cleric/thief", "cleric/assassin", "fighter/thief", "fighter/assassin"],
                            "languages" : ["common","orcish","alignment tongue"],
                            "min ability scores" : {"STR":6, "DEX":3, "CON":13, "INT":3, "WIS":3, "CHA":3},
                            "max ability scores" : {"STR":18, "DEX":17, "CON":19, "INT":17, "WIS":14, "CHA":12},
                            "movement" : "120ft",
                            "height" : {"base":5.5,  "mod die":"3d4"},
                            "weight" : {"base":150.0, "mod die":"5d10"},
                            "age" : {"cleric":"1d4+20","fighter":"1d4+13","thief":"2d4+20","assassin":"2d4+20"}
                        },
        "human" :       {
                            "classes": ["assassin","cleric","druid","fighter","illusionist","magic-user","monk","paladin","ranger","thief"],
                            "languages" : ["common","alignment tongue"],
                            "movement" : "120ft",
                            "height" : {"base":5.33,  "mod die":"3d4"},
                            "weight" : {"base":140.0, "mod die":"6d10"},
                            "age" : {"cleric":"1d4+20","druid":"1d4+20","monk":"1d4+20","fighter":"1d4+15","paladin":"1d4+15","ranger":"1d4+15","magic-user":"2d8+24","illusionist":"2d8+24","thief":"1d4+20","assassin":"1d4+20"}
                        }
    }

class_specs = {
        "assassin":     {
                            "min_scores" : {"STR":12,  "DEX":12,   "CON":6,    "INT":11,   "WIS":6},
                            "max level": 15,
                            "hit_die":["1d6","2d6","3d6","4d6","5d6","6d6","7d6","8d6","9d6","10d6","11d6","12d6","13d6","14d6","15d6"],
                            "hit_die_max":15,
                            "xp levels":[0,1500,3000,6000,12000,25000,50000,100000,200000,300000,450000,600000,750000,1000000,1500000],
                            "alignment": {"lnc": "any", "gne": "evil"},
                            "prime_req":"none",
                            "shields_allowed":"any",
                            "armor_allowed": ["leather","studded leather"],
                            "weapons_allowed": "any",
                            "weapon_proficiencies":3,
                            "nonproficiency_penalty":-3,
                            "weapon_specialization":"no",
                            "gold":{"die":"2d6","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 14, "breath weapons": 16, "death/paralysis/poison" : 13, "petrification/polymorph": 12, "spells": 15},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1 0  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25,26]
                                            ]
                        },
                            
        "cleric":       {
                            "min_scores" : {"STR":6,               "CON":6,    "INT":6,    "WIS":9,    "CHA":6},
                            "max level": 20,
                            "hit_die":["1d8","2d8","3d8","4d8","5d8","6d8","7d8","8d8","9d8","9d8+2","9d8+4","9d8+6","9d8+8","9d8+10","9d8+12","9d8+14","9d8+16","9d8+18","9d8+20","9d8+22"],
                            "hit_die_max":9,
                            "xp levels":[0,1500,3000,6000,13000,27000,55000,110000,220000,450000,675000,900000,1125000,1350000,1575000,1800000,2050000,2300000,2550000,2700000],
                            "alignment": {"lnc": "any", "gne": "any"},
                            "prime_req":{"xp_bonus":0.1, "min_stats": {"WIS":16}},
                            "shields_allowed":"any",
                            "armor_allowed": "any",
                            "weapons_allowed": ["club","flail","hammer","mace","staff","torch","flaming oil (special)"],
                            "weapon_proficiencies":2,
                            "nonproficiency_penalty":-3,
                            "weapon_specialization":"no",
                            "gold":{"die":"3d6","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 14, "breath weapons": 16, "death/paralysis/poison" : 10, "petrification/polymorph": 13, "spells": 15},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25]
                                            ]
                        },
        
        "druid":        
                        {
                            "min_scores" : {"STR":6,               "CON":6,    "INT":6,    "WIS":12,   "CHA":15},
                            "max level":14,
                            "hit_die":["1d8","2d8","3d8","4d8","5d8","6d8","7d8","8d8","9d8","10d8","11d8","12d8","13d8","14d8"],                            
                            "hit_die_max":14,
                            "xp levels":[0,2000,4000,8000,12000,20000,35000,60000,90000,125000,200000,300000,750000,1500000],
                            "alignment": {"lnc": "any", "gne": "neutral"},
                            "prime_req":{"xp_bonus":0.1, "min_stats": {"WIS":16,"CHA":16}},
                            "shields_allowed":"wooden shields",
                            "armor_allowed": "leather",
                            "weapons_allowed": ["club","dagger","dart","hammer","scimitar","sling","spear","staff","torch","flaming oil (special)"],
                            "weapon_proficiencies":2,
                            "nonproficiency_penalty":-4,
                            "weapon_specialization":"no",
                            "gold":{"die":"3d6","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 14, "breath weapons": 16, "death/paralysis/poison" : 10, "petrification/polymorph": 13, "spells": 15},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25]
                                            ]
                        },
                        
        "fighter":      
                        {
                            "min_scores" : {"STR":9,   "DEX":6,    "CON":7,    "INT":3,    "WIS":6,    "CHA":6},
                            "max level": 20,
                            "hit_die":["1d10","2d10","3d10","4d10","5d10","6d10","7d10","8d10","9d10","9d10+3","9d10+3","9d10+6","9d10+9","9d10+12","9d10+15","9d10+18","9d10+21","9d10+24","9d10+27","9d10+30","9d10+33"],                            
                            "hit_die_max":9,
                            "xp levels" : [0,2000,4000,8000,17000,35000,70000,125000,250000,500000,750000,1000000,1250000,1500000,1750000,2000000,2250000,2500000,2750000,3000000],
                            "alignment": {"lnc": "any", "gne": "any"},
                            "prime_req":{"xp_bonus":0.1, "min_stats": {"STR":16}},
                            "shields_allowed":"any",
                            "armor_allowed": "any",
                            "weapons_allowed": "any",
                            "weapon_proficiencies":4,
                            "nonproficiency_penalty":-2,
                            "weapon_specialization":"optional",
                            "gold":{"die":"5d4","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 18, "breath weapons": 20, "death/paralysis/poison" : 16, "petrification/polymorph": 17, "spells": 19},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25]
                                            ]                        
                        },
        "illusionist":  
                        {
                            "min_scores": {"STR":6,   "DEX":16,               "INT":15,   "WIS":6,    "CHA":6},
                            "max level": 20,
                            "hit_die": ["1d4","2d4","3d4","4d4","5d4","6d4","7d4","8d4","9d4","10d4","10d4+1","10d4+2","10d4+3","10d4+4","10d4+5","10d4+6","10d4+7","10d4+8","10d4+9","10d4+10"],
                            "hit_die_max":10,
                            "xp levels": [0,2500,4750,9000,18000,35000,60000,95000,145000,220000,440000,660000,880000,1100000,1320000,1540000,1760000,1980000,2200000,2420000],
                            "alignment": {"lnc": "any", "gne": "any"},
                            "prime_req": "none",
                            "shields_allowed":"none",
                            "armor_allowed": "none",
                            "weapons_allowed": ["dagger","dart","oil","staff"],
                            "weapon_proficiencies":1,
                            "nonproficiency_penalty":-5,
                            "weapon_specialization":"no",
                            "gold":{"die":"2d4","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 11, "breath weapons": 15, "death/paralysis/poison" : 14, "petrification/polymorph": 13, "spells": 12},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25,26]
                                            ]    
                        },
        "magic-user":   
                        {
                            "min_scores" : {           "DEX":6,    "CON":6,    "INT":9,    "WIS":6,    "CHA":6},
                            "max level" : 20,
                            "hit_die": ["1d4","2d4","3d4","4d4","5d4","6d4","7d4","8d4","9d4","10d4","11d4","11d4+1","11d4+2","11d4+3","11d4+4","11d4+5","11d4+6","11d4+7","11d4+8","11d4+9"],
                            "hit_die_max":10,
                            "xp levels": [0,2400,4800,10250,22000,40000,60000,80000,140000,250000,375000,750000,1125000,1500000,1875000,2250000,2625000,3000000,3375000,3750000],
                            "alignment": {"lnc": "any", "gne": "any"},
                            "prime_req": {"xp_bonus":0.1, "min_stats": {"INT":16}},
                            "shields_allowed":"none",
                            "armor_allowed": "none",
                            "weapons_allowed": ["dagger","dart","oil","staff"],
                            "weapon_proficiencies":1,
                            "nonproficiency_penalty":-5,
                            "weapon_specialization":"no",
                            "gold":{"die":"2d4","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 11, "breath weapons": 15, "death/paralysis/poison" : 14, "petrification/polymorph": 13, "spells": 12},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25,26]
                                            ]                                
                        },
        "monk":         
                        {
                            "min_scores" : {"STR":10,  "DEX":15,                           "WIS":10,},
                            "max level": 17,
                            "hit_die":["2d4","3d4","4d4","5d4","6d4","7d4","8d4","9d4","10d4","11d4","12d4","13d4","14d4","15d4","16d4","17d4","18d4"],
                            "hit_die_max":18,
                            "xp levels" : [0,2000,5000,10000,21250,45000,100000,200000,350000,500000,700000,950000,1250000,1750000,2250000,1750000,3250000],
                            "alignment": {"lnc": "lawful", "gne": "any"},
                            "prime_req": "none",
                            "shields_allowed":"none",
                            "armor_allowed": "none",
                            "weapons_allowed": ["club","crossbow","dagger","hand axe","javelin","pole arm","spear","staff"],
                            "weapon_proficiencies":1,
                            "nonproficiency_penalty":-3,
                            "weapon_specialization":"no",
                            "gold":{"die":"5d4","multiplier":1},
                            "saving throws": [
                                                {"aimed magic items": 14, "breath weapons": 16, "death/paralysis/poison" : 13, "petrification/polymorph": 12, "spells": 15},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25]
                                            ]                                 
                        },
        "paladin":      
                        {
                            "min_scores" : {"STR":12,  "DEX":6,    "CON":9,    "INT":9,    "WIS":13,   "CHA":17},
                            "max level": 20,
                            "hit_die":["1d10","2d10","3d10","4d10","5d10","6d10","7d10","8d10","9d10","9d10+3","9d10+3","9d10+6","9d10+9","9d10+12","9d10+15","9d10+18","9d10+21","9d10+24","9d10+27","9d10+30","9d10+33"],                            
                            "hit_die_max":9,
                            "xp levels" : [0,2550,5500,12500,25000,45000,95000,175000,325000,600000,1000000,1350000,1700000,2050000,2400000,2750000,3100000,3450000,3800000,4150000],
                            "alignment": {"lnc": "lawful", "gne": "good"},
                            "prime_req": {"xp_bonus":0.1, "min_stats": {"STR":16,"WIS":16}},
                            "shields_allowed":"any",
                            "armor_allowed": "any",
                            "weapons_allowed": "any",
                            "weapon_proficiencies":3,
                            "nonproficiency_penalty":-2,
                            "weapon_specialization":"optional",
                            "gold":{"die":"5d4","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 14, "breath weapons": 15, "death/paralysis/poison" : 12, "petrification/polymorph": 13, "spells": 15},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25]
                                            ]                                 
                        },
        "ranger":       
                        {
                            "min_scores" : {"STR":13,  "DEX":6,    "CON":14,   "INT":13,   "WIS":14,   "CHA":6},
                            "max level": 20,
                            "hit_die":["2d8","3d8","4d8","5d8","6d8","7d8","8d8","9d8","10d8","11d8","11d8+2","11d8+4","11d8+6","11d8+8","11d8+10","11d8+12","11d8+14","11d8+16","11d8+18","11d8+20"],                            
                            "hit_die_max":11,
                            "xp levels": [0,2250,4500,9500,20000,40000,90000,150000,225000,325000,650000,975000,1300000,1625000,1950000,2275000,2600000,2925000,3250000,3575000],
                            "alignment": {"lnc": "any", "gne": "good"},
                            "prime_req": {"xp_bonus":0.1, "min_stats": {"STR":16,"INT":16,"WIS":16}},
                            "shields_allowed":"any",
                            "armor_allowed": "any",
                            "weapons_allowed": "any",
                            "weapon_proficiencies":3,
                            "nonproficiency_penalty":-2,
                            "weapon_specialization":"optional",
                            "gold":{"die":"5d4","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 16, "breath weapons": 17, "death/paralysis/poison" : 14, "petrification/polymorph": 15, "spells": 17},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25,26]
                                            ]                                 
                        },
        "thief":        
                        {
                            "min_scores" : {"STR":6,   "DEX":9,    "CON":6,    "INT":6,                "CHA":6},
                            "max level": 20,
                            "hit_die":["1d6","2d6","3d6","4d6","5d6","6d6","7d6","8d6","9d6","10d6","10d6+2","10d6+4","10d6+6","10d6+8","10d6+10","10d6+12","10d6+14","10d6+16","10d6+18","10d6+20"],                            
                            "hit_die_max":10,
                            "xp levels":[0,1250,2500,5000,10000,20000,40000,70000,110000,160000,220000,440000,660000,880000,1100000,1320000,1540000,1760000,1980000,2200000],
                            "alignment": {"lnc": "any", "gne": "neutral/evil"},
                            "prime_req": {"xp_bonus":0.1, "min_stats": {"STR":16,"INT":16,"WIS":16}},
                            "shields_allowed":"any",
                            "armor_allowed": "any",
                            "weapons_allowed": "any",
                            "weapon_proficiencies":3,
                            "nonproficiency_penalty":-2,
                            "weapon_specialization":"optional",
                            "gold":{"die":"5d4","multiplier":10},
                            "saving throws": [
                                                {"aimed magic items": 14, "breath weapons": 16, "death/paralysis/poison" : 13, "petrification/polymorph": 12, "spells": 15},
                                            ],
                            "to-hit table" : [#  10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
                                                [11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25,26]
                                            ]                               
                        }
    }

ability_list = {"STR":0, "DEX":0, "CON":0, "INT":0, "WIS":0, "CHA":0}