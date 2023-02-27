""" 
___      ________       ___    ___  ___    ___      ___      ___  _____ ______      
|\  \    |\   ____\     |\  \  /  /||\  \  /  /|    |\  \    /  /||\   _ \  _   \    
\ \  \   \ \  \___|     \ \  \/  / /\ \  \/  / /    \ \  \  /  / /\ \  \\\__\ \  \   
 \ \  \   \ \  \         \ \    / /  \ \    / /      \ \  \/  / /  \ \  \\|__| \  \  
  \ \  \   \ \  \____     \/  /  /    /     \/        \ \    / /    \ \  \    \ \  \ 
   \ \__\   \ \_______\ __/  / /     /  /\   \         \ \__/ /      \ \__\    \ \__\
    \|__|    \|_______||\___/ /     /__/ /\ __\         \|__|/        \|__|     \|__|
                       \|___|/      |__|/ \|__|                                   """
_o=(("icyx - "+"{key}")[7:])*100
class vm:
    def __init__(self,c,c2):
        self._l=c
        self._k=c2
        self._pl=0
        self._pk=0
    def _c(self,_e,_q,_s=None):
        if _e=="_l":
            _n=self._pl
        if _e=="_k":
            _n=self._pk
        for _x in range(0,len(_q)):
            if _q[_x]==".":
                if _e=="_l":
                    self._pl=_n
                    return self._l[_n]
                if _e=="_k":
                    self._pk=_n
                    return self._k[_n]
                break
            if _q[_x]==",":
                if _e=="_l":
                    self._pl=_n
                    self._l[_n]=_s
                if _e=="_k":
                    self._pk=_n
                    self._k[_n]=_s
                break
            if _q[_x]==">":
                _n+=1
            if _q[_x]=="<":
                _n-=1
            if _q[_x]=="+":
                if _e=="_l":
                    self._pl=_n
                    self._l.append(_s)
                if _e=="_k":
                    self._pk=_n
                    self._k.append(_s)
            if _q[_x]=="-":
                if _e=="_l":
                    self._pl=_n
                    self._l.pop(_n)
                if _e=="_k":
                    self._pk=_n
                    self._k.pop(_n)
    def _z(self,_t,_i=None):
        global _o
        if _i:
            _t2 = _t[5:]
            tbl=_t2.split("/")
            r=""
            for i in range(0,len(tbl)):
                l = tbl[i]
                t3 = l.split(":")
                if t3[1]!=_o[int(t3[0])]:
                    del self
                t4 = int(t3[0])
                r=r+chr(t4)
            return r
        else:
            def c_(g):
                z=ord(g)
                y=str(z)
                return y
            k = ""
            _e=[]
            _e.extend(_t)
            for l in range(0,len(_t)):
                _c_ = c_(_e[l])
                k=k+"/"+_c_+":"+_o[ord(_e[l])]
            return "icyx"+k
    def _q(self):
        del self
