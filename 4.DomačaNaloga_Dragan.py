def prazna(n):
    seznam = []
    for i in range(n):
        seznam.append('')
    return (seznam)

def je_prazna(plosca):
    stevec = 0
    stevec2 = 0
    while stevec != len(plosca):
        if plosca[stevec] == '':
            stevec2 = stevec2 + 1
        else:
            break
        stevec = stevec + 1
    if stevec == stevec2:
        var = True
    else:
        var = False
    return var

def v_niz(plosca):
    niz = ""
    for i in range (len(plosca)):
        niz+= str(plosca[i])
        if (plosca[i] == ''):
            niz+= str(' ')
        
    return(niz)
    
def je_prostor(plosca, kje, dolzina):
    if(plosca[kje]==''):
        if(kje == 0):
            for i in range (dolzina):
                if(plosca[kje+i+1] == ''):
                    return (True)
        if(kje != 0):
            for i in range (dolzina):
                if(plosca[kje+i+1] == '' and plosca[kje+1+i] >= (len(plosca)-1) and plosca[kje-1]==''):
                    return (True)
            
    else :
        return (False)
              
        
def postavi(plosca, kje, dolzina, oznaka):
    if (je_prostor(plosca, kje, dolzina) == True):
        for i in range (dolzina):
            s[kje] = oznaka
            kje+=1
        return(True)
    else:
        return(False)

def obstaja(plosca, oznaka):
    for i in s:
        if (i == oznaka):
            return(True)
    return(False)


def prazna(n):
    list = []
    for i in range(n):
        list.append('')
    return list

def je_prazna(plosca):
    for polje in plosca:
        if polje != '':
            return False
    return True

def v_niz(plosca):
    niz = ''
    for polje in plosca:
        if polje == '':
            niz += ' '
        else:
            niz += polje
    return niz

def je_prostor(plosca, kje, dolzina):
    if kje + dolzina > len(plosca):
        return False
    for i in range(-1, dolzina + 1):
        if kje + i < 0:
            continue
        if kje + i >= len(plosca):
            continue
        if plosca[kje + i] != '':
            return False
    return True

def postavi(plosca, kje, dolzina, oznaka):    
    if not je_prostor(plosca, kje, dolzina):
        return False
    for i in range(dolzina):
        plosca[kje + i] = oznaka
    return True

def obstaja(plosca, oznaka):
    return oznaka in plosca

def vse_oznake(plosca):
    oznake = []
    for polje in plosca:
        if polje == '':
            continue
        if polje not in oznake:
            oznake.append(polje)
    return oznake

def strel(plosca, kje):
    if kje >= len(plosca) or plosca[kje] == '':
        return 0
    oznaka = plosca[kje]
    plosca[kje] = ''
    if je_prazna(plosca):
        return 3
    if oznaka in plosca:
        return 1
    else:
        return 2


import unittest

class TestOgrevanje(unittest.TestCase):
    def test_prazna(self):
        self.assertEqual(prazna(1), [''])
        self.assertEqual(prazna(4), ['', '', '', ''])
        p = prazna(100)
        self.assertEqual(len(p), 100)
        self.assertTrue(all(map(''.__eq__, p)))

    def test_je_prazna(self):
        self.assertTrue(je_prazna(['', '', '', '']))
        self.assertTrue(je_prazna(['', '', '', '', '', '' ,'']))
        self.assertFalse(je_prazna(['', '', 'x', '', '', '' ,'']))
        self.assertFalse(je_prazna(['', '', 'a', '', '', '' ,'']))
        self.assertFalse(je_prazna(['x', 'x', 'x', 'x', 'x', 'x' ,'x']))

    def test_v_niz(self):
        self.assertEqual(v_niz(["a"]), "a")
        self.assertEqual(v_niz(["a", "b"]), "ab")
        self.assertEqual(v_niz(["a", "b", "a", "c"]), "abac")

        self.assertEqual(v_niz(["a", "b", "", "c"]), "ab c")
        self.assertEqual(v_niz(['', '', 'a', 'a', 'a', '', 'd', '', '']), "  aaa d  ")
        self.assertEqual(v_niz(prazna(4)), "    ")


class TestObvezna(unittest.TestCase):
    def test_je_prostor(self):
        plosca = ['', '', '', '', '', '', '', '', '', '']
        self.assertTrue(je_prostor(plosca, 1, 3))
        self.assertTrue(je_prostor(plosca, 6, 3))

        self.assertTrue(je_prostor(plosca, 0, 3))
        self.assertTrue(je_prostor(plosca, 7, 3))

        plosca[9] = "a"
        self.assertTrue(je_prostor(plosca, 0, 3))
        self.assertTrue(je_prostor(plosca, 0, 1))
        self.assertTrue(je_prostor(plosca, 7, 1))

        self.assertFalse(je_prostor(plosca, 8, 1))
        self.assertFalse(je_prostor(plosca, 7, 2))

        plosca = ['', '', '']
        self.assertTrue(je_prostor(plosca, 0, 1))
        self.assertTrue(je_prostor(plosca, 0, 2))
        self.assertTrue(je_prostor(plosca, 0, 3))
        self.assertTrue(je_prostor(plosca, 1, 1))
        self.assertTrue(je_prostor(plosca, 1, 2))
        self.assertTrue(je_prostor(plosca, 2, 1))
        self.assertFalse(je_prostor(plosca, 1, 3))

        plosca = ['a', '', '']
        self.assertFalse(je_prostor(plosca, 0, 1))
        self.assertFalse(je_prostor(plosca, 0, 2))
        self.assertFalse(je_prostor(plosca, 0, 3))
        self.assertFalse(je_prostor(plosca, 1, 1))
        self.assertFalse(je_prostor(plosca, 1, 2))
        self.assertTrue(je_prostor(plosca, 2, 1))

        plosca = ['', 'a', '']
        self.assertFalse(je_prostor(plosca, 0, 1))
        self.assertFalse(je_prostor(plosca, 0, 2))
        self.assertFalse(je_prostor(plosca, 0, 3))
        self.assertFalse(je_prostor(plosca, 1, 1))
        self.assertFalse(je_prostor(plosca, 1, 2))
        self.assertFalse(je_prostor(plosca, 2, 1))

        plosca = ['', '', 'a']
        self.assertTrue(je_prostor(plosca, 0, 1))
        self.assertFalse(je_prostor(plosca, 0, 2))
        self.assertFalse(je_prostor(plosca, 0, 3))
        self.assertFalse(je_prostor(plosca, 1, 1))
        self.assertFalse(je_prostor(plosca, 1, 2))
        self.assertFalse(je_prostor(plosca, 2, 1))

    def test_postavi(self):
        plosca = ['', '', '', '', '', '', '', '', '', '']
        self.assertTrue(postavi(plosca, 2, 3, 'x'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 1, 1, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 0, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 5, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 5, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertTrue(postavi(plosca, 6, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', 'y', 'y', '', ''])
        self.assertTrue(postavi(plosca, 0, 1, 'a'))
        self.assertEqual(plosca, ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', ''])

    def test_obstaja(self):
        plosca = ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
        self.assertTrue(obstaja(plosca, 'a'))
        self.assertTrue(obstaja(plosca, 'x'))
        self.assertTrue(obstaja(plosca, 'y'))
        self.assertFalse(obstaja(plosca, 'b'))

    def test_vse_oznake(self):
        plosca = ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
        self.assertEqual(set(vse_oznake(plosca)), set("axy"))
        plosca = ['', '', '', 'x', 'x', '', '', '', '', '']
        self.assertEqual(vse_oznake(plosca), ['x'])
        plosca = ['', '', '', '', '', '', '', '']
        self.assertEqual(vse_oznake(plosca), [])

    def test_strel(self):
        plosca = ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
        self.assertEqual(strel(plosca, 3), 1)
        self.assertEqual(plosca, ['a', '', 'x', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 3), 0)
        self.assertEqual(plosca, ['a', '', 'x', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 9), 0)
        self.assertEqual(plosca, ['a', '', 'x', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 2), 1)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 7), 1)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', 'y', '', '', ''])
        self.assertEqual(strel(plosca, 6), 2)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', '', '', '', ''])
        self.assertEqual(strel(plosca, 2), 0)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', '', '', '', ''])
        self.assertEqual(strel(plosca, 0), 2)
        self.assertEqual(plosca, ['', '', '', '', 'x', '', '', '', '', ''])
        self.assertEqual(strel(plosca, 4), 3)
        self.assertEqual(plosca, ['', '', '', '', '', '', '', '', '', ''])


class TestDodatna(unittest.TestCase):
    def test_razpostavi(self):
        plosca = razpostavi(10, [('a', 3)])
        s = v_niz(plosca)
        self.assertTrue('aaa' in s)
        self.assertEqual(s.count('a'), 3,
                         "Ladja 'a' mora biti dolga 3")

        ladje = [('a', 2), ('b', 3), ('c', 1)]
        plosca = razpostavi(10, ladje)
        s = v_niz(plosca)
        self.assertEqual(len(plosca), 10)
        for oznaka, dolzina in ladje:
            self.assertTrue(oznaka * dolzina in s)
            self.assertEqual(s.count(oznaka), dolzina,
                             "Ladja '{}' mora biti dolga {}".format(oznaka, dolzina))
        for c, d in zip(plosca, plosca[1:]):
            self.assertFalse(c and d and c != d,
                             "Ladje se ne smejo dotikati")


if __name__ == "__main__":
    unittest.main()
