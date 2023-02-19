# from news.models import User
# new_user1 = User.objects.create_user('ALEX')
# new_user2 = User.objects.create_user('GARI')
# from news.models import Author
# Author.objects.create(full_name="Иванов Иван Иванович", gender="мужской", age=22)
# Author.objects.create(full_name="Петров Петр Петрович", gender="мужской", age=40)
#
# from news.models import Category
# Category.objects.create(category_name="Бизнес")
# Category.objects.create(category_name="Спорт")
# Category.objects.create(category_name="Техника")
# Category.objects.create(category_name="Море")
#
# from news.models import Post
# Post.objects.create(post_name="Моряки идут", post_news='PO', author_id=1)
# Post.objects.create(post_name="Жизнь боль", post_news='PO', author_id=2)
# Post.objects.create(post_name="Деньги зло", post_news=' NE', author_id=2)
#
# from news.models import Post_Category
# Post_Category.objects.create(post_id=1, category_id=2)
# Post_Category.objects.create(post_id=3, category_id=1)
# Post_Category.objects.create(post_id=3, category_id=4)
#
# from news.models import Comment
# Comment.objects.create(comment_name="комент1",comment_author="автор1", post_id=1, user_id=1)
# Comment.objects.create(comment_name="комент2",comment_author="автор1", post_id=2, user_id=1)
# Comment.objects.create(comment_name="комент3",comment_author="автор2", post_id=3, user_id=2)
# Comment.objects.create(comment_name="комент4",comment_author="автор3", post_id=4, user_id=2)
#
#
# news_1 = Post.objects.get(id=1).rating_post