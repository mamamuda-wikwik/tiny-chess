import sys,os,json,urllib.request
V=[0,100,320,330,500,900,0,0,0,100,320,330,500,900,0]
PM=[0,0,0,0,0,0,0,0,5,10,10,-20,-20,10,10,5,5,-5,-10,0,0,-10,-5,5,0,0,0,20,20,0,0,0,5,5,10,25,25,10,5,5,10,10,20,30,30,20,10,10,50,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0]
PE=[0,0,0,0,0,0,0,0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,50,50,50,50,50,50,50,50,80,80,80,80,80,80,80,80,0,0,0,0,0,0,0,0]
NM=[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,5,5,0,-20,-40,-30,5,10,15,15,10,5,-30,-30,0,15,20,20,15,0,-30,-30,5,15,20,20,15,5,-30,-30,0,10,15,15,10,0,-30,-40,-20,0,0,0,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
BM=[-20,-10,-10,-10,-10,-10,-10,-20,-10,5,0,0,0,0,5,-10,-10,10,10,10,10,10,10,-10,-10,0,10,10,10,10,0,-10,-10,5,5,10,10,5,5,-10,-10,0,5,10,10,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-10,-10,-10,-10,-20]
RM=[0,0,0,5,5,0,0,0,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,5,10,10,10,10,10,10,5,0,0,0,0,0,0,0,0]
QM=[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,5,0,0,0,0,-10,-10,5,5,5,5,5,0,-10,0,0,5,5,5,5,0,-5,-5,0,5,5,5,5,0,-5,-10,0,5,5,5,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20]
KM=[20,30,10,0,0,10,30,20,20,20,0,0,0,0,20,20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30]
KE=[-50,-30,-30,-30,-30,-30,-30,-50,-30,-30,0,0,0,0,-30,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-20,-10,0,0,-10,-20,-30,-50,-40,-30,-20,-20,-30,-40,-50]
MG=[0,PM,NM,BM,RM,QM,KM]
EG=[0,PE,NM,BM,RM,QM,KE]
PP=[0,0,10,20,35,60,100,0]
NO=[33,18,-14,-31,-33,-18,14,31]
KO=[1,17,16,15,-1,-17,-16,-15]
DO=[17,15,-17,-15]
RO=[1,16,-1,-16]
B=[0]*128
T=0
C=0
E=-1
H=0
K=[4,116]
TT={}
KL=[[0,0] for _ in range(128)]
HI=[0]*1920
N=0
BUD=150000
GH=set()
HP=[]
class AB(Exception):pass
def fen(s):
    global B,T,C,E,H,K
    B=[0]*128;T=0;C=0;E=-1;H=0;K=[4,116]
    p=s.split()
    r=7;f=0
    for ch in p[0]:
        if ch=='/':r-=1;f=0
        elif ch.isdigit():f+=int(ch)
        else:
            q=(r<<4)|f
            d={'P':1,'N':2,'B':3,'R':4,'Q':5,'K':6,'p':9,'n':10,'b':11,'r':12,'q':13,'k':14}[ch]
            B[q]=d
            if d==6:K[0]=q
            if d==14:K[1]=q
            f+=1
    T=0 if p[1]=='w' else 8
    if len(p)>2:
        for ch in p[2]:
            if ch=='K':C|=1
            elif ch=='Q':C|=2
            elif ch=='k':C|=4
            elif ch=='q':C|=8
    if len(p)>3 and p[3]!='-':
        E=(ord(p[3][0])-97)|((int(p[3][1])-1)<<4)
    if len(p)>4:H=int(p[4])
def atk(s,by):
    if by==0:
        t=s-15
        if not(t&0x88) and B[t]==1:return 1
        t=s-17
        if not(t&0x88) and B[t]==1:return 1
    else:
        t=s+15
        if not(t&0x88) and B[t]==9:return 1
        t=s+17
        if not(t&0x88) and B[t]==9:return 1
    for o in NO:
        t=s+o
        if not(t&0x88) and B[t]==(2|by):return 1
    for o in KO:
        t=s+o
        if not(t&0x88) and B[t]==(6|by):return 1
    for o in DO:
        t=s+o
        while not(t&0x88):
            q=B[t]
            if q:
                if q==(3|by) or q==(5|by):return 1
                break
            t+=o
    for o in RO:
        t=s+o
        while not(t&0x88):
            q=B[t]
            if q:
                if q==(4|by) or q==(5|by):return 1
                break
            t+=o
    return 0

def gen(cp):
    L=[];b=B;t=T;e=E
    for f in range(128):
        if f&0x88:continue
        p=b[f]
        if not p or (p&8)!=t:continue
        y=p&7
        if y==1:
            d=16 if t==0 else -16
            u=f+d
            if not(u&0x88) and not b[u]:
                pm=(t==0 and u>=112) or (t and u<8)
                if pm:
                    for r in (5,4,3,2):L.append(f|(u<<7)|(r<<14))
                elif not cp:
                    L.append(f|(u<<7))
                    if ((t==0 and 16<=f<24) or (t and 96<=f<104)) and not b[f+2*d]:L.append(f|((f+2*d)<<7))
            for u in (f+d-1,f+d+1):
                if u&0x88:continue
                if (b[u] and (b[u]&8)!=t) or u==e:
                    pm=(t==0 and u>=112) or (t and u<8)
                    if pm:
                        for r in (5,4,3,2):L.append(f|(u<<7)|(r<<14))
                    else:L.append(f|(u<<7))
        elif y==2:
            for o in NO:
                u=f+o
                if not(u&0x88) and b[u] and (b[u]&8)!=t:L.append(f|(u<<7))
                elif not cp and not(u&0x88) and not b[u]:L.append(f|(u<<7))
        elif y==6:
            for o in KO:
                u=f+o
                if not(u&0x88) and b[u] and (b[u]&8)!=t:L.append(f|(u<<7))
                elif not cp and not(u&0x88) and not b[u]:L.append(f|(u<<7))
            if not cp:
                if t==0:
                    if C&1 and not b[5] and not b[6] and not atk(4,8) and not atk(5,8) and not atk(6,8):L.append(4|(6<<7))
                    if C&2 and not b[3] and not b[2] and not b[1] and not atk(4,8) and not atk(3,8) and not atk(2,8):L.append(4|(2<<7))
                else:
                    if C&4 and not b[117] and not b[118] and not atk(116,0) and not atk(117,0) and not atk(118,0):L.append(116|(118<<7))
                    if C&8 and not b[115] and not b[114] and not b[113] and not atk(116,0) and not atk(115,0) and not atk(114,0):L.append(116|(114<<7))
        else:
            oo=DO if y==3 else RO if y==4 else DO+RO
            for o in oo:
                u=f+o
                while not(u&0x88):
                    q=b[u]
                    if q:
                        if (q&8)!=t:L.append(f|(u<<7))
                        break
                    if not cp:L.append(f|(u<<7))
                    u+=o
    return L
U=[]
def mk(m):
    global T,C,E,H
    f=m&127;t=(m>>7)&127;r=(m>>14)&7
    p=B[f];q=B[t];cs=t
    if (p&7)==1 and t==E and not q:
        cs=t-16 if T==0 else t+16
        q=B[cs];B[cs]=0
    U.append((m,q,cs,C,E,H))
    B[t]=(r|T) if r else p;B[f]=0
    if (p&7)==6:
        K[T>>3]=t
        if abs(t-f)==2:
            if t>f:B[t-1]=B[t+1];B[t+1]=0
            else:B[t+1]=B[t-2];B[t-2]=0
    if (p&7)==6:C&=12 if T==0 else 3
    if f==0:C&=~2
    elif f==7:C&=~1
    elif f==112:C&=~8
    elif f==119:C&=~4
    if t==0:C&=~2
    elif t==7:C&=~1
    elif t==112:C&=~8
    elif t==119:C&=~4
    E=(f+16 if T==0 else f-16) if (p&7)==1 and abs(t-f)==32 else -1
    H=0 if (p&7)==1 or q else H+1
    T^=8
def un():
    global T,C,E,H
    m,q,cs,c2,e2,h2=U.pop()
    f=m&127;t=(m>>7)&127;r=(m>>14)&7
    T^=8
    p=B[t]
    if (p&7)==6:
        K[T>>3]=f
        if abs(t-f)==2:
            if t>f:B[t+1]=B[t-1];B[t-1]=0
            else:B[t-2]=B[t+1];B[t+1]=0
    B[f]=(1|T) if r else p
    B[t]=0
    if q:B[cs]=q
    C,E,H=c2,e2,h2

def ev():
    mg=0;eg=0;ph=0;wp=[];bp=[];wb=0;bb=0
    for s in range(128):
        if s&0x88:continue
        p=B[s]
        if not p:continue
        y=p&7;w=1 if not(p&8) else -1
        i=(s&7)|((s>>4)<<3)
        if p&8:i^=56
        mg+=w*(V[y]+MG[y][i]);eg+=w*(V[y]+EG[y][i])
        if y>1 and y<6:ph+=(1,1,2,4)[y-2] if y<5 else 4
        if y==1:
            if p&8:bp.append(s)
            else:wp.append(s)
        elif y==3:
            if p&8:bb+=1
            else:wb+=1
    if ph>24:ph=24
    s=(mg*ph+eg*(24-ph))//24
    if wb>1:s+=25
    if bb>1:s-=25
    for q in wp:
        f=q&7;r=q>>4;ok=1
        for z in bp:
            if abs((z&7)-f)<2 and (z>>4)>r:ok=0;break
        if ok:s+=PP[r]
    for q in bp:
        f=q&7;r=q>>4;ok=1
        for z in wp:
            if abs((z&7)-f)<2 and (z>>4)<r:ok=0;break
        if ok:s-=PP[7-r]
    return s if T==0 else -s

def qs(a,b,pl,qd):
    global N
    N+=1
    if N>BUD:raise AB
    if qd>8:return ev()
    s=ev()
    if s>=b:return b
    if s>a:a=s
    wd=atk(K[T>>3],T)
    ms=gen(0) if qd==0 and wd else gen(1)
    sc=[]
    for m in ms:
        t=(m>>7)&127;v=B[t]
        sc.append((V[v&7]*16-V[B[m&127]&7] if v else 0,m))
    sc.sort(reverse=True)
    c=0
    for _,m in sc:
        mk(m)
        if atk(K[(T^8)>>3],T):
            un();continue
        c+=1
        v=-qs(-b,-a,pl+1,qd+1)
        un()
        if v>=b:return b
        if v>a:a=v
    if qd==0 and wd and not c:return -29999+pl if atk(K[T>>3],T^8) else 0
    return a
BM=0
def sr(a,b,d,pl):
    global N,BM
    N+=1
    if N>BUD:raise AB
    if H>=100:return 0
    key=(bytes(B),T,C,E)
    if key in HP or key in GH:return 0
    if d<=0:return qs(a,b,pl,0)
    e=TT.get(key)
    if e and e[0]>=d:
        s=e[1];f=e[2]
        if f==0:return s
        if f==1 and s>=b:return s
        if f==2 and s<=a:return s
    chk=atk(K[T>>3],T^8)
    ms=gen(0)
    tm=e[3] if e else 0
    sc=[]
    for m in ms:
        f=m&127;t=(m>>7)&127;v=B[t]
        if m==tm:sc.append((1000000,m))
        elif v:sc.append((100000+V[v&7]*16-V[B[f]&7],m))
        elif m==KL[pl][0] or m==KL[pl][1]:sc.append((90000,m))
        else:sc.append((HI[B[f]*128+t],m))
    sc.sort(reverse=True)
    ao=a;best=-30000;bm=0;c=0
    HP.append(key)
    for i,(s0,m) in enumerate(sc):
        f=m&127;t=(m>>7)&127
        cap=B[t]!=0 or (t==E and (B[f]&7)==1)
        pr=(m>>14)&7
        mk(m)
        if atk(K[(T^8)>>3],T):
            un();continue
        c+=1
        if d>=3 and i>2 and not cap and not pr and not chk:
            v=-sr(-b,-a,d-2,pl+1)
            if v>a:v=-sr(-b,-a,d-1,pl+1)
        else:
            v=-sr(-b,-a,d-1,pl+1)
        un()
        if v>best:best=v;bm=m
        if v>a:a=v
        if a>=b:
            if not cap:
                if m!=KL[pl][0]:KL[pl][1]=KL[pl][0];KL[pl][0]=m
                HI[B[f]*128+t]+=d*d
            break
    HP.pop()
    if not c:return -29999+pl if chk else 0
    fl=0
    if best<=ao:fl=2
    elif best>=b:fl=1
    TT[key]=(d,best,fl,bm)
    if pl==0:BM=bm
    return best
def root():
    global N,HP,BM
    HP=[];N=0;BM=0
    if len(TT)>300000:TT.clear()
    for d in range(1,7):
        ob=BM
        try:sr(-30000,30000,d,0)
        except AB:BM=ob;break
    return BM

def u2m(u):
    f=(ord(u[0])-97)|((int(u[1])-1)<<4)
    t=(ord(u[2])-97)|((int(u[3])-1)<<4)
    r=0
    if len(u)>4:r={'n':2,'b':3,'r':4,'q':5}[u[4]]
    return f|(t<<7)|(r<<14)
def m2u(m):
    f=m&127;t=(m>>7)&127
    s=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
    r=(m>>14)&7
    if r:s+='nbrq'[r-2]
    return s
def setup(mvs):
    global GH
    GH=set();U.clear()
    fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    GH.add((bytes(B),T,C,E))
    for i,u in enumerate(mvs):
        mk(u2m(u))
        if i<len(mvs)-1:GH.add((bytes(B),T,C,E))
    U.clear()
def post(u,o):
    q=urllib.request.Request(u,data=json.dumps(o).encode(),headers={'Content-Type':'application/json'})
    return json.loads(urllib.request.urlopen(q).read())
def main():
    u=os.environ['MAKEFUN_ENV_URL']
    while True:
        s=post(u+'/game',{})
        if s.get('status')=='done':break
        if s.get('status')!='your_move':continue
        setup(s['moves'])
        fen(s['fen'])
        m=root()
        if not m or m2u(m) not in s['legal_moves']:m=u2m(s['legal_moves'][0])
        post(u+'/move',{'game':s['game'],'move':m2u(m)})
if __name__=='__main__':main()
