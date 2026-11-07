# # mysite/db_routers.py


# class BackgroundTaskRouter:
#     """django-q2 のモデルのみ SQLite (task_db) に振り分け、

#     それ以外（一般データ、認証など）はすべて PostgreSQL (default) にルーティングする
#     """

#     # ROUTE_APP_LABELS = {"django_q"}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.ROUTE_APP_LABELS:
#             return "task_db"
#         return "default"

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.ROUTE_APP_LABELS:
#             return "task_db"
#         return "default"

#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label in self.ROUTE_APP_LABELS
#             or obj2._meta.app_label in self.ROUTE_APP_LABELS
#         ):
#             return obj1._meta.app_label == obj2._meta.app_label
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """マイグレーション対象のデータベースを厳密に制限する"""
#         # 1. django_q アプリは、task_db 以外でのマイグレーションを絶対に禁止する
#         if app_label in self.ROUTE_APP_LABELS:
#             return db == "task_db"

#         # 2. それ以外のすべてのアプリは、task_db でのマイグレーションを絶対に禁止する（重要）
#         if db == "task_db":
#             return False

#         # 3. それ以外（通常のアプリかつ、default への反映）は許可
#         return db == "default"
