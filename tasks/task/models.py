from django.db import models

class TaskItem(models.Model):

    deposit = "D"
    withdraw = "W"
    transactions = (
        (deposit, "Deposit"),
        (withdraw, "Withdrawal"),
    )

    name = models.CharField(max_length = 255)
    pin = models.TextField(default = "")
    transaction = models.CharField(max_length = 1,
                                   choices = transactions,
                                   default = "")
    sum = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now = True)

    owner = models.ForeignKey("auth.User", models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name
