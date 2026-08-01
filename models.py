"""ユーザー管理機能のデータモデル層。"""
from dataclasses import dataclass


@dataclass
class User:
    """アプリケーションのユーザーを表すモデル。"""

    id: int
    name: str
    email: str
