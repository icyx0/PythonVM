""" 
___      ________       ___    ___  ___    ___      ___      ___  _____ ______      
|\  \    |\   ____\     |\  \  /  /||\  \  /  /|    |\  \    /  /||\   _ \  _   \    
\ \  \   \ \  \___|     \ \  \/  / /\ \  \/  / /    \ \  \  /  / /\ \  \\\__\ \  \   
 \ \  \   \ \  \         \ \    / /  \ \    / /      \ \  \/  / /  \ \  \\|__| \  \  
  \ \  \   \ \  \____     \/  /  /    /     \/        \ \    / /    \ \  \    \ \  \ 
   \ \__\   \ \_______\ __/  / /     /  /\   \         \ \__/ /      \ \__\    \ \__\
    \|__|    \|_______||\___/ /     /__/ /\ __\         \|__|/        \|__|     \|__|
                       \|___|/      |__|/ \|__|                                   """
_o=("icyx - "+"{key}"*100)[7:]
class vm:
    def __init__(self,c,c2):
        self._l=c
        self._k=c2
    def _c(self,_e,_q,_s=None):
        _n=0
        for _x in range(0,len(_q)):
            if _q[_x]==".":
                if _e=="_l":
                    return self._l[_n]
                if _e=="_k":
                    return self._k[_n]
                break
            if _q[_x]==",":
                if _e=="_l":
                    self._l[_n]=_s
                if _e=="_k":
                    self._k[_n]=_s
                break
            if _q[_x]==">":
                _n+=1
            if _q[_x]=="<":
                _n-=1
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
