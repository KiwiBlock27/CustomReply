from tgfs.utils.translation import registry, en

class CustomText(en):
    START_TEXT="Hello how are you"
    
    HELP_TEXT = "This is help command"
    
registry["en"]=CustomText
