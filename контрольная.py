with open("C:/Users/Aternius/Desktop/quotes.txt", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
      cells = line.split('—')
      len_cells = cells[1].split (' ')
    # len2_cells = 
      dlina = len_cells [1]
      if int(cells [1]) <= 10:
          if int(dlina) < 5:
              print (cells)
          
# программа выдала ошибку ValueError: invalid literal for int() with base 10:
#' Георгий Гачев, «Плюсы и минусы наивного философствования»\n', смысл которой я так и не понял.
#for x in cells:
 #       len_lines += 1
  #      dlina = len(x.split())
   #     
    #    if dlina <= 10 :
     #       if first_word < 5 :
      #          print (lines)

        
