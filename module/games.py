#!/usr/bin/env python
"""
游戏主程序,开始游戏KO模式
start()方法开始进行游戏
print_status()方法显示生命值状态信息
"""
import random
from module import common
from module.people import Role
from files import attack_talk

def print_status(currobj, otherobj, attack_status):
    """
    根据攻击的结果输出生命值信息
    :param currobj:当前选中角色对象
    :param otherobj:对方角色
    :param attack_status:攻击的状态，True(攻击成功) False(攻击失败）
    :return:
    """
    # 显示对话
    if attack_status:
        otherobj.talk(attack_talk.attack_succ_msg[random.randrange(4)], otherobj.talkside)
    else:
        otherobj.talk(attack_talk.attack_fail_msg[random.randrange(4)], otherobj.talkside)

    # 打印双方当前生命值
    print("\033[40;1m【{curr}】生命值{life1}，【{other}】 生命值：{life2}\033[0m".format(curr=currobj.name,
                                                                             life1=currobj.blood,
                                                                             other=otherobj.name,
                                                                             life2=otherobj.blood))


def start():
    # 从配置文件获取角色信息
    cuixue_info = common.load_info("xmcx")
    ye_info = common.load_info("ygc")

    # 实例化两个角色对象
    cuixue = Role(**cuixue_info)
    ye = Role(**ye_info)

    flag = False
    while not flag:
        c_role = input("\n\033[31;1m 请选择游戏角色 1->西门吹雪   2->叶孤城 : \033[0m")
        # 根据用户选择设置一个主角色
        if c_role == "1":
            cuixue.is_main
            currobj = cuixue
            otherobj = ye
        else:
            ye.is_main
            currobj = ye
            otherobj = cuixue
        flag = True

    ye.talk("西门吹雪,我这把剑 剑名巨厥，长三尺八，乃海底塞铁所铸，吹毛断发", ye.talkside)
    cuixue.talk("三尺九寸，西域玄铁铸，不比你差", cuixue.talkside)
    ye.talk("你的心静下来了吗", ye.talkside)
    cuixue.talk("我等待这一天已经很久了，废话少说，那就出招吧！", cuixue.talkside)

    goon_flag = True
    while goon_flag:
        # 用户的角色选择攻击招式
        skillvalue = currobj.choose_skill()
        # 对手接招
        jstatus = otherobj.jiezhao(skillvalue, random.randrange(3))
        print_status(currobj, otherobj, jstatus)
        # 对手干掉了吗?
        if not otherobj.is_alive:
            print("\n\033[33;1m 终于,{0} 完胜 {1}, 不愧是{2}!!!\033[0m;".format(currobj.name, otherobj.name, currobj.alias))
            goon_flag = False

        # 对手发招(自动)
        skillvalue = otherobj.auto_skill()
        # 主角色接招
        jstatus = currobj.jiezhao(skillvalue, random.randrange(3))
        print_status(otherobj, currobj, jstatus)

        # 主角色活着吗?
        if not currobj.is_alive:
            print("\n\033[33;1m经过多个回合,{0} 不敌 {1}, 应声倒下,吐血而亡!!!\033[0m;".format(currobj.name, otherobj.name))
            goon_flag = False
    print("\nGAME OVER")
