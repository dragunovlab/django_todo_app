from django.db import models

class Task(models.Model):
    title = models.CharField("Название задачи", max_length=200)
    completed = models.BooleanField("Выполнено", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def completion_percentage(self):
        """
        Рассчитывает процент выполнения подзадач.
        Если подзадач нет, возвращает 0.
        """
        total = self.subtask_set.count()
        if total == 0:
            return 0
        done = self.subtask_set.filter(completed=True).count()
        return int((done / total) * 100)

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField("Название подзадачи", max_length=200)
    completed = models.BooleanField("Выполнено", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} — {self.title}"
