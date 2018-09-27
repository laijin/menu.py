menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
f_menu=[]
print(menu)
while 1:
    choose=input('选择内容进入或按N退出或按Y返回上一层')
    if menu.get(choose) != None:
        f_menu.append(menu)#与下面的pop相对应，从而实现返回上层的功能
        menu=menu[choose]
        print(menu)
    elif choose=='N':break
    elif choose=='Y':
        if f_menu:
            menu=f_menu.pop()
            print(menu)
        else:print('已经在最上层了')
    else:print('输入有错')

