#实现对数据条目的模糊匹配算法
def handerMacth(i, j):
    return i == j
    
def cal(csrc, i, cdest, j , hander, curdeep, maxdeep):
    score = 0
    lenCsrc = len(csrc)
    lenCdest = len(cdest)
    if curdeep > maxdeep or i >=lenCsrc or j >= lenCdest:
        return 0
    ismatch = hander.compare(csrc[i], cdest[j])
    if ismatch:
        score += 1
        if i + 1 < lenCsrc and j + 1 <lenCdest:
            score += cal(csrc, i+1, cdest, j+1, hander, 0, maxdeep)
    else:
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp1 += cal(csrc, i, cdest, j+1, hander, curdeep+1, maxdeep)
        temp2 += cal(csrc, i+1, cdest, j, hander, curdeep+1, maxdeep)
        temp3 += cal(csrc, i+1, cdest, j+1, hander, curdeep+1, maxdeep)
        score += max(temp1, temp2, temp3)
    return score

def matchS(percent, src, dest, hander):
    score = 0
    maxLen = max(len(src), len(dest))
    score = cal(src, 0, dest,0, hander,0, int((1- percent)*maxLen))
    #print("最小匹配百分比："+str(percent)+"，成功匹配百分比："+str(score / maxLen))
    return score / len(src) > percent
    
def matchF(percent, src, dest):
    return matchS(percent, src, dest, MatchHander())
        

class MatchHander:
    def compare(self,a, b):
        return a == b


print(matchF(0.74, '食品相关产品生产许可获证企业信息', '食品及相关产品许可证获证企业'))
"""for d in bjdata:
	for a in shdata:
		if matchF(0.618, d, a) == True:
			print(d, a)
bjdata = [e.name for e in entryBJ]"""
