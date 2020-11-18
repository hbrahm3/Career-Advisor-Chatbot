# CS 421: Natural Language Processing
# University of Illinois at Chicago
# Fall 2020
# Chatbot Project - Dialogue Manager
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully.
# =========================================================================================================

# Import any necessary libraries here, but check with the course staff before requiring any external
# libraries.
from collections import defaultdict

dst = defaultdict(list)

# update_dst(input): Updates the dialogue state tracker
# Input: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is
#        most appropriate for the corresponding slot.  Defaults to an empty list.
# Returns: Nothing
def update_dst(input=[]):

    global dst # using the global dialogue state tracker
    
    for x, y in input:
        if type(x) != str or type(y) != str: # Error Check: If our arguments aren't string type, then we reject that
            return
        
        if (x == "dialogue_state_history") or (x == "user_intent_history"):
            dst[x].append(y) # add value to the list associated with slot
        else:
            dst[x] = y # add single value to be associated with the slot
        
    return

# get_dst(slot): Retrieves the stored value for the specified slot, or the full dialogue state at the
#                current time if no argument is provided.
# Input: A string value corresponding to a slot name.
# Returns: A dictionary representation of the full dialogue state (if no slot name is provided), or the
#          value corresponding to the specified slot.
def get_dst(slot=""):

    global dst # use the global dialogue state tracker
    if slot == "": # no slot was specified
        return dst
    if slot in dst: # slot in dialogue state tracker was specified
        return dst[slot] # return the value at given slot in dialogue state tracker
    else:
        return "No value at slot {0}".format(slot) # value has yet to be specified

"""
Q1 Written: A list of all permissible slots, and the types of values accepted for the slot.

Slot: greeting Permissible Values: String ("yes" or "no")
Slot: social_interaction Permissible Values: String ("different people" or "familiar group")
Slot: intro_extroversion Permissible Values: String ("introvert" or "extrovert" or "clarify")
Slot: right_leftbrain Permissible Values: String ("right brain" or "left brain")
Slot: academ_pref Permissible Values: String ("math" or "english" or "science" or "art")
Slot: likes_history Permissible Values: String ("yes" or "no")
Slot: job_function Permissible Values: String ("hands-on" or "theoretical")
Slot: imagine_analyze Permissible Values: String ("yes" or "no")
Slot: innovate Permissible Values: String ("traditional" or "creative")
Slot: empathy Permissible Values: String ("very empathetic" or "somewhat empathetic" or "not empathetic")
Slot: result Permissible Values: list ("Healthcare Professional", "Law Enforcement Officer", "Educator", "Social Worker", "Financial Advisor", "Gourmet Chef", "Scientific Researcher", "Nutritionist", "Cosmotologist", "Computer Scientist", "Marketing Specialist", "Engineer", "Accountant", "Graphic Designer", "Nutritionist", "Film Director")
Slot: dialogue_state_history Permissible Values: list ("greeting", "social_interaction", "intro_extroversion", "term_clarify", "right_leftbrain", "academ_pref", "likes_history", "job_function", "imagine_analyze", "innovate", "empathy", "result", "farewell")
Slot: user_intent_history Permissible Values: list ("greeting", "ans_soc_inter", "ans_introextro", "clarify", "ans_rlbrain", "ans_academ", "ans_hist", "ans_jobfunc", "ans_imag_analyze", "ans_innovate", "ans_empathy", "ack_result", "farewell")

"""

# dialogue_policy(dst): Selects the next dialogue state to be uttered by the chatbot.
# Input: A dictionary representation of a full dialogue state.
# Returns: A string value corresponding to a dialogue state, and a list of (slot, value) pairs necessary
#          for generating an utterance for that dialogue state (or an empty list of no (slot, value) pairs
#          are needed).
def dialogue_policy(dst=[]):

    # If the user has asked for clarification on the introversion/extroversion term, then provide that explanation
    next_state = ""
    slot_values = []

    if dst["user_intent_history"]:
        if dst["user_intent_history"][-1] == "clarify": # if latest value is user asking for clarification
            next_state = "term_clarify" # we will aim to clarify the term in this next state
            slot_values = []
            
        if dst["user_intent_history"][-1] == "greeting": # Greeting -> Social Interaction
            next_state = "social_interaction"
            slot_values = [("greeting", dst["greeting"])]
            
        if dst["user_intent_history"][-1] == "ans_soc_inter": # Social Interaction -> Intro/Extroversion
            next_state = "intro_extroversion"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_introextro": # Intro/Extroversion -> Right/Left Brain
            next_state = "right_leftbrain"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_rlbrain": # Right/Left Brain -> Academic Preferences
            next_state = "academ_pref"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_academ": # Academic Preferences -> History
            next_state = "likes_history"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_hist": # History -> Job Function
            next_state = "job_function"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_jobfunc": # Job Function -> Imagination/Analysis
            next_state = "imagine_analyze"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_imag_analyze": # Imagination/Analysis -> Innovation
            next_state = "innovate"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_innovate": # Innovation -> Empathy
            next_state = "empathy"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ans_empathy": # Empathy -> Results
            next_state = "result"
            slot_values = []
        
        if dst["user_intent_history"][-1] == "ack_result": # Results -> Farewell
            next_state = "farewell"
            slot_values = ["result",dst["result"]] # return slot value to wish them good luck on the career path
    
    return next_state, slot_values
        
    


# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 chatbot.py

def main():
    global dst
    
    # Sample Input
#    input = [("num_pizzas", 5), ("pizza_toppings", ["hot peppers", "olives"])]
    
    # Call update_dst(input).  The function should return nothing, but the global dst variable should be
    # updated to:
    # dst["num_pizzas"] = 5
    # dst["pizza_toppings"] = ["hot peppers", "olives"]
#    update_dst(input)
    print("Current Global DST:\n{0}".format(dst))
    
    # List your five test cases for update_dst here:
    print("\n******** update_dst ********")
    test_case_1 = [("social_interaction", "familiar group")]  # update dst at social_interaction

    update_dst(test_case_1)
    print("Global DST - Test Case 1:\n{0}".format(dst))
    
    test_case_2 = [("user_intent_history", "greeting")]  # add the user utterance to history- this also helps guide which state comes next
    update_dst(test_case_2)
    print("\nGlobal DST - Test Case 2:\n{0}".format(dst))
    
    test_case_3 = [("likes_history", "no")]  # update dst
    update_dst(test_case_3)
    print("\nGlobal DST - Test Case 3:\n{0}".format(dst))
    
    test_case_4 = [("innovate", 55)]  # update dst ("innovate", "traditional")
    update_dst(test_case_4)
    print("\nGlobal DST - Test Case 4:\n{0}".format(dst))
    
    test_case_5 = [("academ_pref", "english")]  # update dst
    update_dst(test_case_5)
    print("\nGlobal DST - Test Case 5:\n{0}".format(dst))
    print("****************************")
    
	# Call get_dst().  The function should return a dictionary with keys "num_pizzas" and "pizza_toppings"
    # and values as specified previously.
    current_state_tracker = get_dst()
    print("\nOutput DST:\n{0}".format(current_state_tracker))
    
    # List your five test cases for get_dst here:
    print("\n******** get_dst ********")
    test_case_1 = "likes_history"  # Does user like history?

    value = get_dst(test_case_1)
    print("Output - Test Case 1:\t{0}".format(value))
    
    test_case_2 = "innovate"  # Does user prefer traditional ways or is creative?
    # This should be empty because we gave in an improper format as argument in update_dst. Should return "No value at slot innovate"
    value = get_dst(test_case_2)
    print("Output - Test Case 2:\t{0}".format(value))
    
    test_case_3 = "academ_pref"  # What was user's fav subject?
    value = get_dst(test_case_3)
    print("Output - Test Case 3:\t{0}".format(value))
    
    test_case_4 = "social_interaction"  # User's comfort level with daily new social interactions
    value = get_dst(test_case_4)
    print("Output - Test Case 4:\t{0}".format(value))
    
    test_case_5 = "empathy"  # Does user report being empathetic?
    # This should return "No value at slot empathy" since no value has been added there yet...
    value = get_dst(test_case_5)
    print("Output - Test Case 5:\t{0}".format(value))
    print("*************************")
    
    # Call dialogue_policy(current_state_tracker).  The function should select the next dialogue state,
    # given the information available in current_state_tracker.  Assuming that the function has logic that
    # specifies that a clarification is needed regarding the number of pizzas specified, the function
    # should return two values: "clarification", [("num_pizzas", 5)]
    #next_state, slot_values = dialogue_policy(current_state_tracker)
    
    # Test your demos for dialogue_policy here:
    
    demo1 = defaultdict(list)
    demo1["dialogue_state_history"] = ["greeting"]
    demo1["user_intent_history"] = ["greeting"]
    demo1["greeting"] = "yes"
    # This should return the next state to be: social_interaction and the slot,values should be ("greetings", "yes") to indicate that the user said yes to the system greeting, and the next question to be posed to user is the one about social interaction
    
    
    demo2 = defaultdict(list)
    demo2["dialogue_state_history"] = ["greeting", "social_interaction", "intro_extroversion"]
    demo2["user_intent_history"] = ["greeting", "ans_soc_inter", "clarify"]
    demo2["greeting"] = "yes"
    demo2["social_interaction"] = "familiar group"
    # This should return the next_state to be "term_clarify" since the latest user_intent_history entry indicates that user wants system to clarify the meaning. The system then exlpains intro/extroversion definitions in the term_clarify state. No slot values needed
    
    
    demo3 = defaultdict(list)
    demo3["dialogue_state_history"] = ["greeting", "social_interaction", "intro_extroversion", "term_clarify"]
    demo3["user_intent_history"] = ["greeting", "ans_soc_inter", "clarify", "ans_introextro"]
    demo3["greeting"] = "yes"
    demo3["social_interaction"] = "familiar group"
    demo3["intro_extroversion"] = "extrovert"
    # This should return the next state to be "right_leftbrain" since the user just most recently answered the question about being an introvert/extrovert. Now we can move on to ask about how they prefer to think (left brain vs right brain). No slot values needed
    
    
    demo4 = defaultdict(list)
    demo4["dialogue_state_history"] = ["greeting", "social_interaction", "intro_extroversion", "term_clarify", "right_leftbrain", "academ_pref", "likes_history"]
    demo4["user_intent_history"] = ["greeting", "ans_soc_inter", "clarify", "ans_introextro","ans_introextro", "ans_rlbrain", "ans_academ", "ans_hist"]
    demo4["greeting"] = "yes"
    demo4["social_interaction"] = "familiar group"
    demo4["intro_extroversion"] = "extrovert"
    demo4["right_leftbrain"] = "right brain"
    demo4["academ_pref"] = "art"
    demo4["likes_history"] = "yes"
    # This should return the next state to be "job_function" because since the latest user utterance answered the preference for history, the next step should be for the system to ask about what kind of work the user likes. No slots required for this.
    
    
    demo5 = defaultdict(list)
    demo5["dialogue_state_history"] = ["greeting", "social_interaction", "intro_extroversion", "term_clarify", "right_leftbrain", "academ_pref", "likes_history", "job_function", "imagine_analyze", "innovate", "empathy", "result"]
    demo5["user_intent_history"] = ["greeting", "ans_soc_inter", "clarify", "ans_introextro","ans_introextro", "ans_rlbrain", "ans_academ", "ans_hist", "ans_jobfunc", "ans_imag_analyze", "ans_innovate", "ans_empathy", "ack_result"]
    demo5["greeting"] = "yes"
    demo5["social_interaction"] = "familiar group"
    demo5["intro_extroversion"] = "extrovert"
    demo5["right_leftbrain"] = "right brain"
    demo5["academ_pref"] = "art"
    demo5["likes_history"] = "yes"
    demo5["job_function"] = "theoretical"
    demo5["imagine_analyze"] = "yes"
    demo5["innovate"] = "creative"
    demo5["empathy"] = "somewhat empathetic"
    demo5["result"] = ["Film Director", "Graphic Designer", "Cosmotologist"]
    # This should return the next state to be "farewell" since the user has acknowledged the results (a list of potential careers) produced by the system. At this point, system says bye, and says we hope you look into a career from: [results], and Good luck! This requires the values in the slot dst[result]
    
    print("\n******** dialogue_policy ********")
    next_state, slot_values = dialogue_policy(demo1)
    print("Demo 1 - Next State: {0}\tSlot Values: {1}".format(next_state, slot_values))
    
    next_state, slot_values = dialogue_policy(demo2)
    print("Demo 2 - Next State: {0}\tSlot Values: {1}".format(next_state, slot_values))
    
    next_state, slot_values = dialogue_policy(demo3)
    print("Demo 3 - Next State: {0}\tSlot Values: {1}".format(next_state, slot_values))
    
    next_state, slot_values = dialogue_policy(demo4)
    print("Demo 4 - Next State: {0}\tSlot Values: {1}".format(next_state, slot_values))
    
    next_state, slot_values = dialogue_policy(demo5)
    print("Demo 5 - Next State: {0}\tSlot Values: {1}".format(next_state, slot_values))
    print("*********************************")


################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()
