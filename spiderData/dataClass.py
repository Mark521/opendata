#coding=utf-8

import jieba
import re


class Data:
    """
       这是保存数据描述的类，保存包括数据来源，数据种类，数据名称等信息
    """
    def __init__(self, source, dataType, name, place):
        self.source = source
        self.dataType = dataType
        self.name = name
        self.place = place

    def printInfo(self):
        print(u"数据来源"+self.source+u"数据种类"+self.dataType+u"数据名称"+self.name)
    

class ShangHai(Data):
    """这是保存上海数据开放平台数据的增加了部门主题的属性"""

    def __init__(self, source, dataType, name, department):
        self.source = source
        self.dataType = dataType
        self.name = name
        self.department = department


class EntryData(Data):
    """
    用来保存数据条目信息，包括关键字和匹配度,分词长度,数据来源,数据分类, 城市
    """
    exc = ['武汉市','上海市', '北京市','中心', '单位','企业', '生产', '许可', '机构', '10','11','12','2008','2009','2010','2011','2012','2013','2014','2015','2016','总', '新', '9', '：', '、', '井', '”', ';', '行', '数', '口', '卫', '前', '获', '占', '季', '全', '各', '线', '+', '权', '县', '补', ' ', '闸', '队', '&', '预', '路', '山', '含', '—', '号', '值', '(', '人', '8', '_', '等', '台', '5', '板', '京', '标', '上', '户', ')', '到', '首', '副', '或', '代', '邾', '较', '支', '赴', '镇', '合', '/', '食', '地', '步', '期', '表', '额', '云', '宗', '中', '㎡', '公', '个', '微', '有', '点', '者', '万', '证', '项', '春', '房', '7', '-', '的', '沪', '内', '在', '店', '类', '别', 'i', '厅', '存', '会', '快', '州', '电', '按', '"', '库', '机', '和', '馆', '2', '处', '属', '可', '院', '》', '段', ',', '池', '林', '经', '所', '位', '场', '后', '受', '街', '门', '%', '对', '法', '3', '投', '水', '汽', '第', '至', '6', '园', '走', '站', '病', '外', '办', '五', '比', '超', '村', '均', '卡', '非', '道', '1', '过', '巷', '月', '临', '物', '议', '被', '）', '包', '驻', '城', '业', '酒', 'A', '老', '嘴', '暨', '\t', 'C', '，', '（', '下', '区', '日', '学', '折', '一', '年', '与', '已', '长', '件', '政', '每', '现', '4', '鱼', '单', '未', '市', '奖', '界', '《', '木', '报', '局', '域', '家', '图', '大', '二', '箱', '委', '性', '圈', '量', '高', '“', '通', '拟', '起', '气', '车', '岗', '省', '级', '免', '分', '向', '字', '型', '及', '用', '室', '汉', '不']
    
    def __init__(self):
        Data.__init__(self,'', '', '', '')
        self.dataList = []
        self.size = len(self.dataList)
        self.matchNum = 0

    def setFromData(self, data):
        Data.__init__(self,data.source, data.dataType, data.name, data.place)
        temp = set(jieba.cut(data.name))
        for each in self.exc:
            if each in temp:
                temp.remove(each)
        self.dataList = temp
        self.size = len(self.dataList)
        self.matchNum = 0

    def setFromString(self, source, dataType, name, place):
        Data.__init__(self,source, dataType, name, place)
        temp = set(jieba.cut(name))
        for each in self.exc:
            if each in temp:
                temp.remove(each)
        self.dataList = temp
        self.size = len(self.dataList)
        self.matchNum = 0
    
    #用于与给定数据进行匹配
    def match(self, data):
        matchStr = []
        dataList = list(self.dataList)
        for each in dataList:
            temp = '.*'.join(each)
            regex = re.compile(temp)
            matchStr.append(regex)
        for each in matchStr:
            flag = None
            for item in data:
                flag = each.search(item)
                if flag:
                    self.matchNum = self.matchNum+1
        #print(self.name + '--->匹配结束')

    #使用对象进行匹配
    def matchWithEntry(self, data):
        ll = list(data.dataList)
        self.matchNum = 0
        self.match(ll)
        return self.getMatchNum(),self.getSize()

    
    #若匹配成功，输出匹配关键字
    def printMatch(self, data):
        ll = list(data.dataList)
        self.matchPrint(ll)
    def matchPrint(self, data):
        matchStr = []
        dataList = list(self.dataList)
        for each in dataList:
            temp = '.*'.join(each)
            regex = re.compile(temp)
            matchStr.append(regex)
        for each in matchStr:
            flag = None
            for item in data:
                flag = each.search(item)
                if flag:
                    print('<', each ,'--',item ,'>')
        #print(self.name + '--->匹配结束')
    
    #将当前类数据转换为列表形式存储
    def toList(self):
        sList = []
        sList.insert(0, self.name)
        sList.insert(1, self.dataList)
        sList.insert(2, self.size)
        sList.insert(3, self.matchNum)
        sList.insert(4, self.source)
        sList.insert(5, self.dataType)
        sList.insert(6, self.place)
        return sList

    #获取数据来源
    def getSource(self):
        return self.source

    #获取数据种类
    def getDataType(self):
        return self.dataType

    #获取数据城市
    def getPlace(self):
        return self.place

    #获取关键字个数
    def getSize(self):
        return self.size

    #获取匹配个数
    def getMatchNum(self):
        return self.matchNum

    #获取关键字
    def getDataList(self):
        return list(self.dataList)

    def getData(self):
        return Data(self.source, self.dataType, self.name, self.place)
        





        
