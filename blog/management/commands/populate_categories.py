from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "Ths Command inserts category data"
    
    def handle(self, *args: Any, **options: Any):
        #Delete Existing Files
        Category.objects.all().delete()
        
        category = ['Sports','Technology','Science','Art','Food']
   
        for category_name in category:
            Category.objects.create(name= category_name)
        

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))