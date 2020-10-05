
# for saving and testing patterns we use List to test these sentences in main file.
listofpatterns=[]


# Note: I am saving AIML Commands automatically not hardcoded.
lines = ['<aiml version="1.0.1" encoding="UTF-8">', "\n"] # for saving commands of AIML
"""
<------------------------------ To generate String of command of AIML like category,pattern,template ---------------------------------->
"""
def appendAIML(pattern,template):
    patforlist=''
    # for saving patterns
    a='<pattern>'
    for word in pattern:
        patforlist=patforlist+word
        a=a+word
    pat=a[0:len(a)-1]
    patforlist=patforlist[0:len(patforlist)-1]
    if pat[-1]=='.':
        pat=pat.replace('.','')
        patforlist=patforlist.replace('.','') # at end of each sentence . is stored which is unrecognizable by chatbot. So remove it.
    pat=pat+'</pattern>'
    # for saving patterns in list of patterns so that I could Test it in main function.
    listofpatterns.append(patforlist+"\n")
    # for saving template.
    templates="<template>"
    for word in template:
        templates=templates+word
    final_template=templates[0:len(templates)-1]
    final_template=final_template+"</template>"
    lineList = ['<category>', '\n',pat,'\n',final_template,'\n', '</category>', '\n']
    return "".join(lineList)

"""
<--------------------------- Get Whole Story from File.txt and read it line by line and generate aiml code --------->
"""
def getstorylines_from_file():
    storyfile=open("my_story.txt", "r")
    for storylines in storyfile.readlines():
        lines.append(appendAIML(pattern=storylines.upper(),template="Hmm! Next."))
    aimlfile=open('basic_chat.aiml', "w")

    # Storing * pattern at last of file to avoid mistakes.
    lines.append("\n<category>\n<pattern>HELLO I AM *</pattern>\n<template>Hi! Nice to meet you <star/></template>\n</category>\n")
    lines.append("\n<category>\n<pattern>DO YOU WANT TO LISTEN STORY</pattern>\n<template>Yes Why not</template>\n</category>\n")
    lines.append("\n<category>\n<pattern>TODAY I WILL TEACH YOU SOME LESSON FROM STORY</pattern>\n<template>Ok please start the story</template>\n</category>\n")
    lines.append("\n<category>\n<pattern>MORAL IS IF YOU HELP SOME OLD AGE PEOPLES THEN GOD WILL HELP YOU WHEN YOU NEED HELP</pattern>\n<template>Wow Good Mom I love you</template>\n</category>\n")
    lines.append("\n<category>\n<pattern>*</pattern>\n<template>I did not understand</template>\n</category>\n</aiml>")
    aimlfile.write("".join(lines))
    aimlfile.close()

    # for testing patterns I have saved patterns in .txt file
    # to view it open patterns_list.txt file to view sentences which could be tested in MainChatbotFile.py file.
    listofpatternsFile=open("patterns_list.txt", 'w+')
    listofpatternsFile.write("".join(listofpatterns))

