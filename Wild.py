import string #To get rid of punctuation 
import random #Randomize encounters and opponent moves
import time #Time delays code before executing it so the text is not overwhelming.

def remove_punctuation(input_string):
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    
    return out_string

def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

def end_battle(input_list):
    if 'run' in input_list:
        output = True
        return True
    else:
        output = False
        return False
    
    return output

def is_pokemonselect(input_string):
    if 'pokemon' in input_string:        
        output = True
        return True
        
    else:
        
        output = False
        return False
        
    return output

def send_pikachu(input_list):
    if 'pikachu' in input_list:
        output = True
        return True
    else:
        output = False
        return False
    
    return output

def fight_select(input_list):
    if 'fight' in input_list:
        output = True
        return True
    
    else:
        output = False
        return False
    
    return output

def use_thunderbolt(input_list):
    if 'thunderbolt' in input_list:
        output = True
        return True
    
    else:
        output = False
        return False
    
    return output

def use_tackle(input_list):
    if 'tackle' in input_list:
        output = True
        return True
    
    else:
        output = False
        return False
    
    return output
    
    # This cell defines a collection of input and output strings the system can respond with
EXP = range(42,76)

DAMAGE_OUT = ["The wild Charmander's HP fell!" ,"The wild Charmander's HP has dropped!"]

#Charmander's moveset
WILD_MOVES = ["Ember", "Scratch"] 

UNKNOWN = ['umm...', "Pikachu didn't understand"]

POKEMONSELECT = "Select a pokemon to send out! [Pikachu]"

def have_a_battle():
    import string #To get rid of punctuation 
    import random #Randomize encounters and opponent moves
    import time #Time delays code before executing it so the text is not overwhelming.
    
    """Function that introduces the battle."""
    def begin_encounter():

            print("-" * 72)
            print("A wild Charmander has appeared!")
            time.sleep(1.5)
            print('')
            print("Go! Pikachu!")
            time.sleep(1.7)
            print('')
            print("What will Pikachu do?")
            print('[Fight] [Run] [Pokemon]')
    
    begin_encounter()
        
    """Initial Pokemon HP (Hit Points/Health)"""
    charmanderHP = 44

    pikachuHP = 56
    
    """Main function that maintins the battle."""    
    battle = True
    while battle:
        
        
        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Prepare the input message
        msg = prepare_text(msg)
        
        # Check if the input is PokemonSelect
        pokemonset = is_pokemonselect(msg)

        # Check for an end msg 
        if end_battle(msg):
            out_msg = 'Got away safely!'
            battle = False
        
    
        # Check for a pikachu send out msg
        if send_pikachu(msg):
            print ('Go! Pikachu!')
            print ('')
            print ("What will Pikachu do?")
            time.sleep(1.5)
            out_msg = '[Fight] [Run] [Pokemon]'
            battle = True
       
        
        # Check for a fight msg    
        if fight_select(msg):
            move_select = True
            print ('What move should Pikachu use?')
            time.sleep(.5)
            out_msg = ''
            time.sleep(.5)
            out_msg = '[Thunderbolt] [Tackle]'
            battle = True   

        # Check for a thunderbolt msg  
        thundermove = use_thunderbolt(msg)
        """Activated when user inputs 'thunderbolt' """
        
        if thundermove:   
            print ('Pikachu used Thunderbolt')
            time.sleep(1.5)            
            print (random.choice(DAMAGE_OUT))
            charmanderHP = charmanderHP - 13
            time.sleep(1.5)
            
            """Checks if opponent has fainted"""
            
            if charmanderHP <= 0:
                print ('The wild Charmander fainted!')
                time.sleep(1)
                print("Pikachu gained " + str(random.choice(EXP)) + " Exp. points") 
                Battle = False
                break
                
            else:
                None
                
            time.sleep(1.7)            
            opp_move = 'The wild Charmander used ' + random.choice(WILD_MOVES) +'!'
            print(opp_move)
            time.sleep(1.5)
            
            if "Ember" in opp_move:
                pikachuHP = pikachuHP - 11
                print('Pikachu lost 11 HP!')
                pika_status = 'Pikachu now has ' + str(pikachuHP) + ' HP!'
                print(pika_status)
                time.sleep(1.5)
                
            if "Scratch" in opp_move:
                pikachuHP = pikachuHP - 7
                print('Pikachu lost 7 HP!')
                pika_status = pika_status = 'Pikachu now has ' + str(pikachuHP) + ' HP!'
                print (pika_status)
                time.sleep(1.5)
            
            else:
                
                None
            
            if pikachuHP <= 0:
                print ('Your Pikachu has fainted!')
                time.sleep(.5)
                print ('You are out of usable pokemon')
                time.sleep(1.5)
                print ('... ... ... ...')
                time.sleep(1.5)
                print ('You blacked out and lost ₽126')
                Battle = False
                break
                
            else:
                battle = True
                
                print ('')
                print ("What will Pikachu do?")
                time.sleep(1.5)
                out_msg = '[Fight] [Run] [Pokemon]'

        # Check for a tackle msg
        if use_tackle(msg):
            print ('Pikachu used Tackle')
            time.sleep(1.5)
            print (random.choice(DAMAGE_OUT))
            charmanderHP = charmanderHP - 5
            time.sleep(1.5)
       
            if charmanderHP <= 0:
                print ('The wild Charmander fainted!')
                time.sleep(1)
                print("Pikachu gained " + str(random.choice(EXP)) + " Exp. points")  
                Battle = False
                break
                
            else:
                None
                
            time.sleep(1.7)
            
            opp_move = 'The wild Charmander used ' + random.choice(WILD_MOVES) +'!'
            print(opp_move)
            
            time.sleep(1.5)
            
            if "Ember" in opp_move:
                pikachuHP = pikachuHP - 11
                print('Pikachu lost 11 HP!')
                pika_status = 'Pikachu now has ' + str(pikachuHP) + ' HP!'
                print(pika_status)
                time.sleep(1.5)
                
            if "Scratch" in opp_move:
                pikachuHP = pikachuHP - 7
                print('Pikachu lost 7 HP!')
                pika_status = pika_status = 'Pikachu now has ' + str(pikachuHP) + ' HP!'
                print (pika_status)
                time.sleep(1.5)
            else:
                None
            
            
            if pikachuHP <= 0:
        
                print ('Your Pikachu has fainted!')
                time.sleep(1)
                print ('You are out of usable pokemon')
                time.sleep(1.5)
                print ('... ... ... ...')
                time.sleep(1.5)
                print ('You blacked out and lost ₽126')
                Battle = False
                break
                
            else:
                
                battle = True
                
                print ('')
                print ("What will Pikachu do?")
                time.sleep(1.5)
                out_msg = '[Fight] [Run] [Pokemon]'

        # If the input was pokemon, return msg showing available pokemon
        if not out_msg and pokemonset:
            out_msg = POKEMONSELECT

        # If we don't recognize the input then,
        # we will output a string that basically says the input was not understood
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print(out_msg)
        
# Run all cells above before running this cell
have_a_battle()