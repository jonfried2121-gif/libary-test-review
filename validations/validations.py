

def number_validation(number):
    num = int(number)
    return num

def bigger_eqal_0(number):
    return number >= 0

def bigger_than_0(number):
    return number > 0

def valid_string(string:str):
    return string.isalpha()

def valid_pick(pick):
    valid_choises ={1,2,3,4,5,6,7,8}
    return pick in valid_choises

def is_empty_string(string:str):
    return string.strip() == ""

def all_menu_validations(pick):
    try:
        pick =number_validation(pick)
    except ValueError:
        return "please enter a valid choose"
        
    if not valid_pick(pick):
        return "please pick a valid doption"
    return "ok"   

          






    