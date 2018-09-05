#!/usr/bin/env python
"""
主程序文件,选择菜单
"""
from conf import setting
from conf import templates
from module import games
from module import common


if __name__ == "__main__":
    exit_flag = False
    while not exit_flag:
        # 开始菜单
        print(templates.GAME_MENU)
        func = input("\n请选择功能编号：[1-4]")
        if func not in ("1", "2", "3", "4"):
            continue

        # 退出吗
        if func == "4":
            exit_flag = True
            continue

        # 游戏背景
        if func == "1":
            print(templates.GAME_TITLE.format(currrole="", apponent=""))
            common.load_begin()

        # 查看人物信息
        if func == "2":
            cui_str = common.format_info(common.load_info("xmcx"))
            ye_str = common.format_info(common.load_info("ygc"))
            print(templates.ROLE_INFO.format(cui=cui_str, ye=ye_str))

        # 开始游戏
        if func == "3":
            games.start()


