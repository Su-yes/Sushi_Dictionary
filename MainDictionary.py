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
                Quit   (Q)
                
    Enter: ''').lower().lstrip().rstrip()
    
    # Ensure a valid option in entered
    while True:
    
        if ans in ["a", "e", "s", "l", "q"]:
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
            word_list = add_word()
            
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
        
    else:
        print("See ya later!")
        break
