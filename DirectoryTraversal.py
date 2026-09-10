import os

def main():
    for FolderName , SubFolder, FileName in os.walk("Ved"):
        for fname in FileName:
            print("File name : ",fname)
            
if __name__ == "__main__":
    main()