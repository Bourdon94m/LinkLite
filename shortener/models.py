import random
import string

from django.db import models


# Create your models here.

class shortURL(models.Model):
    original_url = models.URLField(max_length=100)
    short_code = models.URLField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"

    @classmethod
    def generate_short_code(cls):
        # Génere un code aléatoire de 6 caracteres
        length = 6
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            if not cls.objects.filter(short_code=code).exists():
                return code

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)


class URLClick(models.Model):
    url = models.ForeignKey(shortURL, on_delete=models.CASCADE, related_name="click_stats")
    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=500, null=True, blank=True)
    referrer = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Click on {self.url.short_code} at {self.clicked_at}"
