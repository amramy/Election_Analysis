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
with open(file_to_load) as election_data:
    #print the file object
    print(election_data)
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



with open(file_to_load) as election_data:


#To Do read and analyize data here

#Read the file object with the reader function
    file_reader = csv.reader(election_data)

#PRint just the Header ROW
#Remember to INDEX!!!
    headers = next(file_reader)
    print(headers)


#print each row in the csv file.
#   for row in file_reader:
#       print(row)


#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


