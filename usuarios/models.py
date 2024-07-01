from django.db import models

def is_logado(request):
    if not request.user.username:
        return False
    
    return True

