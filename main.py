#User defined function
import check_internet 
import rMQR_generator
import meme_gen
import git_scheduler
import time

#Global Variables
LOCATION = "M:\\CS\\TitTat\\TechnoSeek-V2.0"
FILE_NAME = "clue.png"
COMMIT_MSG = "SIMPLE GIT COMMIT"

# This function is the main function/ control starts here
def main():
    internet_status = check_internet.is_connected("one.one.one.one")

    if (internet_status == True):
        iterations = int(input("Enter the number of iterations:"))
        sleep_timer = int(input("Enter the break amount between every commit (in secs):"))

        for i in range(0, iterations):
            time.sleep(sleep_timer)
            data = meme_gen.get_data()  #To get data for QR code
            rMQR_generator.Generator(data, LOCATION)    #To generate QR code
            git_scheduler.git_all(LOCATION, FILE_NAME, COMMIT_MSG)  #To commit 
            print(f"\nIteration {i+1} done!! \n\n")

    else:
        #Call later
        print("Check your connetion")
        print("Exiting")

main()