# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:40:46 2021

@author: bhatt

This files containts the functions that can read, search, and print from the dictionary. 
"""
import random
import time
import sys

def read_dict(fname):
    '''This functions reads the existing dictionary text file and creates and python dictionary to be used later.
    '''
    
    # Open the exisiting file.  
    file1 = open(fname,'r')
    sushi_dict = {}
    
    col_count = 0
    for line_num, line in enumerate(file1):
        
        # Extract the word and the meanings
        if ':' in line:
           
            if col_count == 0:
                def_list = []
                eg_list = []
            
            line_break = line.split(":")
            
            # Extract the word
            if "[" in line:
                left = line_break[0].split(" ")
                word = left[0]
                pos = left[1].lstrip().rstrip()
                mean = line_break[1].lstrip().rstrip().capitalize()
            else:
                mean = line_break[1].lstrip().rstrip().capitalize()
            
            def_list.append(mean)
            col_count += 1
        
        # Extract the examples
        if "/" in line:
            example_break = line.split("//")
            example = example_break[1].lstrip().rstrip().capitalize()
            
            if "\\" in example_break[1]:
                example_break2 = example_break[1].split("\\\\")
                example = example_break2[0].lstrip().rstrip().capitalize()
                                     
            eg_list.append(example)
            
        # after line break, package the words, ex, and mean to the dict. 
        if "\\" in line:
            
            def_temp = def_list
            eg_temp = eg_list
            sushi_dict[word] = {'pos':pos,'def':def_temp, 'ex': eg_temp}
            
            # clear for next word
            word = None
            def_list = []
            eg_list = []
            col_count = 0
        
    file1.close()
    
    return sushi_dict
# =============================================================================

def print_word(vocab, sushi_dict):
    '''This functions simply prints the definition, meanings, and examples in the console.
    '''
    
    word_dict = sushi_dict[vocab.lstrip().rstrip().capitalize()]
    print("\n")
    print(vocab  + " " + word_dict["pos"] + ": " + word_dict["def"][0])

    # def the tab spacing
    space = len(vocab + " " + word_dict["pos"])

    # print additional definition
    for definition in word_dict["def"][1:]:
        print(" "*space + ": " + definition)

    # No need for \n bc end of def has \n
    print(" ")

    # print example sentences
    for sentence in word_dict["ex"]:
        print(" "*space + "// " + sentence)

# =============================================================================

def add_word(current_dict):
    '''This functions accepts the words, meanings, and examples from the user interactively and returns a list.
    '''
    
    # sushi_dict = {}
    def_list = []
    eg_list = []
    
    new_wrd = input("Enter a word: ").lstrip().rstrip().lower().capitalize()
    if new_wrd in current_dict:
        print("\nThe word already exists.")
        return None
    else:
        
        pos = "[" + input("Enter the word's class: ").lstrip().rstrip() + "]"
        
        mean1 = input("Enter the definition: ").lstrip().rstrip()
        
        # Add period at the end
        if mean1[-1] != '.':
            mean1 = mean1 + "."
        
        def_list.append(mean1)
        
        more_def = input("Are there more definitions? (Y/N): ")
        
        # Get a definitive yes or noa
        if more_def != 'y' and more_def != 'n':
            while True:
                ans = input("Try Again! (Y/N):").lower().lstrip().rstrip()
                if ans == 'y' or ans == 'n':
                    more_def = ans
                    break
        
        if more_def.lower() == 'n':
            pass
        else: 
            while True:
                temp = input("Add another definition ('Q' to quit): ").lstrip().rstrip()
                if temp.lower() == 'q':
                    break
                else:
                    if temp[-1] != '.':
                        temp = temp + "."
                    def_list.append(temp)
        
        ex1 = input("Enter an example sentence: ").lstrip().rstrip()
        
        # Add period at the end
        if ex1[-1] != '.':
            ex1 = ex1 + "."
        
        eg_list.append(ex1)
        
        more_ex = input("Do you want to add more example sentences? (Y/N): ")
        
        # Get a definitive yes or no
        if more_ex != 'y' and more_ex != 'n':
            while True:
                ans2 = input("Try Again! (Y/N):").lower().lstrip().rstrip()
                if ans2 == 'y' or ans2 == 'n':
                    more_ex = ans2
                    break
        
        if more_ex.lower() == 'n':
            pass
        else: 
            while True:
                temp2 = input("Add another example ('Q' to quit): ").lstrip().rstrip()
                if temp2.lower() == 'q':
                    break
                else:
                    if temp2[-1] != '.':
                        temp2 = temp2 + "."
                    eg_list.append(temp2)
    
        def_temp = def_list
        eg_temp = eg_list
    
        # sushi_dict[new_wrd] = {'pos':pos,'def':def_temp, 'ex': eg_temp}
        return [new_wrd, pos, def_temp, eg_temp]

# =============================================================================

def write_word(wrd,pos,mean,ex,fname):
    '''This fucntions write the supplied arugments to the supplied .txt file.
    '''
    
    f = open(fname,'a')
    
    # Write first line
    f.write("\n" + wrd + " " + pos + ": " + mean[0] )
    
    # def the tab spacing
    space = len(wrd + " " + pos)

    # print additional definition
    for definition in mean[1:]:
        f.write("\n" + " "*space + ": " + definition)

    # print example sentences
    for sentence in ex:
        f.write("\n" + " "*space + "// " + sentence)
        
    # Add close out symbol
    f.write(" \\\\")
    f.write("\n")
    
    f.close()
    
# =============================================================================

def learn_words(fname, sushi_dict):
    '''A game to learn new words. This can be a stand alone code if needed. 
    '''
    import random
    
    # Open the history file.  
    file1 = open(fname,'a')   

    ans = input("Would you like to generate a random word? (y/n): ")
    # prompt for a random word
    while ans == 'y':

        if ans.lower() == 'y':
            
            # Generate random word
            wrd, meaning = random.choice(list(sushi_dict.items()))

            print("\nWord: " + wrd)
            ans1 = input("Do you know the meaning? (y/n): ")
            
            if ans1.lower() == "y":
                print("\nUse the word in a sentence and type below: ")
                ans2 = input("Enter sentence: ")
                
                file1.write(wrd + ":= " + ans2 + "\n")

                print('\nSaved. Here is what it means!')
                print_word(wrd, sushi_dict)
                      
            else:
                resp = input("Do you want to know the meaning? (y/n): ")
                if resp.lower() == 'y':
                    print_word(wrd, sushi_dict)
                    
                    print("\nUse the word in a sentence and type below: ")
                    ans2 = input("Enter sentence: ")
                    file1.write(wrd + ":= " + ans2 + "\n")
                    print('\nSaved.')
            
                else:
                    print("So long!")        
        else:
            pass

        ans  = input("Another random word? (y/n): ")
        if ans.lower() == "n":
            print("So Long!")
            
    file1.close()
    
# =============================================================================

def edit_word(wte, sushi_dict):
    '''This functions accepts the word and using that key it updates the values in the dictionary by accepting the inputs from the user. It uses the property that dictionary only have one unique keys.
    
    It's basically the same fucntion as add_word.
    '''
    def_list = []
    eg_list = []
    
    pos = "[" + input("Enter the word's class: ").lstrip().rstrip() + "]"
    
    mean1 = input("Enter the definition: ").lstrip().rstrip()
    
    # Add period at the end
    if mean1[-1] != '.':
        mean1 = mean1 + "."
    
    def_list.append(mean1)
    
    more_def = input("Are there more definitions? (Y/N): ")
    
    # Get a definitive yes or no
    if more_def != 'y' and more_def != 'n':
        while True:
            ans = input("Try Again! (Y/N):").lower().lstrip().rstrip()
            if ans == 'y' or ans == 'n':
                more_def = ans
                break
    
    if more_def.lower() == 'n':
        pass
    else: 
        while True:
            temp = input("Add another definition ('Q' to quit): ").lstrip().rstrip()
            if temp.lower() == 'q':
                break
            else:
                if temp[-1] != '.':
                    temp = temp + "."
                def_list.append(temp)
    
    ex1 = input("Enter an example sentence: ").lstrip().rstrip()
    
    # Add period at the end
    if ex1[-1] != '.':
        ex1 = ex1 + "."
    
    eg_list.append(ex1)
    
    more_ex = input("Do you want to add more example sentences? (Y/N): ")
    
    # Get a definitive yes or no
    if more_ex != 'y' and more_ex != 'n':
        while True:
            ans2 = input("Try Again! (Y/N):").lower().lstrip().rstrip()
            if ans2 == 'y' or ans2 == 'n':
                more_ex = ans2
                break
    
    if more_ex.lower() == 'n':
        pass
    else: 
        while True:
            temp2 = input("Add another example ('Q' to quit): ").lstrip().rstrip()
            if temp2.lower() == 'q':
                break
            else:
                if temp2[-1] != '.':
                    temp2 = temp2 + "."
                eg_list.append(temp2)
    
    def_temp = def_list
    eg_temp = eg_list
    
    # update the values. 
    sushi_dict[wte] = {'pos':pos,'def':def_temp, 'ex': eg_temp}

# =============================================================================

def rapid_learn(sushi_dict):
    '''
    Prints out provides random word from the dictionary.

    '''
    return random.choice(list(sushi_dict.keys()))

# =============================================================================
# Terminal Timer

def terminal_timer(t):
    
    for remaining in range(t, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)
    
    sys.stdout.write("\rTimes up!            \n")
    return True

# =============================================================================



