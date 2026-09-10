import sys
import os

def DirectoryScanner(DirectoryPath):
    
    print("files ffrom the directory are : ")
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            print(fname)
def main():
    Border = "_"*40

    print(Border)
    print("  Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) != 2):
        if(sys.argv[1]  == "--h" or sys.argv[1] == "--H"):
            print("this automation script is used to travel directory")
            print("for better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please exexute the script as")
            print("python FileName.py directory")
            print("difrectory name should be absolute path")
        else:
            DirectoryScanner(sys.argv[1])

    else:
        print("invalid no. of arguments")
        print("please us --h or --u for more info")

    print(Border)
    print("Thankyou for using Marvellous Automation Script")
    print(Border)
   
if __name__ == "__main__":
   main()