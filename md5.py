#-*- coding:utf-8 -*-
import pprint
myfile = open('word.txt', 'r') #Word 贴过来的文档的名字
md5file = open('md5.txt','r') #标准md5 文档的名字

md5Words=[]
line = md5file.readline() 
while line:  
    list = line.split(' ')
    for word in list:
       md5Words.append(word)  
    line = md5file.readline()  
md5file.close()

allWords = []  
line = myfile.readline()  
while line:  
    list = line.split(' ')
    for word in list:
        allWords.append(word)  
    line = myfile.readline()  
myfile.close()    


md5List=[]
pathList=[]
md5Comparelist=[]
pathComparelist=[]
for eachone in md5Words:
    if len(eachone) == 32:
        md5List.append(eachone)
    elif "/" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathList.append(eachone)
        else:
            pathList.append(eachone)


for eachone in allWords:
    if len(eachone) ==32:
        md5Comparelist.append(eachone)
    elif "/" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathComparelist.append(eachone)
        else:
            pathComparelist.append(eachone)
    elif "boot" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathComparelist.append(eachone)
        else:
            pathComparelist.append(eachone)
    elif "V3" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathComparelist.append(eachone)
        else:
            pathComparelist.append(eachone)
    elif "client" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathComparelist.append(eachone)
        else:
            pathComparelist.append(eachone)
    elif "boot_env" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathComparelist.append(eachone)
        else:
            pathComparelist.append(eachone)
    elif "lib" in eachone:
        if eachone[-1] =="\n":
            eachone = eachone[:-1]
            pathComparelist.append(eachone)
        else:
            pathComparelist.append(eachone)





md5dict=dict(map(lambda x,y:[x,y],pathList,md5List))
md5comparedict = dict(map(lambda x,y:[x,y],pathComparelist,md5Comparelist))






if md5dict["/opt/3tcloud/bin/3tchpviewer"] == md5comparedict['/usr/local/bin/3tchpviewer']:
    pass
else:
    md5dict["/opt/3tcloud/bin/3tchpviewer"] = md5comparedict['/usr/local/bin/3tchpviewer']


if md5dict["/opt/3tcloud/bin/3tchpdaemon/3tchpdaemon"] ==md5comparedict['/home/hofmann/3tchpdaemon/3tchpdaemon']:
    pass
else:
    md5dict["/opt/3tcloud/bin/3tchpdaemon/3tchpdaemon"] = md5comparedict['/home/hofmann/3tchpdaemon/3tchpdaemon']



if md5dict['/opt/3tcloud/bin/asound.state'] == md5comparedict['/opt/3tcloud/bin/asound.state']:
    pass
else:
    md5dict['/opt/3tcloud/bin/asound.state'] = md5comparedict['/opt/3tcloud/bin/asound.state']


if md5dict['/opt/3tcloud/bin/audio_channel_client'] ==md5comparedict['/opt/3tcloud/bin/audio_channel_client']:
    pass
else:
    md5dict['/opt/3tcloud/bin/audio_channel_client'] =md5comparedict['/opt/3tcloud/bin/audio_channel_client']


if md5dict['/opt/3tcloud/bin/socketclient_n2h'] == md5comparedict['/opt/3tcloud/bin/socketclient_n2h']:
    pass
else:
    md5dict['/opt/3tcloud/bin/socketclient_n2h'] = md5comparedict['/opt/3tcloud/bin/socketclient_n2h']



if md5dict['/opt/3tcloud/bin/socketclient_h2n'] ==md5comparedict['/opt/3tcloud/bin/socketclient_h2n']:
    pass
else:
    md5dict['/opt/3tcloud/bin/socketclient_h2n'] =md5comparedict['/opt/3tcloud/bin/socketclient_h2n']

if md5dict['/opt/3tcloud/bin/start_audio_channel.sh'] == md5comparedict['/opt/3tcloud/bin/start_audio_channel.sh']:
    pass
else:
    md5dict['/opt/3tcloud/bin/start_audio_channel.sh'] = md5comparedict['/opt/3tcloud/bin/start_audio_channel.sh']


if md5dict['/opt/3tcloud/bin/stop_audio_channel.sh'] ==md5comparedict['/opt/3tcloud/bin/stop_audio_channel.sh']:
    pass
else:
    md5dict['/opt/3tcloud/bin/stop_audio_channel.sh'] =md5comparedict['/opt/3tcloud/bin/stop_audio_channel.sh']

if md5dict['/opt/3tcloud/bin/start_record_sound_channel.sh'] ==md5comparedict['/opt/3tcloud/bin/start_record_sound_channel.sh']:
    pass
else:
    md5dict['/opt/3tcloud/bin/stop_audio_channel.sh'] = md5comparedict['/opt/3tcloud/bin/stop_audio_channel.sh']

if md5dict['/opt/3tcloud/bin/stop_record_sound_channel.sh'] ==md5comparedict['/opt/3tcloud/bin/stop_record_sound_channel.sh']:
    pass
else:
    md5dict['/opt/3tcloud/bin/stop_record_sound_channel.sh'] = md5comparedict['/opt/3tcloud/bin/stop_record_sound_channel.sh']


if md5dict['/3tcloud_branch/chpprotocol/winserver/trunk/libmultimedia_core.so'] ==md5comparedict['./out/libmultimedia_core.so']:
    pass
else:
    md5dict['/3tcloud_branch/chpprotocol/winserver/trunk/libmultimedia_core.so'] =md5comparedict['./out/libmultimedia_core.so']

if md5dict['/3tcloud_branch/chpprotocol/winserver/trunk/libmm_s5pv210.so'] == md5comparedict['./out/libmm_s5pv210.so']:
    pass
else:
    md5dict['/3tcloud_branch/chpprotocol/winserver/trunk/libmm_s5pv210.so'] = md5comparedict['./out/libmm_s5pv210.so']

if  md5dict['/opt/3tcloud/boot_bin/u-boot_v7.bin'] == md5comparedict['u-boot_v7.bin']:
    pass
else:
    md5dict['/opt/3tcloud/boot_bin/u-boot_v7.bin'] = md5comparedict['u-boot_v7.bin']

if  md5dict['/opt/3tcloud/boot_bin/u-boot_v8.bin'] == md5comparedict['u-boot_v8.bin']:
    pass
else:
    md5dict['/opt/3tcloud/boot_bin/u-boot_v8.bin'] = md5comparedict['u-boot_v8.bin']

if  md5dict['/opt/3tcloud/boot_bin/u-boot_v9.bin'] == md5comparedict['u-boot_v9.bin']:
    pass
else:
    md5dict['/opt/3tcloud/boot_bin/u-boot_v9.bin'] = md5comparedict['u-boot_v9.bin']

if md5dict['/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk'] == md5comparedict['V325']:
    pass
else:
    md5dict['/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk'] = md5comparedict['V325']

if md5dict['/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk_v8'] ==md5comparedict['V326']:
    pass
else:
    md5dict['/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk_v8'] =md5comparedict['V326']


if md5dict['/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk_v9'] ==md5comparedict['V327']:
    pass
else:
   md5dict['/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk_v9'] =md5comparedict['V327']


if md5dict['/3tcloud_branch/hs_centos_trunk/client/bin/client'] ==md5comparedict['client']:
    pass
else:
    md5dict['/3tcloud_branch/hs_centos_trunk/client/bin/client'] =md5comparedict['client']

if md5dict['/usr/bin/client'] ==md5comparedict['client']:
    pass
else:
    md5dict['/usr/bin/client'] =md5comparedict['client']


if md5dict['/usr/bin/boot_env'] == md5comparedict['boot_env']:
    pass
else:
    md5dict['/usr/bin/boot_env'] = md5comparedict['boot_env']

if md5dict['/3tcloud_upgrade/client_upgrade_2'] == md5comparedict['client_upgrade_2']:
    pass
else:
    md5dict['/3tcloud_upgrade/client_upgrade_2'] = md5comparedict['client_upgrade_2']

if md5dict['/usr/lib/libhwinfo.so'] == md5comparedict['libhwinfo.so']:
    pass
else:
    md5dict['/usr/lib/libhwinfo.so'] = md5comparedict['libhwinfo.so']


if md5dict['/usr/lib/libupgrade.so'] ==md5comparedict['libupgrade.so']:
    pass
else:
    md5dict['/usr/lib/libupgrade.so'] =md5comparedict['libupgrade.so']



pathlist =['/opt/3tcloud/bin/3tchpviewer','/opt/3tcloud/bin/3tchpdaemon/3tchpdaemon','/opt/3tcloud/bin/asound.state',
        '/opt/3tcloud/bin/audio_channel_client','/opt/3tcloud/bin/socketclient_n2h','/opt/3tcloud/bin/socketclient_h2n ',
           '/opt/3tcloud/bin/start_audio_channel.sh','/opt/3tcloud/bin/stop_audio_channel.sh','/opt/3tcloud/bin/start_record_sound_channel.sh',
           '/opt/3tcloud/bin/stop_record_sound_channel.sh','/3tcloud_branch/chpprotocol/winserver/trunk/libmultimedia_core.so',
           '/3tcloud_branch/chpprotocol/winserver/trunk/libmm_s5pv210.so','/opt/3tcloud/boot_bin/u-boot_v7.bin',
           '/opt/3tcloud/boot_bin/u-boot_v8.bin','/opt/3tcloud/boot_bin/u-boot_v9.bin','/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk',
           '/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk_v8','/3tcloud_branch/hs_centos_trunk/kernel/zImage_hs_centos_trunk_v9',
           '/3tcloud_branch/hs_centos_trunk/client/bin/client','/usr/bin/client','/usr/bin/boot_env','/3tcloud_upgrade/client_upgrade_2',
           '/usr/lib/libhwinfo.so','/usr/lib/libupgrade.so']



f = open('md5out.txt','w')
for x in range(len(pathlist)):
    for key in md5dict:
        if pathlist[x] == key:
            print md5dict[key] +' ' + key
            f.writelines( md5dict[key]+"  "+key+'\n')
f.close()


print "md5 file has been Done,please check md5out.txt"

