import frappe
from frappe.model.document import Document

class TaskTree(Document):
    pass


def progress_calculation(self,method= None):
    if self.parent_task:
        sub_tasks = frappe.get_list("Task", filters={"parent_task": self.parent_task}, pluck = "name")
        sub_task_progress = []
        for sub_task in sub_tasks:
            child_task = frappe.get_doc("Task", sub_task)
            sub_task_progress.append(child_task.progress)
        if sub_task_progress:
            total_progress = sum(sub_task_progress)
            average_progress = round(total_progress / len(sub_task_progress), 3)
            parent_task = frappe.get_doc("Task", self.parent_task)
            parent_task.progress = average_progress
            parent_task.save()

	