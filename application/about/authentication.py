from about.models import UserProfile


class EmailAuthBackend(object):
    """Authenticate using e-mail account
    """
    def authenticate(self, username=None, password=None):
        try:
            user = UserProfile.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None

