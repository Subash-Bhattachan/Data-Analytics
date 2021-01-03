# Project 3
# Subash Bhattachan
# Program that processes data files using lists and tuples
# November 14, 2016



while True:
    print("Hi there! Do you want to know more about Major League Baseball of 2013?" 
          "\n" + "Just enter 'y' for yes or 'n' for no!")
    response = input().lower()
    
    if response in ["y", "n"]:
        break
    else:
        print('That is not a valid option!')

if response == "y":
    print("Okay! Let's start the journey!")
    
    
    # From here the loop repeats again and again except the upper part that executes only once.
    while True: 
        
        print("\n") 
        print("Please type: either 'HELP', 'INPUT', 'TEAM', 'REPORT' or 'QUIT'.") 
        userinput = input().upper()
        
        if userinput in ["HELP", "INPUT", "TEAM", "REPORT", "QUIT"]:
             break
        else:
            print("That is not an option! Try it again please!")

            
    while userinput != "QUIT":
           
  
  
      if userinput == "HELP":
        print("\n", "SO WHAT DO THESE COMMANDS RECOGNIZED BY THIS PROGRAM DO?"
        "\n", "INPUT = This asks for an input file of the user's choice and will avail of any information linked with the file."
        "\n", "TEAM = This asks for a team identifier from the user and will display all the information about all the players in that team."
        "\n", "REPORT = This displays all the information about the top 'n' players in a category of the user's choice."
        "\n", "QUIT = This halts the execution of the program.")
        
        
        print("\n") 
        print("Please type: either 'HELP', 'INPUT', 'TEAM', 'REPORT' or 'QUIT'.") 
        userinput = input().upper()
      
#####################################################################################################  
      elif userinput == "INPUT":


        i = 0            
        while i < 3:
            i += 1
            print()
            print("Please enter a correct input filename that you would like to view." 
                  "\n" + "There are two files: 'mlb.2013.txt' and 'mlb.part.txt'. (You can avoid the file extension.)")
            answer1 = input().lower()
            if answer1 in ["mlb.2013", "mlb.part", "mlb.2013.txt", "mlb.part.txt"]:
                break
            elif i == 3:
              print("You have consecutively exhausted all your three chances! This halts the program now!")             
              break #to halt the program if the input is invalid three consecutive times. 
            else:
              print('That is not a valid option!')


        if answer1 == "mlb.2013" or answer1 == "mlb.2013.txt":
             
            import urllib.request
            link = "http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Baseball/mlb.2013.txt"
            f = urllib.request.urlopen(link)
            myfile = f.read().decode('utf-8')
            print(myfile)
                   
        
        elif answer1 == "mlb.part" or answer1 == "mlb.part.txt":
            import urllib.request
            link = "http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Baseball/mlb.part.txt"
            f = urllib.request.urlopen(link)
            myfile = f.read().decode('utf-8')
            print(myfile)
                      
        
        print("\n") 
        print("Please type: either 'HELP', 'INPUT', 'TEAM', 'REPORT' or 'QUIT'.") 
        userinput = input().upper()
  
#####################################################################################################  

      elif userinput == "TEAM":

        while True:
            print()
            print("Please enter a correct acronym of the team that you would like to view the players from." 
                  "\n" + "These are the teams that you can choose from: 'ARI', 'ATL', 'LAA', 'BAL'"
                  "\n" + "'BOS', 'CHC', 'CIN', 'CLE', 'COL', 'CWS', 'DET', 'HOU', 'KC', 'LAA', 'LAD'"
                  "\n" + "'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SEA', 'SF'"
                  "\n" + "'STL', 'TB', 'TEX', 'TOR', 'WAS'")
            answer2 = input().upper()
            
            if answer2 in ['ARI', 'ATL', 'LAA', 'BAL', 'BOS', 'CHC', 'CIN', 'CLE', 'COL', 'CWS',
                           'DET', 'HOU', 'KC', 'LAA', 'LAD','MIA', 'MIL', 'MIN', 'NYM', 'NYY',
                           'OAK', 'PHI', 'PIT', 'SD', 'SEA', 'SF', 'STL', 'TB', 'TEX', 'TOR', 'WAS']:
                break
            else:
                print('That is not a valid option!')



        if answer2 in ['ARI', 'ATL', 'LAA', 'BAL', 'BOS', 'CHC', 'CIN', 'CLE', 'COL', 'CWS',
                           'DET', 'HOU', 'KC', 'LAA', 'LAD','MIA', 'MIL', 'MIN', 'NYM', 'NYY',
                           'OAK', 'PHI', 'PIT', 'SD', 'SEA', 'SF', 'STL', 'TB', 'TEX', 'TOR', 'WAS']:


            import urllib.request
            link = "http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Baseball/mlb.2013.txt"
            f = urllib.request.urlopen(link)
            myfile = f.read().decode('utf-8')
            lines = myfile.splitlines()

            for line in lines:
                    if answer2 in line:
                        print(line)
            
    
        
        print("\n") 
        print("Please type: either 'HELP', 'INPUT', 'TEAM', 'REPORT' or 'QUIT'.") 
        userinput = input().upper()
        
#####################################################################################################  
      elif userinput == "REPORT":
        
        while True:
            try:
                print("Please enter the top 'n' number of players you want the report for? There are around 687 players altogether.")
                answer3 = int(input())
            except ValueError: 
                print("That is not a valid option!")
            else:    
            
                if answer3 in range(1,688):# this will control the print output
                    break
                else:
                    print("That is not a valid option!")
          
       
          
        
        while True:
            print("Please choose between 'HITS', 'BATTING', or 'SLUGGING'")
            answer4 = input().lower()
          
            if answer4 in ["hits", "batting", "slugging"]:
                break
            else:
              print("That is not a valid option!")
              

          
        if answer4 == "hits":

            import urllib.request
            link = "http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Baseball/mlb.2013.txt"
            f = urllib.request.urlopen(link)
            myfile = f.read().decode('utf-8')
            lines = myfile.splitlines()
                  
           
            scores = []
           
            for line in lines:
                (name, identifier, games, bats, runs, hits, doubles, triples, homeruns) = line.split(";")
               
                scores.append((name, int(hits)))

            scores.sort(key=lambda s: s[1], reverse = True)
            
            for (name, hits) in scores[:answer3]:#write answer3 as cut off number here
                
                    print(name + " : ", hits)

          
        
        elif answer4 == "batting":
           
            import urllib.request
            link = "http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Baseball/mlb.2013.txt"
            f = urllib.request.urlopen(link)
            myfile = f.read().decode('utf-8')
            lines = myfile.splitlines()
                  
           
            scores = []
           
            for line in lines:
                (name, identifier, games, bats, runs, hits, doubles, triples, homeruns) = line.split(";")

                batavg = int(hits)/ int(bats)
                scores.append((name, batavg))

            scores.sort(key=lambda s: s[1], reverse = True)
            
            for (name, batavg) in scores[:answer3]:#write answer3 as cut off number here
                
                    print(name + " : ", "%.3f" % batavg)

         
        
        elif answer4 == "slugging":
          
            import urllib.request
            link = "http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Baseball/mlb.2013.txt"
            f = urllib.request.urlopen(link)
            myfile = f.read().decode('utf-8')
            lines = myfile.splitlines()
                  
           
            scores = []
           
            for line in lines:
                (name, identifier, games, bats, runs, hits, doubles, triples, homeruns) = line.split(";")

                slugperct = (int(hits) + int(doubles) + (2 * int(triples)) + (3 * int(homeruns)))/ int(bats)
                scores.append((name, slugperct))

            scores.sort(key=lambda s: s[1], reverse = True)
            
            for (name, slugperct) in scores[:answer3]:#write answer3 as cut off number here
                
                    print(name + " : ", "%.3f" % slugperct)


      
        print("\n") 
        print("Please type: either 'HELP', 'INPUT', 'TEAM', 'REPORT' or 'QUIT'.") 
        userinput = input().upper()
                
####################################################################################################   

      elif (userinput != "HELP") or (userinput != "INPUT") or (userinput != "TEAM") or (userinput != "REPORT"):    
        print("That is not an option! Try it again please!")
        
        
        print("\n") 
        print("Please type: either 'HELP', 'INPUT', 'TEAM', 'REPORT' or 'QUIT'.") 
        userinput = input().upper()
    
#####################################################################################################  

    else:
       print("\n")
       print("This halts the execution now! Hope you had an insightful time!")
      
else:
    print("Goodbye! Have a good one!")
          



          
                                                  
