from src.Chatbots.GetStoryFromFile import getstorylines_from_file
import aiml

class Chatbot:
    def __init__(self):
        self.kernel=aiml.Kernel()
        self.kernel.learn("startup.xml") # execute startup xml file
        self.kernel.respond("load aiml")
        getstorylines_from_file()
       # print("Bot: Hi I am Bot.")

    def conversation(self,inputs):
       # while True:
        reply=self.kernel.respond(inputs)
        return reply
            # file_patterns=open("patterns_list.txt", 'r')
            # for line in file_patterns:
            #     print("Me: "+line)
            #     reply=self.kernel.respond(line)
            #     if reply:
            #         print("Bot: "+reply)
            # break


# if __name__=="__main__":
#     # getstorylines_from_file()
#     # chatbot=Chatbot()
#     # chatbot.conversation()