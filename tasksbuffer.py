class TaskBuffer(object):

    list_header = ":mag: You have the following tasks for today:"
    list_updated = "Your to-do list have just been updated. Now you have the next followin tasks:"

    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)
        mssg = self.list_updated + "\n"
        for task in self.tasks:
            mssg+=":heavy_check_mark:" + task + "\n"
        
        return mssg
