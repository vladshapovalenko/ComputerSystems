from Lab1entropy import proc_file, get_res
import pandas as pd
import matplotlib.pyplot as plt
import os


def base64encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    
    bit_str = ''
    base64_str = ''
    div24_symb = ''
    
    for byte in data:
        bin_byte = bin(byte).lstrip("0b")
        bin_byte = bin_byte.zfill(8)
        bit_str += bin_byte
    
    while len(bit_str) % 24 != 0:
        div24_symb = '='
        bit_str += '0'

    groups = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]
    for group in groups:
        base64_str += alphabet[int(group, 2)]

    base64_str += div24_symb

    return base64_str


Al_orig = 'sources/Al.txt'
Al_enc = 'sources/al_enc'
Al_bz2 = 'sources/Al.bz2'
Al_bz2_enc = 'sources/al_bz2_enc'

BSM_orig = 'sources/BSMNHC.txt'
BSM_enc = 'sources/bsmnhc_enc'
BSM_bz2 = 'sources/BSMNHC.bz2'
BSM_bz2_enc = 'sources/bsmnhc_bz2_enc'

RHCP_orig = 'sources/RHCP.txt'
RHCP_enc = 'sources/rhcp_enc'
RHCP_bz2 = 'sources/RHCP.bz2'
RHCP_bz2_enc = 'sources/rhcp_bz2_enc'

al = open(Al_orig, 'rb')
bsm = open(BSM_orig, 'rb')
rhcp = open(RHCP_orig, 'rb')



with open(Al_enc, 'w', encoding='utf-8') as file:
    file.write(base64encode(al.read()))
with open(BSM_enc, 'w', encoding='utf-8') as file:
    file.write(base64encode(bsm.read()))
with open(RHCP_enc, 'w', encoding='utf-8') as file:
    file.write(base64encode(rhcp.read()))

with open(Al_bz2, 'rb') as source, open(Al_bz2_enc, 'w', encoding='utf-8') as file:
    file.write(base64encode(source.read()))
with open(BSM_bz2, 'rb') as source, open(BSM_bz2_enc, 'w', encoding='utf-8') as file:
    file.write(base64encode(source.read()))
with open(RHCP_bz2, 'rb') as source, open(RHCP_bz2_enc, 'w', encoding='utf-8') as file:
    file.write(base64encode(source.read()))

al = open(Al_orig, encoding='utf-8')
bsm = open(BSM_orig, encoding='utf-8')
rhcp = open(RHCP_orig, encoding='utf-8')

al_enc = open(Al_enc)
bsm_enc = open(BSM_enc)
rhcp_enc = open(RHCP_enc)

al_bz2 = open(Al_bz2_enc)
bsm_bz2 = open(BSM_bz2_enc)
rhcp_bz2 = open(RHCP_bz2_enc)

info_al = proc_file(al, 'Alchemistry orig')
info_al_s = os.path.getsize(Al_orig)
info_al_enc = proc_file(al_enc, 'Alchemistry encoded')
info_al_enc_s = os.path.getsize(Al_enc)
info_al_bz2 = proc_file(al_bz2, 'Alchemistry bz2 encoded')
info_al_bz2_s = os.path.getsize(Al_bz2_enc)
print('Alchemistry orig_q: %f orig_s: %f enc_q: %f enc_s: %f bz2+enc_q: %f bz2+enc_s: %f' % (info_al, info_al_s, info_al_enc, info_al_enc_s, info_al_bz2, info_al_bz2_s))

info_bsm = proc_file(bsm, 'Kozaku ne spekotno orig')
info_bsm_s = os.path.getsize(BSM_orig)
info_bsm_enc = proc_file(bsm_enc, 'Kozaku ne spekotno encoded')
info_bsm_enc_s = os.path.getsize(BSM_enc)
info_bsm_bz2 = proc_file(bsm_bz2, 'Kozaku ne spekotno bz2 encoded')
info_bsm_bz2_s = os.path.getsize(BSM_bz2_enc)
print('Kozaku ne spekotno orig_q: %f orig_s: %f enc_q: %f enc_s: %f bz2+enc_q: %f bz2+enc_s: %f' % (info_bsm, info_bsm_s, info_bsm_enc, info_bsm_enc_s, info_bsm_bz2, info_bsm_bz2_s))

info_rhcp = proc_file(rhcp, 'Red Hot Chili Peppers orig')
info_rhcp_s = os.path.getsize(RHCP_orig)
info_rhcp_enc = proc_file(rhcp_enc, 'Red Hot Chili Peppers encoded')
info_rhcp_enc_s = os.path.getsize(RHCP_enc)
info_rhcp_bz2 = proc_file(rhcp_bz2, 'Red Hot Chili Peppers bz2 encoded')
info_rhcp_bz2_s = os.path.getsize(RHCP_bz2_enc)
print('Red Hot Chili Peppers orig_q: %f orig_s: %f enc_q: %f enc_s: %f bz2+enc_q: %f bz2+enc_s: %f' % (info_rhcp, info_rhcp_s, info_rhcp_enc, info_rhcp_enc_s, info_rhcp_bz2, info_rhcp_bz2_s))

soq = 'orig q'
sos = 'orig s'
seq = 'enc q'
ses = 'enc s'
sebz2q = 'bz2enc q'
sebz2s = 'bz2enc s'

df1 = pd.DataFrame([info_al, info_al_s, info_al_enc, info_al_enc_s, info_al_bz2, info_al_bz2_s], index=[soq, sos, seq, ses, sebz2q, sebz2s])
ax1 = df1.plot(kind='bar')
ax1.legend(['Alchemistry'])
df2 = pd.DataFrame([info_bsm, info_bsm_s, info_bsm_enc, info_bsm_enc_s, info_bsm_bz2, info_bsm_bz2_s], index=[soq, sos, seq, ses, sebz2q, sebz2s])
ax2 = df2.plot(kind='bar', color='green')
ax2.legend(['Kozaku ne spekotno'])
df3 = pd.DataFrame([info_rhcp, info_rhcp_s, info_rhcp_enc, info_rhcp_enc_s, info_rhcp_bz2, info_rhcp_bz2_s], index=[soq, sos, seq, ses, sebz2q, sebz2s])
ax3 = df3.plot(kind='bar', color='brown')
ax3.legend(['Red Hot Chili Peppers'])
plt.show()