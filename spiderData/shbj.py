Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\audaque\AppData\Local\Temp\jieba.cache
Loading model cost 1.119 seconds.
Prefix dict has been built succesfully.
>>> bjjg = []
>>> shjg
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    shjg
NameError: name 'shjg' is not defined
>>> shjg = []
>>> whjg = []
>>> shjg = set(bjjg)
>>> type(shjg)
<class 'set'>
>>> for e in entryBJ:
	shjg.add(e.source)

	
>>> e.size()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    e.size()
TypeError: 'int' object is not callable
>>> len(shjg)
39
>>> whjg  = set(whjg)
>>> shjg = set(shjg)
>>> bjjg = []
>>> shjg = []
>>> whjg = []
>>> bjjg = set(bjjg)
>>> shjg = set(shjg)
>>> whjg = set(whjg)
>>> for e in entryBJ:
	bjjg.add(e.source)

	
>>> for e in entrySH:
	shjg.add(e.source)

	
>>> for e in entryWH:
	whjg.add(e.source)

	
>>> len(whjg)
89
>>> len(shjg)
43
>>> len(bjjg)
39
>>> print(whjg)
{'市旅游局', '武昌区', '市妇联', '市安全生产监督管理局', '市公安局', '市教育局', '市民防办公室', '市司法局', '市地铁集团', '武汉住房公积金管理中心', '市国有资产监督管理委员会', '市政服务中心管理办公室', '武汉新港管委会', '市纪委', '武汉海关', '市审计局', '市文联', '江汉区', '市委宣传部', '市工商行政管理局', '武汉市城市路桥收费中心', '市财政局', '市文化局', '青山区', '市住房保障和房屋管理局', '市交管局', '粮食局', '市金融工作局', '市国土资源和规划局', '市政府参事室', '市园林和林业局', '市监察局', '市农业委员会', '市国税局', '市科协', '市卫生和计划生育委员会', '市委党校（武汉行政学院）', '江夏区', '市统计局', '市网信办', '市水务集团', '市环境保护局', '东湖生态旅游风景区管委会', '洪山区', '武汉临空港经济技术开发区管委会(东西湖)', '市体育局', '武汉化学工业区管委会', '贸促会武汉分会', '市外事办公室', '武汉共青团', '市老干部局', '市委市直机关工委', '汉阳区', '市食品药品监督管理局', '市编办', '东湖新技术开发区管委会', '市商务局', '江岸区', '市经济和信息化委员会', '市人力资源和社会保障局', '市政协', '市发展和改革委员会', '市质量技术监督局', '市工商联', '市人大', '市民政局', '市法院', '市城乡建设委员会', '市燃气热力集团', '市城市管理委员会', '市地税局', '市侨联', '市总工会', '市档案局', '市法制办公室', '市公交集团', '蔡甸区', '市科学技术局', '新洲区', '市文明办', '市民族宗教事务委员会', '汉南区', '黄陂区', '残疾人联合会', '硚口区', '市红十字会', '武汉经济技术开发区管委会', '市交通运输委员会', '市水务局'}
>>> bjentry = []
>>> shentry = []
>>> whentry = []
>>> for e in whjg:
	temp = EntryData()
	temp.setFromString('', '机构', e, 'WH')

	
>>> for e in whjg:
	temp = EntryData()
	temp.setFromString('', '机构', e, 'WH')
	whentry.append(temp)

	
>>> for e in shjg:
	temp = EntryData()
	temp.setFromString('', '机构', e, 'WH')
	shentry.append(temp)

	
>>> for e in bjjg:
	temp = EntryData()
	temp.setFromString('', '机构', e, 'WH')
	bjentry.append(temp)

	
>>> match1, match2 = matchList(bjentry, whentry)
>>> match3, match4 = matchList(whentry, bjentry)
>>> ll = []
>>> for e in range(len(match1))
SyntaxError: invalid syntax
>>> for e in range(len(match1)):
	temp = []
	temp.insert(0,match1.name)
	temp.insert(1,match2.name)
	ll.append(temp)

	
Traceback (most recent call last):
  File "<pyshell#58>", line 3, in <module>
    temp.insert(0,match1.name)
AttributeError: 'list' object has no attribute 'name'
>>> match1
[<dataClass.EntryData object at 0x06285D50>, <dataClass.EntryData object at 0x06285DB0>, <dataClass.EntryData object at 0x06285DF0>, <dataClass.EntryData object at 0x06285E10>, <dataClass.EntryData object at 0x06285E70>, <dataClass.EntryData object at 0x06285EF0>, <dataClass.EntryData object at 0x06285F90>, <dataClass.EntryData object at 0x062857F0>, <dataClass.EntryData object at 0x0628D050>, <dataClass.EntryData object at 0x0628D0F0>, <dataClass.EntryData object at 0x0628D130>, <dataClass.EntryData object at 0x0628D1B0>, <dataClass.EntryData object at 0x0628D1D0>]
>>> for e in range(len(match1)):
	temp = []
	temp.insert(0,match1[e].name)
	temp.insert(1,match2[e].name)
	ll.append(temp)

	
>>> for e in range(len(match3)):
	temp =
	
SyntaxError: invalid syntax
>>> lll = []
>>> for e in range(len(match3)):
	temp = []
	temp.insert(0,match4[e].name)
	temp.insert(1,match3[e].name)
	lll.append(temp)

	
>>> lll
[['市公安局', '市公安局'], ['市民防局', '市民防办公室'], ['市司法局', '市司法局'], ['市文化局', '市文化局'], ['市科协', '市科协'], ['市体育局', '市体育局'], ['市民政局', '市民政局'], ['市档案局', '市档案局'], ['市水务局', '市水务局']]
>>> ll
[['市质监局', '市质量技术监督局'], ['市档案局', '市档案局'], ['市公安局', '市公安局'], ['市环保局', '市环境保护局'], ['市司法局', '市司法局'], ['市社会办', '市人力资源和社会保障局'], ['市科协', '市科协'], ['市民政局', '市民政局'], ['市药监局', '市食品药品监督管理局'], ['市民委', '市民防办公室'], ['市文化局', '市文化局'], ['市水务局', '市水务局'], ['市体育局', '市体育局']]
>>> ll = []
>>> for e in range(len(match1)):
	temp = []
	temp.insert(0,match1[e].name)
	temp.insert(1,match2[e].name)
	ll.append(temp)

	
>>> lll = []
>>> for e in range(len(match3)):
	temp = []
	temp.insert(0,match4[e].name)
	temp.insert(1,match3[e].name)
	lll.append(temp)

	
>>> for e in lll:
	print(e)

	
['市公安局', '市公安局']
['市民防局', '市民防办公室']
['市司法局', '市司法局']
['市文化局', '市文化局']
['市科协', '市科协']
['市体育局', '市体育局']
['市民政局', '市民政局']
['市档案局', '市档案局']
['市水务局', '市水务局']
>>> len(match1)
13
>>> ll
[['市质监局', '市质量技术监督局'], ['市档案局', '市档案局'], ['市公安局', '市公安局'], ['市环保局', '市环境保护局'], ['市司法局', '市司法局'], ['市社会办', '市人力资源和社会保障局'], ['市科协', '市科协'], ['市民政局', '市民政局'], ['市药监局', '市食品药品监督管理局'], ['市民委', '市民防办公室'], ['市文化局', '市文化局'], ['市水务局', '市水务局'], ['市体育局', '市体育局']]
>>> xx = [a for x in ll :x in lll]
SyntaxError: invalid syntax
>>> xx = [a for x in ll if x in lll]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    xx = [a for x in ll if x in lll]
  File "<pyshell#81>", line 1, in <listcomp>
    xx = [a for x in ll if x in lll]
NameError: name 'a' is not defined
>>> xx = [x for x in ll if x in lll]
>>> xx
[['市档案局', '市档案局'], ['市公安局', '市公安局'], ['市司法局', '市司法局'], ['市科协', '市科协'], ['市民政局', '市民政局'], ['市文化局', '市文化局'], ['市水务局', '市水务局'], ['市体育局', '市体育局']]
>>> 
