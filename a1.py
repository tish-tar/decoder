def decode_message(message_to_read):
    
    #checking length and characters for validity
    
    incorrect_message = ""
    for char in message_to_read:
        if char in ",;." or char.isdigit() or char.isalpha() or char.isspace():
            continue
        else:
            if char not in incorrect_message:
                incorrect_message += char
    big_length = False
    has_incorrect = False
    
    if incorrect_message != "":
        has_incorrect = True
        print("Error, incorrect characters: " + incorrect_message)
    
    
    if len(message_to_read) > 100:
        big_length = True
        print("Error, message is too long.")
        
    if big_length or has_incorrect:
        return False
    
    else:
        final_instructions = get_instructions(message_to_read)
        concise_instructions = make_it_concise(final_instructions)
        print("Instructions: " + final_instructions)
        print("Concise instructions: " + concise_instructions)
        
def get_instructions(message_to_read):
    
    message_to_read = message_to_read.lower()
    has_buzz = False
    
    if "buzz" in message_to_read:
        message_to_read = message_to_read.replace("buzz", "uzz", 1)
        has_buzz = True

    cipher_1 = ""
    
    for j in message_to_read:
        if j == "a":
            cipher_1 = cipher_1 + "\u2191" #up
        if j == "b":
            cipher_1 = cipher_1 + "\u2193" #down
        if j == "c":
            cipher_1 = cipher_1 + "\u2190" #left
        if j == "d":
            cipher_1 = cipher_1 + "\u2192" #right

    #checks for fizz and applies inversion, applies rotation if has_buzz is True             
    if "fizz" in message_to_read:
        cipher_1 = make_string_invert(cipher_1)
        
    if has_buzz:
        cipher_1 = make_string_rotate(cipher_1)
 
    return cipher_1   
    
def make_it_concise(decoded_message):
    up_count = decoded_message.count("\u2191")
    down_count = decoded_message.count("\u2193")
    left_count = decoded_message.count("\u2190")
    right_count = decoded_message.count("\u2192")
    up_down_min = min(up_count, down_count)
    left_right_min = min(left_count, right_count)

    decoded_message = decoded_message.replace("\u2191","",up_down_min)
    decoded_message = decoded_message.replace("\u2193","",up_down_min)
    decoded_message = decoded_message.replace("\u2190","",left_right_min)
    return decoded_message.replace("\u2192","",left_right_min)

#rotating by 90 degrees    
def rotate_arrow(arrow_to_rotate):
    if arrow_to_rotate == "\u2191":
        return "\u2192"
    if arrow_to_rotate == "\u2193":
        return "\u2190"
    if arrow_to_rotate == "\u2190":
        return "\u2191"
    if arrow_to_rotate == "\u2192":
        return "\u2193"
    
def make_string_rotate(cipher_to_rotate):
    rotated_cipher = ""
    for a in cipher_to_rotate:
        rotated_cipher += rotate_arrow(a)
    return rotated_cipher

#inverting up to down, left to right, and vice versa 
def invert_arrow(arrow_to_invert):
    if arrow_to_invert == "\u2191":
        return "\u2193"
    if arrow_to_invert == "\u2193":
        return "\u2191"
    if arrow_to_invert == "\u2190":
        return "\u2192"
    if arrow_to_invert == "\u2192":
        return "\u2190"
    
def make_string_invert(cipher_to_invert):
    inverted_cipher = ""
    for a in cipher_to_invert:
        inverted_cipher += invert_arrow(a)
    return inverted_cipher

# For automatic test, DO NOT REMOVE
in_str = input()
decode_message(in_str)
