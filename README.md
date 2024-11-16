# 数値解析特論の最終課題のテンプレ

コードを写すのが面倒な人向けに配布します。

## インストール方法

プロジェクト管理ツールの[uv](https://docs.astral.sh/uv/)を使います。

-   Windows の場合
    ```shell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    実行後、出てきた指示にパスを通してください。

-   macOS の場合
    ```shell
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

その後、依存関係をインストールするために以下を実行してください。

```shell
uv sync
```

## 使い方
```shell
uv run src/main.py
```
