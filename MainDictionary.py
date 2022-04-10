# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:47:53 2021

@author: bhatt

This is the dictionary version 4. This utilizes external functions to execute tasks. 

"""
from DictionaryCommand import *

fname = "New_Dictionary.txt"
fname_2 = "Dict_hist.txt"

# Read the create a dictionary. 
sushi_dict = read_dict(fname)

# Master loop
while True:

    ans = input('''What would you like to do? 
                
                Add    (A)
                Edit   (E)
                Search (S)
                Learn  (L)
                Rapid  (R)
                Quit   (Q)
                
    Enter: ''').lower().lstrip().rstrip()
    
    # Ensure a valid option in entered
    while True:
    
        if ans in ["a", "e", "s", "l","r", "q"]:
            break
        else:
            ans = input("Invalid option. Try again. :").lower().lstrip().rstrip()
    
    if ans == "s":
        
        while True:
            wrd = input("Enter a word: ").lower().lstrip().rstrip().capitalize()
            if wrd in sushi_dict:
                print_word(wrd,sushi_dict)
            else: 
                print("\n***Word not found. Try again or considering adding it.")
            
            # keep going with search?
            kgs_ans = input("Search another word? (Y/N): ").lower().lstrip().rstrip()
            if kgs_ans == 'n':
                break
            else:
                pass
        
    elif ans == "a":
        
        while True:
            word_list = add_word(sushi_dict)
            
            if word_list == None:
                pass
            else:
                # Add to dict.
                sushi_dict[word_list[0]] = {'pos':word_list[1],'def':word_list[2], 'ex':word_list[3]}
            
                # Write to dict .txt file.
                write_word(word_list[0], word_list[1], word_list[2], word_list[3], fname)
                print("\nWord Added!\n")
        
            # keep going with add?
            kgd_ans = input("Add another word? (Y/N): ").lower().lstrip().rstrip()
            if kgd_ans == 'n':
                break
            else:
                pass
            
    elif ans == "e":
        print("E")
        
        # Input word to edit
        wte = input("Enter a word to edit: " ).lower().lstrip().rstrip().capitalize()
        
        if wte in sushi_dict:
            
            print("\nHere is the exisiting information.")
            print_word(wte, sushi_dict)
            print("\nEnter the new information below to update the word.")
            edit_word(wte, sushi_dict)
            print("The word has been updated.")
            
            # Update the dictionary text file. Rewrite it. 
            file_rewrite = open(fname,'w')
            for key in sushi_dict:
                
                write_word(key, sushi_dict[key]["pos"], sushi_dict[key]["def"], sushi_dict[key]["ex"], fname)
            
            print("The dictionary has been updated.")
            file_rewrite.close()
            
        else:
            print("The word doesn't exists in the dictionary. ")
        
    elif ans == "l":
        learn_words(fname_2, sushi_dict)
        
    elif ans == "r":
        
        print("\n Rapid Quiz Time!!")
        
        already_displayed = []
        keep_searching = True
        end_dict = False
        already_listed_counter = 0
        
        # main loop
        while True: 
            
            # keep generating until unique word is gnerated. loop 2. 
            while True:
                # get word to display
                wtd = rapid_learn(sushi_dict)
            
                if wtd in already_displayed:
                    already_listed_counter += 1 
                    
                    if already_listed_counter == len(sushi_dict):
                        print("\n You've reached the end of this dictionary! Good job!")
                        end_dict = True
                        
                else:
                    # reset it for next loop
                    already_listed_counter = 0
                    break # loop 2
            
            if end_dict:
                break # main loop
            else:
                print(f"\n Word: {wtd}\n")
            
                if terminal_timer(5):
                   temp =  input("\n Another word? (Y/N): ").lower().lstrip().rstrip()
                   
                   # Get a definitive yes or no
                   if temp != 'y' and temp != 'n':
                       while True:
                           ans = input("Try Again! (Y/N):").lower().lstrip().rstrip()
                           if ans == 'y' or ans == 'n':
                               temp = ans
                               break
                   
                   if temp == 'n':
                        break  # main loop
                        
                already_displayed.append(wtd)
        
        print("\nSee ya next time!")
        break  # master loop 
    
        
    else:
        print("\nSee ya later!")
        break
