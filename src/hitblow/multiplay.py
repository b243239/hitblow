def select_player_count() -> int:
    """プレイ人数を1～3人から選択する。"""
    while True:
        value = input("プレイ人数を入力してください（1～3人）> ").strip()

        if not value.isdigit():
            print("1～3の数字を入力してください")
            continue

        player_count = int(value)

        if 1 <= player_count <= 3:
            return player_count

        print("1～3の範囲で入力してください")


def player_prompt(player_number: int):
    print(f"{player_number}番目の人の番です。")


def next_player(current_player: int, player_count: int) -> int:
    """次に予想するプレイヤー番号を返す。"""
    if current_player == player_count:
        return 1

    return current_player + 1


def show_winner(player_number: int) -> None:
    """勝者を表示する。"""
    print(f"{player_number}番目の人の勝ちです！")