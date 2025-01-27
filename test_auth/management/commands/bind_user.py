from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=3)

        group, created = Group.objects.get_or_create(
            name='Manager',
        )

        permission_profile = Permission.objects.get(
            codename='view_profile',
        )

        permission_log = Permission.objects.get(
            codename='view_logentry',
        )

        # добавление разрешения для группы
        group.permissions.add(permission_profile)


        # добавление юзера в группу
        user.groups.add(group)

        # свзяать юзера напрямую с разрешением
        user.user_permissions.add(permission_log)

        group.save()
        user.save()

