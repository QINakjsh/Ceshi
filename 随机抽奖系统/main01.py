from flask import Flask,render_template
import random





class hezi:
    def __init__(self,史诗体验卡=0,欢乐豆=0,菜篮子=0,换将卡=0,手气卡=0,点将卡=0,进阶丹=0,
                 雁翎甲=0,招募令=0,史诗宝珠碎片=0,良品武将=0,史诗宝珠=0,将魂=0,皮肤加动态包=0
                 ,权十武将=0,权三武将=0,权一武将=0,心愿积分=0,雁翎=0):
        self.心愿积分=心愿积分
        self.雁翎=雁翎
        self.史诗体验卡=史诗体验卡
        self.欢乐豆=欢乐豆
        self.菜篮子=菜篮子
        self.换将卡=换将卡
        self.手气卡=手气卡
        self.点将卡=点将卡
        self.进阶丹=进阶丹
        self.雁翎甲=雁翎甲
        self.招募令=招募令
        self.史诗宝珠碎片=史诗宝珠碎片
        self.良品武将=良品武将
        self.史诗宝珠=史诗宝珠
        self.将魂=将魂
        self.皮肤加动态包=皮肤加动态包
        self.权十武将=权十武将
        self.权三武将=权三武将
        self.权一武将=权一武将

    def qucho(self):

        if self.皮肤加动态包>1:
            self.史诗宝珠+=(self.皮肤加动态包-1)*2
            self.皮肤加动态包=1
        if self.权十武将>1:
            self.史诗宝珠+=(self.权十武将-1)*3
            self.权十武将=1
        if self.权三武将>1:
            self.史诗宝珠+=(self.权三武将-1)*15
            self.权三武将=1
        if self.权一武将>1:
            self.史诗宝珠+=(self.权一武将-1)*30
            self.权一武将=1

    def dy(self):

        if self.史诗宝珠:
            print(f"史诗宝珠*{self.史诗宝珠}",end=',')
        if self.权一武将:
            print(f"权一武将*{self.权一武将}",end=',')
        if self.权三武将:
            print(f"权三武将*{self.权三武将}", end=',')
        if self.权十武将:
            print(f"权十武将*{self.权十武将}", end=',')
        if self.皮肤加动态包:
            print(f"皮肤加动态包*{self.皮肤加动态包}", end=',')
        if self.良品武将:
            print(f"良品武将*{self.良品武将}",end=',')
        if self.史诗宝珠碎片:
            print(f"史诗宝珠碎片*{self.史诗宝珠碎片}",end=',')

        if self.招募令:
            print(f"招募令*{self.招募令}", end=',')
        if self.雁翎甲:
            print(f"雁翎甲*{self.雁翎甲}",end=',')
        if self.进阶丹:
            print(f"进阶丹*{self.进阶丹}", end=',')
        if self.史诗体验卡:
            print(f'史诗体验卡*{self.史诗体验卡}', end=',')
        if self.欢乐豆:
            print(f"欢乐豆*{self.欢乐豆}", end=',')
        if self.菜篮子:
            print(f"菜篮子*{self.菜篮子}", end=',')
        if self.换将卡:
            print(f"换将卡*{self.换将卡}", end=',')
        if self.手气卡:
            print(f"手气卡*{self.手气卡}", end=',')
        if self.点将卡:
            print(f"点将卡*{self.点将卡}", end=',')


        if self.心愿积分:
            print(f"心愿积分*{self.心愿积分}",end=',')
        if self.雁翎:
            print(f"雁翎*{self.雁翎}",end=',')
        if self.将魂:
            print(f"将魂*{self.将魂}",end=',')
    def dy01(self):
        s=""

        if self.史诗宝珠:
            s+=f"史诗宝珠*{self.史诗宝珠},"
        if self.权一武将:
            s+=f"权一武将*{self.权一武将},"
        if self.权三武将:
            s+=f"权三武将*{self.权三武将},"
        if self.权十武将:
            s+=f"权十武将*{self.权十武将},"
        if self.皮肤加动态包:
            s+=f"皮肤加动态包*{self.皮肤加动态包},"
        if self.良品武将:
            s+=f"良品武将*{self.良品武将},"
        if self.史诗宝珠碎片:
            s+=f"史诗宝珠碎片*{self.史诗宝珠碎片},"

        if self.招募令:
            s+=f"招募令*{self.招募令},"
        if self.雁翎甲:
            s+=f"雁翎甲*{self.雁翎甲},"
        if self.进阶丹:
            s+=f"进阶丹*{self.进阶丹},"
        if self.史诗体验卡:
            s+=f'史诗体验卡*{self.史诗体验卡},'
        if self.欢乐豆:
            s+=f"欢乐豆*{self.欢乐豆},"
        if self.菜篮子:
            s+=f"菜篮子*{self.菜篮子},"
        if self.换将卡:
            s+=f"换将卡*{self.换将卡},"
        if self.手气卡:
            s+=f"手气卡*{self.手气卡},"
        if self.点将卡:
            s+=f"点将卡*{self.点将卡},"

        if self.心愿积分:
            s+=f"心愿积分*{self.心愿积分},"
        if self.雁翎:
            s+=f"雁翎*{self.雁翎},"
        if self.将魂:
            s+=f"将魂*{self.将魂},"

        return s
    def kkk(self, other):
        self.史诗体验卡 += other.史诗体验卡
        self.欢乐豆 += other.欢乐豆
        self.菜篮子 += other.菜篮子
        self.换将卡 += other.换将卡
        self.手气卡 += other.手气卡
        self.点将卡 += other.点将卡
        self.进阶丹 += other.进阶丹
        self.雁翎甲 += other.雁翎甲
        self.招募令 += other.招募令
        self.史诗宝珠碎片 += other.史诗宝珠碎片
        self.良品武将 += other.良品武将
        self.史诗宝珠 += other.史诗宝珠
        self.将魂 += other.将魂
        self.皮肤加动态包 += other.皮肤加动态包
        self.权十武将 += other.权十武将
        self.权三武将 += other.权三武将
        self.权一武将 += other.权一武将



def txt_01(e):
        global wp
        wp = hezi(心愿积分=e, 雁翎=20 * e, 将魂=2 * e)
        for r in range(e):
            sjsh=random.randint(0,99999)

            for i in dict_jp:
                if sjsh<i:
                    list_d=dict_jp[i].strip().split("*")
                    dict_j={f"{list_d[0]}":int(list_d[1])}
                    k=hezi(**dict_j)
                    wp.kkk(k)
                    break

        wp.qucho()
        return wp.dy01()

if __name__ == '__main__':


    list_1=[]

    s=0
    dict_jp={}
    with open("1.txt",mode="r",encoding="UTF-8") as f:
        list_txt=f.readlines()
        for i in list_txt:
            list_wp=i.strip().split(",")
            s+=float(list_wp[1])*1000
            list_1.append(list_wp[0])
            dict_jp[s]=list_wp[0]
    # while i:
    #     e=int(input("\n请输入抽奖个数："))
    #     wp=hezi(心愿积分=e,雁翎=20*e,将魂=2*e)
    #     for r in range(e):
    #         sjsh=random.randint(0,99999)
    #
    #         for i in dict_jp:
    #             if sjsh<i:
    #                 list_d=dict_jp[i].strip().split("*")
    #                 dict_j={f"{list_d[0]}":int(list_d[1])}
    #                 k=hezi(**dict_j)
    #                 wp.kkk(k)
    #                 break
    #
    #     wp.qucho()
    #     wp.dy()

    print(list_1)
    app = Flask(__name__)  # 创建服务器对象


    @app.route('/index')
    def index():
        return render_template("1.html",lsit_y=list_1)
    @app.route('/chj')
    def chj():
        return render_template("1.html",lsit_y=list_1,h=txt_01(1))
    @app.route('/chj50')
    def chj50():
        return render_template("1.html", lsit_y=list_1, h=txt_01(50))

    app.run(debug=True)