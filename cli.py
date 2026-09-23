


def select_ability_generation_method():
    
    while True:
        print("Select rolling method:")
        print("0. Pre-defined")
        print("1. Hard mode")
        print("2. Difficult mode")
        print("3. Normal mode")
        print("4. Flexible mode")
    
        score_gen_method = input("select> ")
        
        if is_integer(score_gen_method):
            score_gen_method = int(score_gen_method)
            if score_gen_method >= 0 and score_gen_method <= 4:
                return score_gen_method
