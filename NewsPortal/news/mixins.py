class LoginRequiredMixin:
    """
    Миксин, который проверяет наличие аутентификации пользователя.
    Если пользователь не авторизован, то он будет перенаправлен на страницу авторизации.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        pass
