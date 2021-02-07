import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np
import os

def count_freq(chars):
    freq = {}
    total = sum(chars.values())
    for char in chars.keys():
        freq[char] = chars[char] * 1. / total
    
    return freq

def count_amount(string):
    chars = {}
    for char in string:
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    
    return chars

def count_entropy(freq):
    entropy = 0
    for char in freq:
        entropy -= freq[char] * math.log(freq[char], 2)

    return entropy

def get_res(string):
    chars = count_amount(string)
    freq = count_freq(chars)
    entropy = count_entropy(freq)

    return chars, freq, entropy

def visual_sep(chars, freq):
    order = sorted([*chars])
    
    df1 = pd.DataFrame.from_dict(chars, orient='index')
    df1 = df1.reindex(order)
    ax = df1.plot(kind='bar')
    ax.legend(['quantity of chars'])
    plt.show()

    df2 = pd.DataFrame.from_dict(freq, orient='index')
    df2 = df2.reindex(order)
    ax = df2.plot(kind='bar', color='green')
    ax.legend(['frequency of chars'])
    plt.show()

def proc_file(file, name):
    string = file.read()
    chars, freq, entropy = get_res(string)
    print('Chars amounts in %s' % name)
    keys = [*chars]
    keys.sort()
    for key in keys:
        print('%s: %i' % (key, chars[key]))
    

    print('Chars frequency in %s' % name)
    for key in keys:
        print('%s: %f' % (key, freq[key]))

    print('Entropy: %f' % entropy)

    quant = entropy * sum(chars.values()) / 8

    print('Quantity of information: %f' % quant)
    visual_sep(chars, freq)

    return quant

Al_orig = 'sources/Al.txt'
Al_orignot = 'sources/Al'
file_Al = open(Al_orig, encoding='utf-8')
Al_bz2 = Al_orignot + '.bz2'
Al_zip = Al_orignot + '.zip'
Al_gz = Al_orignot + '.gz'
Al_7z = Al_orignot + '.7z'
Al_xz = Al_orignot + '.xz'
info_Al = proc_file(file_Al, '\"Alchemistry\"')

BSM_orig = 'sources/BSMNHC.txt'
BSM_orignot = 'sources/BSMNHC'
file_BSM = open(BSM_orig,  encoding='utf-8')
BSM_bz2 = BSM_orignot + '.bz2'
BSM_zip = BSM_orignot + '.zip'
BSM_gz = BSM_orignot + '.gz'
BSM_7z = BSM_orignot + '.7z'
BSM_xz = BSM_orignot + '.xz'
info_BSM = proc_file(file_BSM, '\"Kozaku Ne Spekotno!\"')

RHCP_orig = 'sources/RHCP.txt'
RHCP_orignot = 'sources/RHCP'
file_RHCP = open(RHCP_orig,  encoding='utf-8')
RHCP_bz2 = RHCP_orignot + '.bz2'
RHCP_zip = RHCP_orignot + '.zip'
RHCP_gz = RHCP_orignot + '.gz'
RHCP_7z = RHCP_orignot + '.7z'
RHCP_xz = RHCP_orignot + '.xz'
info_RHCP = proc_file(file_RHCP, '\"Red Hot Chili Peppers\"')

sto = 'orig\n'
sbz2 = 'bz2\n'
szip = 'zip\n'
sgz = 'gz\n'
s7z = '7z\n'
sxz = 'xz\n'
sqoi = 'quantity\n'
slabel = 'Size of file'

y_Al = list(map(os.path.getsize, [Al_orig, Al_bz2, Al_zip, Al_gz, Al_7z, Al_xz]))
y_Al.append(round(info_Al))
x_Al = [sto  + str(y_Al[0]), sbz2 + str(y_Al[1]), szip + str(y_Al[2]), sgz + str(y_Al[3]), s7z + str(y_Al[4]), sxz + str(y_Al[5]), sqoi + str(y_Al[6])]
plt.ylabel(slabel)
plt.bar(x_Al, y_Al)
plt.show()

y_BSM = list(map(os.path.getsize, [BSM_orig, BSM_bz2, BSM_zip, BSM_gz, BSM_7z, BSM_xz]))
y_BSM.append(round(info_BSM))
x_BSM = [sto  + str(y_BSM[0]), sbz2 + str(y_BSM[1]), szip + str(y_BSM[2]), sgz + str(y_BSM[3]), s7z + str(y_BSM[4]), sxz + str(y_BSM[5]), sqoi + str(y_BSM[6])]
plt.ylabel(slabel)
plt.bar(x_BSM, y_BSM)
plt.show()

y_RHCP = list(map(os.path.getsize, [RHCP_orig, RHCP_bz2, RHCP_zip, RHCP_gz, RHCP_7z, RHCP_xz]))
y_RHCP.append(round(info_RHCP))
x_RHCP = [sto +  str(y_RHCP[0]), sbz2 + str(y_RHCP[1]), szip + str(y_RHCP[2]), sgz + str(y_RHCP[3]), s7z + str(y_RHCP[4]), sxz + str(y_RHCP[5]), sqoi + str(y_RHCP[6])]
plt.ylabel(slabel)
plt.bar(x_RHCP, y_RHCP)
plt.show()
