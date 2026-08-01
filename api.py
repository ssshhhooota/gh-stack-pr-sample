"""ユーザー管理機能のAPI層。models層に依存する。"""
from models import User

_users: dict[int, User] = {}


def create_user(id: int, name: str, email: str) -> User:
    """ユーザーを作成して保存する。"""
    user = User(id=id, name=name, email=email)
    _users[user.id] = user
    return user


def get_user(id: int) -> User | None:
    """IDからユーザーを取得する。存在しなければNone。"""
    return _users.get(id)
