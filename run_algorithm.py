import algorithms.ceasar as Caesar
import algorithms.vignere as Vignere
import algorithms.belasco as Belasco
import algorithms.trithemius as Trithemius
import algorithms.chuyenvihaidong as ChuyenVi2Dong
import algorithms.chuyenvinhieudong as ChuyenViNhieuDong


def Run(type, algorithm, text, key):

   if(type == "Mã hoá"):
      match algorithm:
         case "Caesar":
            return Caesar.MaHoa(text, key) 
         case "Vignere":
            return Vignere.MaHoa(text, key)
         case "Belasco":
            return Belasco.MaHoa(text, key)
         case "Trithemius":
            return Trithemius.MaHoa(text)
         case "Chuyển vị 2 dòng":
             return ChuyenVi2Dong.MaHoa(text)
         case "Chuyển vị nhiều dòng":
            keyArray = key.split(',')
            keyArray = [int(x) for x in keyArray]
            print("keyArray", keyArray)
            return ChuyenViNhieuDong.MaHoa(text, keyArray)
   else:
      match algorithm:
         case "Caesar":
            return Caesar.GiaiMa(text, key) 
         case "Vignere":
            return Vignere.GiaiMa(text, key)
         case "Belasco":
            return Belasco.GiaiMa(text, key)
         case "Trithemius":
            return Trithemius.GiaiMa(text)
         case "Chuyển vị 2 dòng":
             return ChuyenVi2Dong.GiaiMa(text)
         case "Chuyển vị nhiều dòng":
            keyArray = key.split(',')
            keyArray = [int(x) for x in keyArray]
            return ChuyenViNhieuDong.GiaiMa(text, keyArray)
