"""ユーザー管理機能のフロントエンド層。api層に依存する。"""
from api import create_user, get_user


def render_user_card(id: int) -> str:
    """ユーザーIDから表示用のカードHTMLを生成する。"""
    user = get_user(id)
    if user is None:
        return f"<div class='user-card'>ユーザー {id} は見つかりません</div>"
    return f"<div class='user-card'><b>{user.name}</b> ({user.email})</div>"


def register_and_render(id: int, name: str, email: str) -> str:
    """ユーザーを登録してそのカードHTMLを返す。"""
    create_user(id, name, email)
    return render_user_card(id)
