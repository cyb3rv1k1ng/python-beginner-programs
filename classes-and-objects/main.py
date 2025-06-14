from user import User
from post import Post

app_user_one = User("user@user.com", "Nana", "Password123!", "DevOps Engineer")
app_user_one.get_user_info()

# app_user_one.change_job_title("Cloud Engineer")
# app_user_one.get_user_info()

app_user_two = User("user2@user.com", "Jim", "Password321!", "Software Engineer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_one.name)
new_post.get_post_info()