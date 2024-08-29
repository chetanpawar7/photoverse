from app.models import User, PostMaster, ImageMaster, CommentMaster

def get_user_instace(user_id:int = None, username:str = None, user=None):
    try:
        if user_id:
            return User.objects.get(id=user_id)
        if username:
            return User.objects.get(username=username)
        if user:
            return User.objects.get(user=user)
    except Exception as ex:
        return ex
    
def get_posts(user_id:int=None):
    try:
        if user_id:
            return PostMaster.objects.filter(user_id=user_id)
        else:
            return PostMaster.objects.all()
    except Exception as ex:
        return ex

def get_comments(user_id:int=None):
    try:
        if user_id:
            return CommentMaster.objects.filter(user_id=user_id)
        else:
            return CommentMaster.objects.all()
    except Exception as ex:
        return ex

