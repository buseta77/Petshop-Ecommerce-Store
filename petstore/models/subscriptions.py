from django.db import models


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def placeSubscriber(self):
        self.save()

    @staticmethod
    def get_all_subscribers():
        return Subscription.objects.all()