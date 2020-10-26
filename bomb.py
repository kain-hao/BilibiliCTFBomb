from random import sample
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json
dic = list('abcdef1234567890')

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
	"Cookie": "bsource=search_baidu;\
		_uuid=F6769D03-B03C-0CC-F64B-9C397605C1E103882infoc;\
		buvid3=4CCF0EA0-F24-47D7-AF50-65885BE70247143093infoc;\
		sid=aprw6f7;\
		DedeUserID=288***541;\
		DedeUserID__1ca9be367de13b1;\
		SESSDATA=c559160a,161746818,03625*a1;\
		bp_t_offset_28815841=449702020999812692;\
		bili_jct=c259d9dfaf9020e691d9e9d52e260cc3;\
		bp_video_offset_28815854=449698713870780522;\
		CURRENT_FNVAL=0;\
		LIVE_BUVID=AUTO101619950254148;\
		blackside_state=1;\
		rpdid=|(um|J~k)JJ0J'uY|k|RR))R;\
		sid=ae015bv;\
		PVID=;",
    #Cookie里每个都删过了不要想用我的跑了（
	"Referer":"https://security.bilibili.com/sec1024/",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-origin",
	"Content-Type": "application/json;charset=UTF-8",
	"Origin": "https://security.bilibili.com",
	"Accept": "application/json, text/plain, */*",}

while True:
	flag = ''.join(sample(dic,8)) +'-'+ ''.join(sample(dic,8))+'-'+ ''.join(sample(dic,8))+'-'+ ''.join(sample(dic,8))
	data = {"flag":flag,"ctf_id":6}
	res = requests.post("https://security.bilibili.com/sec1024/api/v1/flag",headers=headers,data=json.dumps(data),verify=False)
	#print(flag+" ------> "+res.text)
	if res.text == '{"code":200,"msg":"Flag错误，请继续努力"}':
		print(flag+" ------> "+res.text)
	elif res.text == '{"code":500,"msg":"请勿频繁提交."}':
		print(flag+" ------> "+res.text)
	elif res.text != '{"code":200,"msg":"Flag错误，请继续努力"}' and res.text !='{"code":500,"msg":"请勿频繁提交."}':
		print(res.text)
		with open("flag6.txt",'w+') as fo:
			fo.write(flag)
		print("成功"+flag)
		break
