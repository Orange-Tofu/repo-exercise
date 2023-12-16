import check_internet #User defined function

#Global Variables
LOCATION = "M:\\CS\\TitTat\\TechnoSeek-V2.0"
FILE_NAME = "clue.png"
COMMIT_MSG = "SIMPLE GIT COMMIT"

# This function is the main function/ control starts here
def main():
    internet_status = check_internet.is_connected("one.one.one.one")

    if (internet_status == True):
        # print(git_directory, file_path, commit_msg, sep="\n\n")
        # standard_output = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')



    else:
        #Call later
        pass


main()