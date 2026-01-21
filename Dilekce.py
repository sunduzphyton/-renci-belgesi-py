dilekce="""          tarih:{}
T.C. 
    {} üniversitesi 
    {} fakültesi dekanlığına
    fakültenizden {} yılında mezun oldum. diplomanın tarafıma verilmesini arz ederim.

imza:
adı soyadı:{}
T.C. no:{}"""
tarih=input("tarihi:")
üniversite=input("üniversite adı:")
fakülte=input("fakülte adı:")
yıl=input("mezuniyet yılı:")
adı_soyadı=input("adı soyadı:")
tc_no=input("T.C. no:")
print(dilekce.format(tarih, üniversite, fakülte, yıl, adı_soyadı, tc_no))
