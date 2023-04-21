import algorithms.ceasar as Caesar
import algorithms.chuyenvihaidong as ChuyenVi2Dong
import algorithms.chuyenvinhieudong as ChuyenViNhieuDong

def Run(type, algorithm, text, key):

   if(type == "Mã hoá"):
      match algorithm:
         case "Caesar":
             return Caesar.MaHoa(text, key)
         case "Chuyển vị 2 dòng":
             return ChuyenVi2Dong.MaHoa(text)
         case "Chuyển vị nhiều dòng":
             return ChuyenViNhieuDong.MaHoa(text, key)
   else:
      match algorithm:
         case "Caesar":
             return Caesar.GiaiMa(text, key)
         case "Chuyển vị 2 dòng":
             return ChuyenVi2Dong.GiaiMa(text)
         case "Chuyển vị nhiều dòng":
             return ChuyenViNhieuDong.GiaiMa(text, key)
  


