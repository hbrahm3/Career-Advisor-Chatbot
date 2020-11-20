# CS 421: Natural Language Processing
# University of Illinois at Chicago
# Fall 2020
# Chatbot Project - Chatbot Evaluation
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully.
# Code Attribution: Used Professor Natalie Parde's (UIC) example code as a starter for the chatbot structure
# =========================================================================================================

# Import any necessary libraries here, but check with the course staff before requiring any external
# libraries.
from collections import defaultdict
import random
import re

dst = defaultdict(list)

# update_dst(input): Updates the dialogue state tracker
# Input: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is
#        most appropriate for the corresponding slot.  Defaults to an empty list.
# Returns: Nothing
def update_dst(input=[]):

    global dst # using the global dialogue state tracker
    
    for x, y in input:
        if type(x) != str: # Error Check: If our arguments aren't string type, then we reject that
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
Slot: empathy Permissible Values: String ("yes" or "no")
Slot: result Permissible Values: list ("Healthcare Professional", "Law Enforcement Officer", "Educator", "Social Worker", "Financial Advisor", "Gourmet Chef", "Scientific Researcher", "Nutritionist", "Cosmotologist", "Computer Scientist", "Marketing Specialist", "Engineer", "Accountant", "Graphic Designer", "Nutritionist", "Film Director", "Politician", )
Slot: dialogue_state_history Permissible Values: list ("greeting", "social_interaction", "intro_extroversion", "term_clarify", "right_leftbrain", "academ_pref", "likes_history", "job_function", "imagine_analyze", "innovate", "empathy", "result", "farewell")
Slot: user_intent_history Permissible Values: list ("greeting", "ans_soc_inter", "ans_introextro", "clarify", "ans_rlbrain", "ans_academ", "ans_hist", "ans_jobfunc", "ans_imag_analyze", "ans_innovate", "ans_empathy", "ack_result", "farewell")
"""

# Function to get a career based on the user's responses
#
# No arguments for input
#
# Returns one of the possible career values as a string
def get_career():
    global dst
    
    social = dst["social_interaction"]
    intro_extro = dst["intro_extroversion"]
    brain = dst["right_leftbrain"]
    fav_subject = dst["academ_pref"]
    history = dst["likes_history"]
    job_type = dst["job_function"]
    analysis = dst["imagine_analyze"]
    innovate = dst["innovate"]
    empathy = dst["empathy"]
    
    career_poss = []
    
    if social == "different people" and intro_extro == "extrovert" and fav_subject == "science" and empathy == "yes" and job_type == "hands-on":
        career_poss.append("Healthcare Professional")
        
    if social == "different people" and intro_extro == "extrovert" and empathy == "yes" and job_type == "hands-on":
        career_poss.append("Law Enforcement Officer")
        career_poss.append("Teacher")
        career_poss.append("Educator")
        
    if brain == "left brain" and job_type == "hands-on" and history == "yes" and empathy == "yes":
        career_poss.append("Archeologist")
        career_poss.append("Historian")
        
    if fav_subject == "art" and job_type == "hands-on" and innovate == "creative" and social == "familiar group":
        career_poss.append("Gourmet Chef")
        career_poss.append("Graphic Designer")
        
    if social == "familiar group" and brain == "left brain" and fav_subject == "math" and innovate == "traditional" and analysis == "yes":
        career_poss.append("Financial Advisor")
        career_poss.append("Data Manager")
    
    if intro_extro == "introvert" and job_type == "theoretical" and (fav_subject == "math" or fav_subject == "science") and social == "familiar group":
        career_poss.append("Scientific Researcher")
        
    if brain == "right brain" and intro_extro == "extrovert" and empathy == "yes" and history == "no":
        career_poss.append("Nutritionist")
        
    if (fav_subject == "english" or fav_subject == "art") and social == "different people" and innovate == "creative":
        career_poss.append("Cosmetologist")
    
    if analysis == "yes" and innovate == "creative" and intro_extro == "introvert":
        career_poss.append("Computer Scientist")
        career_poss.append("Software Engineer")
        
    if social == "different people" and intro_extro == "extrovert" and job_type == "hands-on":
        career_poss.append("Marketing Specialist")
        
    if (fav_subject == "math" or fav_subject == "science") and job_type == "hands-on" and innovate == "creative":
        career_poss.append("Engineer")
        
    if fav_subject == "math" and social == "familiar group":
        career_poss.append("Accountant")
        
    if fav_subject == "art" and brain == "right brain" and social == "familiar group":
        career_poss.append("Art Director")
    
    if fav_subject == "art" and innovate == "creative" and job_type == "hands-on":
        career_poss.append("Film Director")
        
    if social == "different people" and empathy == "yes":
        career_poss.append("Social Worker")
        
    if history == "yes":
        career_poss.append("Historian")
        
    career_poss.append("Politician")
    
    #print(career_poss)
    
    pick_career = random.choice(career_poss)
    
    return pick_career


# dialogue_policy(dst): Selects the next dialogue state to be uttered by the chatbot.
# Input: A dictionary representation of a full dialogue state.
# Returns: A string value corresponding to a dialogue state, and a list of (slot, value) pairs necessary
#          for generating an utterance for that dialogue state (or an empty list of no (slot, value) pairs
#          are needed).
def dialogue_policy(dst=[]):

    # If the user has asked for clarification on the introversion/extroversion term, then provide that explanation
    next_state = "greeting"
    slot_values = []

    if dst["user_intent_history"]:
        if dst["user_intent_history"][-1] == "clarify": # if latest value is user asking for clarification
            next_state = "term_clarify" # we will aim to clarify the term in this next state
            slot_values = []
            
        if dst["user_intent_history"][-1] == "greeting": # Greeting -> Social Interaction
            slot_values = [("greeting", dst["greeting"])]
            if dst["greeting"] == "no":
                print("Ok, thank you for your time. Hopefully we'll see you next time. Bye for now!")
                exit(0)
            next_state = "social_interaction"
            
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
            career = get_career()
            update_dst([("result", career)])
            slot_values = [("result",dst["result"])] # dst["result"] should have a career when we get here... Make a new Function that takes responses and translates them into a career
        
        if dst["user_intent_history"][-1] == "ack_result": # Results -> Farewell
            next_state = "farewell"
            slot_values = [("result",dst["result"])] # return slot value to wish them good luck on the career path
    
    return next_state, slot_values
    
def get_template_res(state, slots=[]):

    if state == "result" or state == "farewell":
        slot, value = slots[0] # take the first slot and separate into slot, value. It'll be the slot="result" and the value = the recommended career
    templates = defaultdict(list)
    
    # The templates for the greeting state
    templates["greeting"] = []
    templates["greeting"].append("Hi! Welcome to 421CareerCounselor. Would you like to answer some questions to find out what career path would be a good fit for you?")
    templates["greeting"].append("Welcome to 421CareerCounselor. Do you want to find out what would be a good career for you by answering a few quick questions?")
    
    # Templates for the social interaction state. A part of this is acknoledging that the user said yes ot taking the survey/quiz for a career recommendation.
    templates["social_interaction"] = []
    templates["social_interaction"].append("Great, let's Begin! Would you prefer a workplace where you interact with many different people every day or are you more comfortable with a familiar group you work with on a daily basis?")
    templates["social_interaction"].append("Wonderful, let's get started! Do you prefer a job where you get to meet new people every day, or do you like to stick to a familiar group of coworkers?")
    
    # Templates for the introversion extroversion state
    templates["intro_extroversion"] = []
    templates["intro_extroversion"].append("Would you consider yourself an introvert or an extrovert?")
    templates["intro_extroversion"].append("Would you say you are more of an introvert or extrovert?")
    
    # Templates for the state where we clarify if the user doesn't know what "introvert" or "extrovert" means
    templates["term_clarify"] = []
    templates["term_clarify"].append("An introvert is someone who is often quiet, shy, reserved, and introspective. On the other hand, an extrovert is someone who is often outgoing, social, lively and talkative. Which one sounds more like you?")
    templates["term_clarify"].append("An introvert is more often the quiet observer in a group conversation. But if you're the life of the party... You're more of an extrovert! So which one sounds more like you?")
    
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
    templates["imagine_analyze"].append("Are you good at taking current circumstances and visualizing how they influence the future?")
    
    # Template for the innovation state
    templates["innovate"] = []
    templates["innovate"].append("Do you prefer to stick to a tried and tested method, or do you constantly look for new and efficient ways to do old tasks?")
    templates["innovate"].append("Do you tend to stick to a traditional method of doing things, or are you usually innovative?")
    
    # Templates for the empathy state
    templates["empathy"] = []
    templates["empathy"].append("Do you find it easy to empathize with people’s personal problems and try to help them?")
    templates["empathy"].append("If you see someone in a difficult situation, do you try to take the time to help them?")
    
    # Templates for the results. This takes in a value of career recommendation
    if state == "result" or state == "farewell":
        templates["result"] = []
        article = ""
        regex_vowel = "^[AEIOU][a-zA-z]*"
        if (re.search(regex_vowel, value)):
            article = "an"
        else:
            article = "a"
        
        templates["result"].append("Based on your responses, it seems that a career as {0} {1} would be a great fit for you.".format(article,value))
        templates["result"].append("Based on your interests and personality, you should look into being a {0} as a possible career for you.".format(value))
        
        # Templates for farewell. Once again potentially takes in the value of a career.
        templates["farewell"] = []
        templates["farewell"].append("Thank you for your time today, and I hope you have a great day! Good luck on your journey as {0} {1}!".format(article, value))
        templates["farewell"].append("Hopefully, you'll look into being {0} {1} as a potential career! We wish you the best of luck!".format(article, value))
    
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


# nlu(input): Interprets a natural language input and identifies relevant slots and their values
# Input: A string of text.
# Returns: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is most
#          appropriate for the corresponding slot.  If no slot values are extracted, the function should
#          return an empty list.
def nlu(input=""):
    global dst
    
    slots_and_values = []
    
    # To narrow the set of expected slots, you may (optionally) first want to determine the user's intent,
    # based on what the chatbot said most recently. We have a case for each dialouge state
    user_intent = ""
    if "dialogue_state_history" in dst:
        if dst["dialogue_state_history"][-1] == "greeting":
            # Check to see if the input contains a valid response to greeting.
            pattern = re.compile(r"\b([Yy]es)|([Nn]o(pe)?)|([Ss]ure)|([Yy]eah)|([Oo][Kk](ay)?)|([Nn]ah)|([Yy]up)\b") # checks if input has yes or no in it
            match = re.search(pattern, input)
            if match:
                user_intent = "greeting" # if user says yes, we can start
                slots_and_values.append(("user_intent_history", "greeting"))
                
        if dst["dialogue_state_history"][-1] == "social_interaction":
            # Check to see if the input contains an answer to whether they like same group every day or meeting new people.
            pattern = re.compile(r"\b([Dd]ifferent)|([Ss]ame)|([Nn]ew)|([Ff]amiliar)|([Ss]mall)|([Mm]any)|([Ff]ew)\b") # making sure user is answering question
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_soc_inter"
                slots_and_values.append(("user_intent_history", "ans_soc_inter"))
                
        if dst["dialogue_state_history"][-1] == "intro_extroversion":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"\b(intr[ao]vert)|(extr[oa]vert)|([Ww]hat)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_introextro"
                slots_and_values.append(("user_intent_history", "ans_introextro"))
                
        if dst["dialogue_state_history"][-1] == "term_clarify":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"\b(intr[ao]vert)|(extr[oa]vert)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_introextro"
                slots_and_values.append(("user_intent_history", "ans_introextro"))
                
        if dst["dialogue_state_history"][-1] == "right_leftbrain":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"plan|math|analyz|method|instinct|(\bin the moment\b)|heart|head")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_rlbrain"
                slots_and_values.append(("user_intent_history", "ans_rlbrain"))
                
        if dst["dialogue_state_history"][-1] == "academ_pref":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"\b([Mm]ath)|([Ee]nglish)|([Ss]cience)|([Aa]rt)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_academ"
                slots_and_values.append(("user_intent_history", "ans_academ"))
                
        if dst["dialogue_state_history"][-1] == "likes_history":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"\b(history)|(historical)|(old)|(new)|(current)|(news)|([Yy]es)|([Nn]o)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_hist"
                slots_and_values.append(("user_intent_history", "ans_hist"))
                
        if dst["dialogue_state_history"][-1] == "job_function":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"hands|behind|theor")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_jobfunc"
                slots_and_values.append(("user_intent_history", "ans_jobfunc"))
                
        if dst["dialogue_state_history"][-1] == "imagine_analyze":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"\b([Yy]es)|([Nn]o)|([Nn]ot)|([Yy]eah)\b") # checks if input has yes or no in it
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_imag_analyze"
                slots_and_values.append(("user_intent_history", "ans_imag_analyze"))
                
        if dst["dialogue_state_history"][-1] == "innovate":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"old|tried|tested|known|traditional|new|innovat|creat|efficient|proven")
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_innovate"
                slots_and_values.append(("user_intent_history", "ans_innovate"))
                
        if dst["dialogue_state_history"][-1] == "empathy":
            # Check to see if the input contains a valid answer.
            pattern = re.compile(r"\b([Yy]es)|([Nn]o)|([Nn]ot)|([Yy]eah)|([Yy]up)\b") # checks if input has yes or no in it
            match = re.search(pattern, input)
            if match:
                user_intent = "ans_empathy"
                slots_and_values.append(("user_intent_history", "ans_empathy"))
                
        if dst["dialogue_state_history"][-1] == "result":
            # Check to see if the input contains a valid answer.
            if input:
                user_intent = "ack_result"
                slots_and_values.append(("user_intent_history", "ack_result"))
    else:
        user_intent = "unknown" # otherwise, the user's intent is unknown it'll repeat the question
        
    # Then, based on what type of user intent we think the user had, we can determine which slot values to try to extract.
    if user_intent == "greeting":
        pattern = re.compile(r"\b([Yy]es)|([Ss]ure)|([Yy]eah)|([Oo][Kk](ay)?)|([Yy]up)\b")
        is_yes = re.search(pattern, input)
        
        pattern = re.compile(r"\b([Nn]o(pe)?)|([Nn]ah)\b")
        is_no = re.search(pattern, input)
        
        if is_yes:
            slots_and_values.append(("greeting","yes"))
        elif is_no:
            slots_and_values.append(("greeting","no"))
            
    # Parsing for the social interaction answer
    if user_intent == "ans_soc_inter":
        pattern = re.compile(r"\b([Dd]ifferent)|([Nn]ew)|([Mm]any)\b") # likes to interact with new people -probably good for service sector
        diff = re.search(pattern, input)
        
        pattern = re.compile(r"\b([Ss]ame)|([Ff]amiliar)|([Ss]mall)|([Ff]ew)\b") # prefers to stick to familiar group of people
        same = re.search(pattern, input)
        
        if diff:
            slots_and_values.append(("social_interaction", "different people"))
        elif same:
            slots_and_values.append(("social_interaction", "familiar group"))
    
    # Parsing for the introverted v extroverted personality answer
    if user_intent == "ans_introextro":
        pattern = re.compile(r"\bintr[ao]vert\b")
        intro = re.search(pattern, input)
        
        pattern = re.compile(r"\bextr[oa]vert\b")
        extro = re.search(pattern, input)
        
        pattern = re.compile(r"[Ww]hat") # indicates that the user asked a question about the terms presumably
        clarify = re.search(pattern, input)
        
        if clarify:
            slots_and_values.append(("intro_extroversion", "clarify")) # This leads to state where system can clarify what those terms mean
            slots_and_values.append(("user_intent_history","clarify"))
        elif intro:
            slots_and_values.append(("intro_extroversion", "introvert"))
        elif extro:
            slots_and_values.append(("intro_extroversion","extrovert"))
        
    # Parsing for the right v left brain answer
    if user_intent == "ans_rlbrain":
        pattern = re.compile(r"(instinct)|(\bin the moment\b)|heart") # all charcateristics of the right-brain individuals - relevant key words
        rb = re.search(pattern, input)
        
        pattern = re.compile(r"plan|math|analy|method|head") # all charcateristics of the left-brain individuals - relevant key words
        lb = re.search(pattern, input)
        
        if rb:
            slots_and_values.append(("right_leftbrain","right brain"))
        if lb:
            slots_and_values.append(("right_leftbrain","left brain"))
         
    # Parsing for the academic preference answer, pick Math, English, Science, or Art
    if user_intent == "ans_academ":
        pattern = re.compile(r"\b[Mm]ath\b")
        math = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ee]nglish\b")
        english = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ss]cience\b")
        science = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Aa]rt\b")
        art = re.search(pattern, input)
        
        if math:
            slots_and_values.append(("academ_pref","math"))
        elif english:
            slots_and_values.append(("academ_pref","english"))
        elif science:
            slots_and_values.append(("academ_pref","science"))
        elif art:
            slots_and_values.append(("academ_pref","art"))
            
    # Parsing for the history preference answer
    if user_intent == "ans_hist":
        pattern = re.compile(r"\b(history)|(historical)|(old)|([Yy]es)\b") # positive sentiment towards history TODO: Add NLTK negation detection here
        yes = re.search(pattern, input)
        
        pattern = re.compile(r"\b(new)|(current)|(news)|([Nn]o)\b") # prefers current events
        no = re.search(pattern, input)
        
        if yes:
            slots_and_values.append(("likes_history","yes"))
        elif no:
            slots_and_values.append(("likes_history","no"))
        
    # Parsing for the job function answer
    if user_intent == "ans_jobfunc":
        pattern = re.compile(r"hands") # should be enough for hands-on
        h = re.search(pattern, input)
        
        pattern = re.compile(r"behind|theor") # should be enough to indicate they like behind the scenes kind of work.. or low key kind or work
        b = re.search(pattern, input)
        
        if h:
            slots_and_values.append(("job_function","hands-on"))
        elif b:
            slots_and_values.append(("job_function","theoretical")) # just another way to express behind the scenes (nothing high-profile)
        
    # Parsing for the imagination answer
    if user_intent == "ans_imag_analyze":
        pattern = re.compile(r"\b([Yy]es)|([Yy]eah)\b") # checks if input has yes
        y = re.search(pattern, input)
        
        pattern = re.compile(r"\b([Nn]o)|([Nn]ot)\b") # checks if input has no
        n = re.search(pattern, input)
        
        if y:
            slots_and_values.append(("imagine_analyze","yes"))
        elif n:
            slots_and_values.append(("imagine_analyze","no"))
        
    # Parsing for the innovate answer
    if user_intent == "ans_innovate":
        pattern = re.compile(r"old|tried|tested|known|traditional|proven") # words that express that the user prefers traditional way of things
        trad = re.search(pattern, input)
        
        pattern = re.compile(r"new|innovat|creat|efficient") # words that show that user is more creative
        creat = re.search(pattern, input)
        
        if trad:
            slots_and_values.append(("innovate","traditional"))
        elif creat:
            slots_and_values.append(("innovate","creative"))
    
    # Parsing for the answer to empathy question
    if user_intent == "ans_empathy":
        pattern = re.compile(r"\b([Yy]es)|([Yy]eah)|([Yy]up)\b") # checks if input has yes
        y = re.search(pattern, input)
        
        pattern = re.compile(r"\b([Nn]o)|([Nn]ot)\b") # checks if input has no
        n = re.search(pattern, input)
        
        if y:
            slots_and_values.append(("empathy","yes"))
        elif n:
            slots_and_values.append(("empathy","no"))
        
    return slots_and_values # returns the slots_and_values with the additional information to augment to the structure of the chatbot

# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 chatbot.py

def main():
    global dst
    
    update_dst([("dialogue_state_history", "greeting")])
    current_state_tracker = get_dst()
    next_state, slot_values = dialogue_policy(current_state_tracker)
    
    greet = nlg("greeting")
    print(greet)
    
    while next_state != "farewell":
        
        # Accept user's input with Python input() function
        print("\n")
        user_input = input()
        
        # Perform Natural Language Understanding on the user's input
        slots_and_values = nlu(user_input)
        
        # Store the extracted values in the global dialogue state tracker
        update_dst(slots_and_values)
        
        # Get the latest contents of dst in tracker
        current_state_tracker = get_dst()
        
        # Determine which state the chatbot should enter next
        next_state, slot_values = dialogue_policy(current_state_tracker)
        
        # Generate a natural language realization for the specified state (and slot values if needed)
        output = nlg(next_state, slot_values)
        update_dst([("dialogue_state_history", next_state)])
        current_state_tracker = get_dst()
        print("\n")
        # Print output to terminal, or to user interface
        print(output)
        
        #print(current_state_tracker)

################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()
