#The Data we need to Retireve

#Add our dependencies.
import csv
import os


#Direct Path to file
#assign vairable for the file to load and path     file_ ='foldername/filename'
##file_to_load = 'Election_Analysis/Resources/election_results.csv'

#open the election results as read file
##election_data = open(file_to_load, 'r')
    #unsure if this worked...

#close the file
##election_data.close()

#Edit code to open with WITH, open election results as read file, no need to close.
##with open(file_to_load) as election_data:
    #perform analysis
    ##print(election_data)
        #OUTPUT  <_io.TextIOWrapper name='Election_Analysis/Resources/election_results.csv' mode='r' encoding='cp1252'>



#Indirect Path to OPen File
#assign vairable for the file to load and path NOTE had to add Election_Analysis to path
file_to_load = os.path.join("Election_Analysis","Resources", "election_results.csv")

#open the election results as read file
##with open(file_to_load) as election_data:
    #print the file object
    ##print(election_data)
        #OuTPUT <_io.TextIOWrapper name='Election_Analysis\\Resources\\election_results.csv' mode='r' encoding='cp1252'>

#To Write a file to a diectory
#Create a filename vairable to direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","analysis","election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
#This should creat and open the txt file created in the file_to_save...YES IT DID!!
##open(file_to_save, "w")
    
    # Use the open statement to open the file as a text file.
##outfile = open(file_to_save, "w")
    # Write some data to the file.
##outfile.write("Hello World")

# Close the file
##outfile.close()

#MAKE IT CLEANER
with open(file_to_save, "w") as txt_file:
    #write something
    txt_file.write("Hello Sunshine, ")

    #write 3 counties   
        #add a comma and space after each! otherwise they will be smashed together
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson, ")

    #OR write like this
    txt_file.write("Arapahoe, Denver, Jefferson")
    #NEXT LINE   n\    n\   
    txt_file.write("\nArapahoe, \nDenver \n Jefferson")
    txt_file.write("\nCounties in the Election \nArapahoe \nDenver \nJeffferson")



#INSERTED TOTAL VOTES COUNT
#1. Initialize a total vote counter.
total_votes = 0


#INSERTED 
#Declare new List: Candidate names
candidate_options = []

#INSERTED
#Create Dictionary for Candidate and number of votes
#Dictionarys have the curlyS {}
candidate_votes = {}

#INSERTED
#Find Vote %
#vote_percent = (votes / total_votes) * 100

#Open the election results and read the file
with open(file_to_load) as election_data:


#To Do read and analyize data here

#Read the file object with the reader function
    file_reader = csv.reader(election_data)

#PRint just the Header ROW
#Remember to INDEX!!!
    headers = next(file_reader)
    ##print(headers)


#print each row in the csv file.
    for row in file_reader:
    #2. INSERTED add to the total vote count.
        total_votes += 1

        #commented print row out so it will print votes... see changes
       ##print(row)
        #3. Print the toal Votes REMEMBER to index!
        ##print(total_votes)

        #INSERT
        #finding candidate names (running through data starting on row 2 under Header)
        candidate_name = row[2]
        #Print candidate name from each row...... This printed all the lines candidate name....
        ##print(candidate_name)
        

        #InSERT 
        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the listof candidates

        #INSERT 
        #add candidate name to the candidate list.......THis printed all the candidates... not in a list. like a checkerboard.
                                                        ###UNTIL added the if statement above. then it listed the 3 candidates :)
            candidate_options.append(candidate_name)

            ##Begin tracking candidate's vote count.
            candidate_votes[candidate_name] = 0

            #NEED to increase (increment) votes by 1 every time candidates name appears in a row
            ###NOTE needed to align indent with IF 
        candidate_votes[candidate_name] += 1

    ##Determint % of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2Retrieve vote count of a candidte.
        votes = candidate_votes[candidate_name]
        #3calculate percentage of votes  
        # NOTE I removed the * 100 that was at the end of the string and put it in the  print f string
        votes_percentage = float(votes) / float(total_votes) 


        #print candidate list
            #print(candidate_options)

            #Print candidate vote dictionary......This printed Candidate and Votes AT ZERO!, 
        #print(candidate_votes)
                #{'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}


         #4 Print the candidate name and percent votes
         # Removed * 100 from votes_percent above and added the *100:.1f to make the % one decimal.
        print(f'{candidate_name}: recieved {votes_percentage * 100:.1f} % of the vote.')

#Total number of votes cast


#A complete list of candidates who received votes


#Total number of votes each candidate received
    #{'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}

#Percentage of votes each candidate won
    #Charles Casper Stockham: recieved 23.04854332167558 % of the vote.
    #Diana DeGette: recieved 73.81224794501652 % of the vote.
    #Raymon Anthony Doane: recieved 3.1392087333079077 % of the vote.

#The winner of the election based on popular vote


