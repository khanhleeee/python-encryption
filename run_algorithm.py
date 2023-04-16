import algorithms.ceasar as Caesar

def Run(type, algorithm, text, key):

   if(type == "Mã hoá"):
      match algorithm:
         case "Caesar":
            return runCaesar(text, key) 

def runCaesar(text, key):
   return Caesar.MaHoa(text, key)


