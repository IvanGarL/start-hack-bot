class TaskBuffer(object):

    list_header = ":mag: You have the following tasks for today:"
    list_updated = "Your to-do list have just been updated. Now you have the next followin tasks:"

    def __init__(self):
        self.tasks = []