import algorithms.ceasar as Caesar

def Run(type, algorithm, text, key):

   if(type == "Mã hoá"):
      match algorithm:
         case "Caesar":
             return Caesar.MaHoa(text, key)
   else:
      match algorithm:
         case "Caesar":
             return Caesar.GiaiMa(text, key)

  


