from tgfs.utils.translation import registry, en

class CustomText(en):
    START_TEXT="Hey there how are you\nYou can send me any file and i will generate link for that file"
    HELP_TEXT = """
Available Commands:
/start - Start the bot
/help - Show this help message
/group - Start creating a group of files
/done - Finish adding files to the group
/files - List your uploaded files or created groups
/setln - Change your language
/cancel - Cancel the current operation
"""

registry["en"]=CustomText
