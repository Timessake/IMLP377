def convertInputString():
    #請使用者輸入一串字串，先轉換字串為統一小寫
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ") 
    return rawInput

def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    #去除相關標點符號
    for i in dirtyList:
        dirtyList=dirtyList.replace(i,'')
    return dirtyList

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if straightList==reversedList: 
        return "The text you have entered is a palindrome!" 
    else: 
        return "The text you have entered is not a palindrome." 

def main(): 
    print("\nPalindrome checker") 
    a=convertInputString()
    a=stripAnalphabetics(a)
    print(runPalindromeCheck(a))
main() 