from app_test.models import RbData

# static txt format data
# http://cm.sh.dl4.baidupcs.com/file/e3e43df3cf9f1590eae92507ccdb1247?bkt=p2-nj02-911&fid=1832116389-250528-340137501647238&time=1444006894&sign=FDTAXGERLBH-DCb740ccc5511e5e8fedcff06b081203-KthrcQ1O7z5W3iYmfKdfLv7C3ko%3D&to=scnj2&fm=Nan,B,M,mn&sta_dx=0&sta_cs=0&sta_ft=txt&sta_ct=0&fm2=Nanjing02,B,M,mn&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=1400e3e43df3cf9f1590eae92507ccdb1247a9afeff1000000012a0d&sl=81395788&expires=8h&rt=sh&r=137869940&mlogid=6433134671485730120&vuk=1832116389&vbdid=3746494203&fin=rb.txt&fn=rb.txt&slt=pm&uta=0&rtype=1&iv=0&isw=0&dp-logid=6433134671485730120&dp-callid=0.1.1
#
class WayOne(object):
    def __init__(self):
        pass
    def predict(self):
        pass
    def accuracy(self):
        pass

    @staticmethod
    def getdata():
        #TODO:private method
        '''

        :return[[qishu,riqi,r1,r2,r3,r4,r5,r6,b1],...] or []:
        '''
        data = []
        for item in RbData.objects.all():
            data.append([item.qishu,item.riqi.__str__(),item.r1,item.r2,item.r3,
                        item.r4,item.r5,item.r6,item.b1])
        return tuple(data)