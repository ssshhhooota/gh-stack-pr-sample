# gh-stack-pr-sample

`gh stack`（スタックドPR）の動作を試すためのサンプルリポジトリ。

ユーザー管理機能を、依存関係の順に 3 層のスタックへ分割して実装する。

```
main (trunk)
 └── feat-user_models    データモデル
  └── feat-user_api      モデルを使う API
   └── feat-user_frontend API を呼ぶ UI
```
