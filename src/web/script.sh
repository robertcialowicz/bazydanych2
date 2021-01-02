python3 manage.py runserver 0.0.0.0:8000 &
sleep 7 && 
(    cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@admin.com", "admin")
else:
    print('User "{}" exists already, not created'.format("admin"))
EOF
) &
sleep 2 && python manage.py migrate &
tail -f /dev/random &> /dev/null