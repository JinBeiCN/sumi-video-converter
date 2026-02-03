import os,sys,subprocess as sp
from pathlib import Path as P
C={'w':454,'h':454,'f':30,'b':'2M','o':'bg.mp4','e':32}

class V:
 def __init__(s):s.f=s.cf()
 @staticmethod
 def cf():
  try:sp.run(["ffmpeg","-v"],o=sp.PIPE,e=sp.PIPE,c=1);return 1
  except:return 0
 def cv(s,i,o):
  if not s.f:print("⚠️ 无ffmpeg");return 0
  print(f"🎬 转:{i}")
  cmd=['ffmpeg','-i',i,'-vf',f'scale={C["w"]}:{C["h"]}:force_original_aspect_ratio=decrease,pad={C["w"]}:{C["h"]}:(ow-iw)/2:(oh-ih)/2','-r',str(C['f']),'-b:v',C['b'],'-c:v','libx264','-preset','medium','-movflags','+faststart','-y',o]
  try:
   r=sp.run(cmd,o=sp.PIPE,e=sp.PIPE,t=1)
   if r.rc==0:print(f"✅ 成功:{o}");return 1
   else:print(f"❌ 失败:{r.stderr}");return 0
  except Exception as e:print(f"❌ 错误:{e}");return 0
 @staticmethod
 def ef(i,o):
  try:
   with open(i,'rb')as f:d=bytearray(f.read())
   for i in range(min(C['e'],len(d))):d[i]^=i
   with open(o,'wb')as f:f.write(d)
   print(f"🔒 加密:{o}");return 1
  except Exception as e:print(f"❌ 失败:{e}");return 0
 @staticmethod
 def df(i,o):return V.ef(i,o)

class B:
 def __init__(s):s.p=V()
 def gv(s,d):
  e={'.mp4','.avi','.mov','.mkv','.flv','.wmv'}
  return[str(f)for f in P(d).iterdir()if f.suffix in e]
 def be(s,f,o):
  os.makedirs(o,e=1)
  c=0
  for x in f:
   if s.p.ef(x,os.path.join(o,P(x).name)):c+=1
  print(f"✅ 加密:{c}/{len(f)}")
 def bd(s,f,o):
  os.makedirs(o,e=1)
  c=0
  for x in f:
   n=P(x).stem+'_d'+P(x).suffix
   if s.p.df(x,os.path.join(o,n)):c+=1
  print(f"✅ 解密:{c}/{len(f)}")
 def sv(s,i,c=1):
  b=P(i).parent
  t=b/'temp.mp4'
  o=b/C['o']
  if c and s.p.f:
   if not s.p.cv(i,str(t)):t=P(i)
  else:t=P(i)
  if s.p.ef(str(t),str(o)):
   if t.name=='temp.mp4'and t.exists():t.unlink()
   print(f"🎉 完成:{o}")
  else:print("❌ 失败")

def pm():print("\n[1]单处理 [2]批加密 [3]批解密 [4]仅转换 [5]配置 [0]退出")

def ec():
 print(f"\n分辨率:{C['w']}x{C['h']}\n帧率:{C['f']}\n码率:{C['b']}\n输出:{C['o']}")
 if input("修改?(y/n):").lower()=='y':
  try:
   C['w']=int(input(f"宽[{C['w']}]:")or C['w'])
   C['h']=int(input(f"高[{C['h']}]:")or C['h'])
   C['f']=int(input(f"帧率[{C['f']}]:")or C['f'])
   C['b']=input(f"码率[{C['b']}]:")or C['b']
   C['o']=input(f"输出[{C['o']}]:")or C['o']
   print("✅ 配置更新")
  except:print("❌ 输入无效")

def main():
 print("="*60+"\nAndroid表盘视频处理 v1.0\n"+"="*60)
 b=B()
 if not b.p.f:
  print("⚠️ 无ffmpeg\n安装:\n Windows:https://ffmpeg.org/download.html\n Linux:sudo apt install ffmpeg\n macOS:brew install ffmpeg")
  input("\n回车继续")
 while 1:
  pm()
  c=input("选项:").strip()
  if c=='0':print("\n👋 再见");break
  elif c=='1':
   f=input("\n文件路径:").strip().strip('"')
   if not os.path.exists(f):print("❌ 不存在");continue
   cv=input("转换?(y/n)[y]:").lower()!='n'
   b.sv(f,cv)
  elif c=='2':
   d=input("\n目录:").strip().strip('"')
   if not os.path.isdir(d):print("❌ 不存在");continue
   o=input("输出[./encrypted]:")or"./encrypted"
   f=b.gv(d)
   if not f:print("❌ 无文件");continue
   print(f"\n找到{len(f)}个文件")
   for x in f:print(f" -{P(x).name}")
   if input("\n确认?(y/n):").lower()=='y':b.be(f,o)
  elif c=='3':
   d=input("\n目录:").strip().strip('"')
   if not os.path.isdir(d):print("❌ 不存在");continue
   o=input("输出[./decrypted]:")or"./decrypted"
   f=b.gv(d)
   if not f:print("❌ 无文件");continue
   print(f"\n找到{len(f)}个文件")
   for x in f:print(f" -{P(x).name}")
   if input("\n确认?(y/n):").lower()=='y':b.bd(f,o)
  elif c=='4':
   f=input("\n文件路径:").strip().strip('"')
   if not os.path.exists(f):print("❌ 不存在");continue
   o=input(f"输出[{C['o']}]:").strip()or C['o']
   b.p.cv(f,str(P(f).parent/o))
  elif c=='5':ec()
  else:print("❌ 无效")

if __name__=="__main__":
 try:main()
 except KeyboardInterrupt:print("\n👋 退出");sys.exit(0)
 except Exception as e:print(f"\n❌ 错误:{e}");input("回车退出");sys.exit(1)