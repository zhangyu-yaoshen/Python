#!/usr/bin/env python
# -*- coding:utf-8 -*-
BeiJing_Map = {
    "通州区":{"潞城镇":["潞城一村","潞城二村","潞城三村"],
           "永顺镇":["永顺一村","永顺二村","永顺三村"],
           "梨园镇":["梨园一村","梨园二村","梨园三村"]
           },
    "大兴区":{"大兴1镇":["大兴1镇一村","大兴1镇二村","大兴1镇三村"],
           "大兴2镇":["大兴2镇一村","大兴2镇二村","大兴2镇三村"],
           "大兴3镇":["大兴3镇一村","大兴3镇二村","大兴3镇三村"]
           },
    "顺义区":{"顺义1镇":["顺义1镇一村","顺义1镇二村","顺义1镇三村"],
           "顺义2镇":["顺义2镇一村","顺义2镇二村","顺义2镇三村"],
           "顺义3镇":["顺义3镇一村","顺义3镇二村","顺义3镇三村"]
           }
}
exit_flag = False#标志位
while not exit_flag:
    print("==========欢迎来北京==========")
    for i in BeiJing_Map:
        print(i)
    choice = input("请选择去哪》》》|退出请安q:")
    if choice in BeiJing_Map:
        while not exit_flag:
            print("==========欢迎来%s==========" % (choice))
            for i2 in BeiJing_Map[choice]:
                print("\t",i2)
            choice2 = input("请选择去哪2》》》|退出请安q:")
            if choice2 in BeiJing_Map[choice]:
                while not exit_flag:
                    print("==========欢迎来%s==========" % (choice2))
                    for i3 in BeiJing_Map[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("请选择去哪3》》》|退出请安q:")
                    if choice3 in BeiJing_Map[choice][choice2]:
                        print("==========欢迎来%s==========" % (choice3))
                        # for i4 in BeiJing_Map[choice][choice2][choice3]:
                        #     print("==========欢迎来%s==========" % (choice3))
                        #     print("\t\t\t",i4)
                        choice4 = input("最后一层，按b返回|退出请安q:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
    if choice == "q":
        exit_flag = True


