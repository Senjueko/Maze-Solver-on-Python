import sys

a = int(sys.argv[3])
def letters(n):
    valids = []
    for character in n:
        if character.isalpha() or character.isdigit() or character == ',':
            valids.append(character)
    return ''.join(valids)


liste = []
liste_h = []

with open(sys.argv[1], 'r', encoding='utf-8-sig') as f:
    def maze():
        liste1 = []
        global liste
        global s
        s = f.readline()
        if s == '':
            return s
        else:
            for i in letters(s):
                liste1.append(i)
            liste.append(liste1)
            return maze()


    maze()

for i in range(len(liste)):
    for q in range(len(liste[0])):
        if liste[i][q] == 'S':
            col, row = int(i), int(q)
            break
with open(sys.argv[2], 'r', encoding='utf-8-sig') as f:
    def maze_1():
        liste2 = []
        global liste_h
        global m
        m = f.readline()
        if m == '':
            return m
        else:
            for i in letters(m):
                liste2.append(i)
            liste_h.append(liste2)
            return maze_1()
    maze_1()

for o in range(len(liste_h)):
    for p in range(len(liste_h[0])):
        if liste_h[o][p] == 'S':
            col_h, row_h = int(o), int(p)
            break
def maze_solve_h(listex,col_gelen, row_gelen, col_giden, row_giden,can_ilk):
    try:
        if not (col_giden > -1 and row_giden > -1 and row_giden < len(listex[0]) and col_giden < len(listex)):
            return "0", can_ilk
        if listex[col_giden][row_giden] == 'S':
            if not (col_gelen == col_giden and row_gelen == row_giden + 1):
                sag, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden, row_giden + 1, can_ilk)
            if sag != "1" and not (col_gelen == col_giden and row_gelen == row_giden - 1):
                sol, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden, row_giden - 1, can_ilk)
            if sag != "1" and sol != "1" and not (col_gelen == col_giden - 1 and row_gelen == row_giden + 1):
                asagi, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden + 1, row_giden, can_ilk)
            if sag != "1" and sol != "1" and asagi != "1" and not (
                    col_gelen == col_giden + 1 and row_gelen == row_giden + 1):
                yukari, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden - 1, row_giden, can_ilk)
            if sag != "1" and sol != "1" and asagi != "1" and yukari != "1":
                return False, ret_can
            if ret_can < 0:
                return ret_can, False
            return True, ret_can

        elif listex[col_giden][row_giden] == 'W':
            return "0", can_ilk
        elif listex[col_giden][row_giden] == 'F':
            return "1", can_ilk

        elif listex[col_giden][row_giden] == 'P' or liste_h[col_giden][row_giden] == 'H':
            ilk_edgeri = listex[col_giden][row_giden]
            listex[col_giden][row_giden] = "G"
            if not (col_gelen == col_giden and row_gelen == row_giden + 1):
                ret_val, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden, row_giden + 1, can_ilk,)
                if ret_val == "1":
                    ret_can = can_ilk if listex[col_giden][row_giden] == 'H' else ret_can - 1
                    listex[col_giden][row_giden] = ret_val
                    return ret_val, ret_can
                listex[col_giden][row_giden] = ilk_edgeri
            if not (col_gelen == col_giden and row_gelen == row_giden - 1):
                ret_val, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden, row_giden - 1, can_ilk)
                if ret_val == "1":
                    ret_can = can_ilk if listex[col_giden][row_giden] == 'H' else ret_can - 1
                    listex[col_giden][row_giden] = ret_val
                    return ret_val, ret_can
                listex[col_giden][row_giden] = ilk_edgeri
            if not (col_gelen == col_giden + 1 and row_gelen == row_giden):
                ret_val, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden + 1, row_giden, can_ilk)
                if ret_val == "1":
                    ret_can = can_ilk if listex[col_giden][row_giden] == 'H' else ret_can - 1
                    listex[col_giden][row_giden] = ret_val
                    return ret_val, ret_can
                listex[col_giden][row_giden] = ilk_edgeri
            if not (col_gelen == col_giden - 1 and row_gelen == row_giden):
                ret_val, ret_can = maze_solve_h(listex,col_giden, row_giden, col_giden - 1, row_giden, can_ilk)
                if ret_val == "1":
                    ret_can = can_ilk if listex[col_giden][row_giden] == 'H' else ret_can - 1
                    listex[col_giden][row_giden] = ret_val
                    return ret_val, ret_can
                listex[col_giden][row_giden] = ilk_edgeri
            ret_can = can_ilk if listex[col_giden][row_giden] == 'H' else ret_can - 1
            return ret_val, ret_can
    except:
        return "0", can_ilk

cevap = maze_solve_h(liste_h,col_h,row_h,col_h,row_h,a)
maze_solve_h(liste,col,row,col,row,99999)

def zero(n):
    for s in range(len(n)):
        for z in range(len(n[s])):
            if n[s][z] == 'W' or n[s][z] == 'P':
                n[s][z] = '0'
zero(liste_h)
zero(liste)

with open(sys.argv[4],'w') as f:
        f.write("Solution for the given maze without health condition\n")
        for w in liste:
            f.write('%s\n' % ', '.join(letters(w)))
        f.write("Solution for the given maze with health condition\n")
        for q in liste_h:
            f.write('%s\n' % ', '.join(letters(q)))


