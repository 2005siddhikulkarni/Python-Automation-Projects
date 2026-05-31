import hashlib
import os

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for FName in FileName:
            FName = os.path.join(FolderName, FName)
            Checksum = CalculateCheckSum(FName)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(FName)

            else:
                Duplicate[Checksum] = [FName]

    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Cnt = 0

    for value in Result:
        for subvalue in value:
            Cnt += 1
            print(subvalue)
        print("value of count is: ",Cnt)
        Cnt = 0



            

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)   # Data

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Cnt = 0
    Count = 0

    for value in Result:
        for subvalue in value:
            Cnt += 1
            if(Cnt > 1):
                print("Deleted file: ",subvalue)
                os.remove(subvalue)
                Count += 1
        Cnt = 0

    print("Total deleted files: ",Count)


def main():
   DeleteDuplicate()

if __name__ == "__main__":
    main()