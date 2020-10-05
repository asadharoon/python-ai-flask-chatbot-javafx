def mergeHelpingverbs(stringList):
    a=""
    if len(stringList)==0:
        return ""
    if len(stringList)<1:
        a=a+stringList.pop(0)
        return a
    for i in stringList:
        if(stringList[-1]!=i):
            a+=i+"_"
        elif(stringList[-1]==i):
            a+=i
    return a
def split_sentences(string):
    #string= string.replace(',','.')
    listofsentences=string.split('.')
    print("length of split is {}".format(len(listofsentences)))
    print(listofsentences)
    if(listofsentences[-1]=='' and len(listofsentences)<3):
        return [string]
    listofsentences.pop()
    return listofsentences