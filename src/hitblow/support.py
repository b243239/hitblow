import itertools
import random

def generate_all_candidates(digits=3):
    """すべての可能性（重複なしの数字の順列）を生成する"""
    return ["".join(p) for p in itertools.permutations("0123456789", digits)]

def check_hit_blow(secret, guess):
    """HitとBlowを計算する内部ヘルパー"""
    hit = sum(s == g for s, g in zip(secret, guess))
    blow = sum(g in secret for g in guess) - hit
    return hit, blow

def get_remaining_candidates(history, digits=3):
    """過去の履歴から、矛盾しない残り候補をすべて絞り込む"""
    candidates = generate_all_candidates(digits)
    for past_guess, past_hit, past_blow in history:
        valid_candidates = []
        for cand in candidates:
            h, b = check_hit_blow(cand, past_guess)
            # 過去の推測と同じHit/Blow数になるものだけが正解の可能性がある
            if h == past_hit and b == past_blow:
                valid_candidates.append(cand)
        candidates = valid_candidates
    return candidates

def analyze_history(guess, hit, blow):
    """過去のコール結果から、UIイメージに沿った分析テキストを生成"""
    digits_str = ", ".join(guess)
    if hit == 0 and blow == 0:
        return f"【除外確定】 {digits_str} は使われていない"
    elif blow == 0 and hit > 0:
        return f"{digits_str} のどれか{hit}つは確定"
    elif hit == 0 and blow > 0:
        return f"{digits_str} のうち{blow}つは場所違いで存在"
    else:
        return f"確定{hit}つ、場所違い{blow}つを含んでいる"

def show_support_dashboard(history, digits=3):
    """コンパクトなダッシュボードを画面に出力する"""
    print("\n" + "=" * 45)
    print(" 📊 サポートダッシュボード")
    print("=" * 45)
   
    if not history:
        print(" まだコール履歴がありません。まずは数字を予想してみてね！")
        print("=" * 45 + "\n")
        return

    print(" [過去のコール結果と判定サポート]")
    for guess, hit, blow in history:
        analysis = analyze_history(guess, hit, blow)
        # 見やすくフォーマット
        print(f"  {guess} │ {hit} Hit, {blow} Blow │ {analysis}")
   
    # 残り候補の計算
    candidates = get_remaining_candidates(history, digits)
   
    print("-" * 45)
    print(f" 💡 現在の残り候補数：{len(candidates)} 通り")
   
    if len(candidates) > 0:
        # ランダムに1つ選んでおすすめとして提示
        recommendation = random.choice(candidates)
        # 候補が少ない場合は、具体的に全部見せるなどの工夫も可能
        print(f"    次は例えば「 {recommendation} 」などをコールしてみるのがオススメです！")
    else:
        print("    【エラー】履歴に矛盾が発生しています。")
       
    print("=" * 45 + "\n")