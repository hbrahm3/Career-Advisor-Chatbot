# CS 421: Natural Language Processing
# University of Illinois at Chicago
# Fall 2020
# Chatbot Project - Natural Language Generation
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
import random

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
    
def get_template_res(state, slots=[]):

    if state == "result" or state == "farewell":
        slot, value = slots[0] # take the first slot and separate into slot, value. It'll be the slot="result" and the value = the recommended career
    templates = defaultdict(list)
    
    # The templates for the greeting state
    templates["greeting"] = []
    templates["greeting"].append("Hi! Welcome to 421CareerConselor. Would you like to answer some questions to find out what career path would be a good fit for you?")
    templates["greeting"].append("Welcome to 421CareerCounselor. Do you want to find out what would be a good career for you by answering a few quick questions?")
    
    # Templates for the social interaction state. A part of this is acknoledging that the user said yes ot taking the survey/quiz for a career recommendation.
    templates["social_interaction"] = []
    templates["social_interaction"].append("Great, let's Begin! Would you prefer a workplace where you interact with many different people every day or are you more comfortable with a familiar group you work with on a daily basis?")
    templates["social_interaction"].append("Wonderful, let's get started! Do you prefer a job where you get to meet new people everyday, or do you like to stick to a familiar group of coworkers?")
    
    # Templates for the introversion extroversion state
    templates["intro_extroversion"] = []
    templates["intro_extroversion"].append("Would you consider yourself an introvert or an extrovert?")
    templates["intro_extroversion"].append("Would you say you are more of an introvert or extrovert?")
    
    # Templates for the state where we clarify if the user doesn't know what "introvert" or "extrovert" means
    templates["term_clarify"] = []
    templates["term_clarify"].append("An introvert is someone who is often quiet, shy, reserved, and introspective. On the other hand, an extrovert is someone who is often outgoing, social, lively and talkative. Which one sounds more like you?")
    templates["term_clarify"].append("If you find yourself listening more in a group converstaion, you're probably an introvert. If you're the life of the party... You're more of an extrovert!")
    
    # Templates for the right brain left brain state
    templates["right_leftbrain"] = []
    templates["right_leftbrain"].append("Do you prefer a planned, mathematical, and methodical approach to life, or do you prefer to live in the moment and take each day as it comes?")
    templates["right_leftbrain"].append("Do you make decisions by analyzing the pros and cons or do you prefer to let your instincts lead in most situations?")
    
    # Templates for the state asking about which subject they like best out of math, english, science and art
    templates["academ_pref"] = []
    templates["academ_pref"].append("If you had to choose a favorite subject in school from Math, English, Science, or Art, which one would you pick?")
    templates["academ_pref"].append("Think back to grade school. If you had to repeat any one of the following, which would it be? Math, English, Science, or Art?")
    
    # Templates for the state asking about user's preference for history
    templates["likes_history"] = []
    templates["likes_history"].append("Do you prefer learning about or exploring the historical aspect of issues, or do you prefer to focus on current events and news?")
    templates["likes_history"].append("Would you consider yourself someone who's passionate about learning history?")
    
    # Template for the job-function state. Hands-on vs. theoretical.
    templates["job_function"] = []
    templates["job_function"].append("Do you prefer hands-on work or more theoretical, behind-the-scenes kind of work?")
    templates["job_function"].append("Do you work best with behind-the-scenes kind of work? Or do you prefer hands-on work?")
    
    # Templates for imagination/analysis state
    templates["imagine_analyze"] = []
    templates["imagine_analyze"].append("Do you find it easy to hypothesize how different actions in the present may yield different scenarios in the future?")
    templates["imagine_analyze"].append("Are you good at taking current cirsumstances and visualizing how they influence the future?")
    
    # Template for the innovation state
    templates["innovate"] = []
    templates["innovate"].append("Do you prefer to stick to a tried and tested method, or do you constantly look for new and efficient ways to do old tasks?")
    templates["innovate"].append("Do you tend to stick to a tradiitonal method of doing things, or are you usually innovative?")
    
    # Templates for the empathy state
    templates["empathy"] = []
    templates["empathy"].append("Do you find it easy to empathize with people’s personal problems and try to help them?")
    templates["empathy"].append("If you see someone in a difficult situation, do you try to take the time to help them?")
    
    # Templates for the results. This takes in a value of career recommendation
    if state == "result" or state == "farewell":
        templates["result"] = []
        templates["result"].append("Based on your responses, a career as a {0} would be a great fit for you.".format(value))
        templates["result"].append("Based on your interests and personality, you should look into being a {0} as a possible career for you.".format(value))
        
        # Templates for farewell. Once again potentially takes in the value of a career.
        templates["farewell"] = []
        templates["farewell"].append("Thank you for your time today, and I hope you have a great day!")
        templates["farewell"].append("Hopefully, you'll look into being a {0} as a potential career! We wish you the best of luck!".format(value))
    
    random_num = random.randrange(0,2) # generates a 0 or 1 randomly to choose which template we want to use for the particular state. Each state only has two different options at this time, so this works for every state, regardless of what it is.
    return templates[state][random_num] # returns the sentence/repsonse at the chosen template for the state.
    
# nlg(state, slots=[]): Generates a surface realization for the specified dialogue act.
# Input: A string indicating a valid state, and optionally a list of (slot, value) tuples.
# Returns: A string representing a sentence generated for the specified state, optionally
#          including the specified slot values if they are needed by the template.
def nlg(state, slots=[]):
    
    """
    This function mainly operates by calling the get_template_res() function that takes the state and slots list to generate a proper response and return that response back to this function.
    """
    output = get_template_res(state, slots) # get the generated output/response
    return output # return the appropriate response to the user


# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 chatbot.py

def main():
    global dst
 
#    # Test Cases
#    output = nlg("greetings")
#    print("Test Case #1: {0}".format(output))
#    # Explanation: This test case works because it successfully returns a natural-sounding greeting when specified.
#
#    output = nlg("clarification", [("num_pizzas", 1)])
#    print("Test Case #2: {0}".format(output))
#    # Explanation: There is room for improvement with this test case.  The output it produces is interpretable,
#    # but it doesn't sound very natural since it uses the phrase "1 pizzas."
    
    # ***** TEST CASES *****
    
    # Test case 1
    output = nlg("greeting", [])
    print("Test Case #1: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates of this state.
    
    # Test case 2
    output = nlg("social_interaction", [])
    print("Test Case #2: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for social interaction
    
    # Test case 3
    output = nlg("intro_extroversion", [])
    print("Test Case #3: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for asking whether the individual is and extrovert or an introvert.
    
    # Test case 4
    output = nlg("term_clarify", [])
    print("Test Case #4: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the clarification state, which is optional, but there just in case the user asks for a definition
    
    # Test case 5
    output = nlg("right_leftbrain", [])
    print("Test Case #5: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the right vs left brain state
    
    # Test case 6
    output = nlg("academ_pref", [])
    print("Test Case #6: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for knowing the user's preferred subject
    
    # Test case 7
    output = nlg("likes_history", [])
    print("Test Case #7: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the History state.
    
    # Test case 8
    output = nlg("job_function", [])
    print("Test Case #8: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the job function preference state.
    
    # Test case 9
    output = nlg("imagine_analyze", [])
    print("Test Case #9: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the imagination/analysis dialogue state.
    
    # Test case 10
    output = nlg("empathy", [])
    print("Test Case #10: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the empathy state
    
    """
    Result possibilities: ("Healthcare Professional", "Law Enforcement Officer", "Educator", "Social Worker", "Financial Advisor", "Gourmet Chef", "Scientific Researcher", "Nutritionist", "Cosmotologist", "Computer Scientist", "Marketing Specialist", "Engineer", "Accountant", "Graphic Designer", "Nutritionist", "Film Director")
    """
    # Test case 11
    output = nlg("result", [("result", "Engineer")])
    print("Test Case #11: {0}".format(output))
    # Explanation: This test case could still use some improvement since it sounds grammatically incorrect to say "a Engineer". I'm looking to add code in the get_template_res() function to take care of this a/an situation.
    
    # Test case 12
    output = nlg("farewell", [("farewell", "Computer Scientist")])
    print("Test Case #12: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the farewell state.
    
    # Test case 13
    output = nlg("result", [("result", "Graphic Designer")])
    print("Test Case #13: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the result state. It gives the user a career recommendation.
    
    # Test case 14
    output = nlg("result", [("result", "Financial Advisor")])
    print("Test Case #14: {0}".format(output))
    # Explanation: This test case works because it returns a natural sounding phrase randomly choosing from the templates for the result state. It gives the user a career recommendation.
    
    # Test case 15
    output = nlg("farewell", [("farewell", "Gourmet Chef")])
    print("Test Case #15: {0}".format(output))
    # Explanation: This test case works well since it produces a natural-sounding farewell for the user. Maybe I can add more templates for this state, but I still have to work on that, since it'd impact the rest of the code for randomly generating a repsonse from 3 options instead of 2.


################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()
    
