#coding:utf-8
'''
selenium help function
'''
#高亮显示方便定位元素
def high_light(dr,ele):
	dr.execute_script("arguments[0].style.border = '2px solid red'",ele)