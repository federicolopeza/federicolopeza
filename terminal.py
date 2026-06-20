from datetime import datetime
from zoneinfo import ZoneInfo

import gifos


def main():
    t = gifos.Terminal(750, 420, 15, 15)
    t.set_prompt("\x1b[0;92mfederico\x1b[0m@\x1b[0;93mpentagoo ~> \x1b[0m")
    tz = ZoneInfo("America/Montevideo")
    year_now = datetime.now(tz).strftime("%Y")

    # --- BIOS boot sequence ---
    t.toggle_show_cursor(False)
    t.gen_text("Pentagoo Systems BIOS v1.0.11", 1)
    t.gen_text(
        f"Copyright (C) {year_now}, \x1b[32mPentagoo Labs Inc.\x1b[0m",
        2,
    )
    t.gen_text("\x1b[94mGitHub Profile Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 5)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, "
        "\x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Memory Test: {i}", 7, count=2, contin=True)
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 9, count=10, contin=True)

    # --- Boot animation ---
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("", 2, count=5, contin=True)

    # --- Login ---
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mPentagoo OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("federicolopeza", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("**************", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(tz).strftime("%a %b %d %I:%M:%S %p %Z %Y")
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    # --- Run neofetch ---
    t.gen_prompt(8, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mneofetc", 8, contin=True)
    t.delete_row(8, t.curr_col - 7)
    t.gen_text("\x1b[92mneofetch\x1b[0m", 8, count=3, contin=True)

    # --- Fetch GitHub stats ---
    stats = gifos.utils.fetch_github_stats("federicolopeza")
    top_langs = [lang[0] for lang in stats.languages_sorted[:5]]

    # --- Neofetch display ---
    t.clear_frame()
    t.toggle_show_cursor(False)

    info = f"""\
    \x1b[32;1mfedericolopeza\x1b[0m@\x1b[32;1mGitHub\x1b[0m
    \x1b[32m------------------------\x1b[0m
    \x1b[32mOS:\x1b[0m       Montevideo, Uruguay
    \x1b[32mHost:\x1b[0m     AutoP2P / Rekon / Pentagoo
    \x1b[32mKernel:\x1b[0m   Full Stack + Offensive Sec
    \x1b[32mShell:\x1b[0m    Python, TypeScript, FastAPI
    \x1b[32mDE:\x1b[0m       VS Code
    \x1b[32mUptime:\x1b[0m   shipping weekly

    \x1b[32;1mGitHub Stats:\x1b[0m
    \x1b[32m------------------------\x1b[0m
    \x1b[32mRank:\x1b[0m         {stats.user_rank.level}
    \x1b[32mStars:\x1b[0m        {stats.total_stargazers}
    \x1b[32mCommits:\x1b[0m      {stats.total_commits_last_year}
    \x1b[32mPRs:\x1b[0m          {stats.total_pull_requests_made}
    \x1b[32mPR Merged:\x1b[0m    {stats.pull_requests_merge_percentage}%
    \x1b[32mContribs:\x1b[0m     {stats.total_repo_contributions}
    \x1b[32mLanguages:\x1b[0m    {", ".join(top_langs)}"""

    t.gen_text(info, 1, count=5, contin=True)

    t.gen_prompt(t.curr_row + 1)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[32m# build > hype\x1b[0m", t.curr_row, contin=True)
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()
