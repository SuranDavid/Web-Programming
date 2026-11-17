from django.core.management.base import BaseCommand
from django.utils import timezone
from myApp.models import Student, Module
class Command(BaseCommand):
    help = 'Add a small set of sample students and modules'
    def handle(self, *args, **options):
        module_data = [('MOD002619','Web Programming'),('MOD002691','Final Project'),('MOD003212','Introduction to Programming')]
        modules = {code: Module.objects.update_or_create(code=code, defaults={'name':name})[0] for code,name in module_data}
        students = [
            ('Amara','Perera',20,'amara@example.com',['MOD002619','MOD003212']),
            ('Kasun','Fernando',21,'kasun@example.com',['MOD002619']),
            ('Nimali','Silva',19,'nimali@example.com',['MOD003212']),
            ('Ravindu','Jayasinghe',22,'ravindu@example.com',['MOD002691','MOD002619']),
            ('Tharushi','De Silva',20,'tharushi@example.com',['MOD002691']),
            ('Daniel','Peris',23,'daniel@example.com',['MOD002619','MOD003212']),
        ]
        for first,last,age,email,codes in students:
            student, _ = Student.objects.get_or_create(email=email, defaults={'firstName':first,'lastName':last,'age':age,'enrolmentDate':timezone.now()})
            student.modules.set([modules[c] for c in codes])
        self.stdout.write(self.style.SUCCESS('Sample modules and students are ready.'))
