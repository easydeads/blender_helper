engof=endof-1
"""Размещение компонентов"""

target = "MovieSequence" #
name_of_strip = ""
channel_n=2
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: # перебираем всех кто на монтажном столе
    strip_name = str(i)[28:str(i).find('")')] # выдергиваем из элемента списка ('<bpy_struct, SoundSequence("RC1_0001-19690.066") at 0x000001E9AF7BD608>') только название файла/стрипа
    bpy.data.scenes["Scene"].sequence_editor.sequences_all[strip_name].frame_start=0 #изменяем начало на кадр "0"
    if str(i).find(target) > 2: # проверяем что фрагмент соответствует требованиям
        if str(i).find("dmglog") > 1: #dmglog
            dmglog = strip_name #добавить поиск необходимого файла по начальному названию
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmglog].channel=channel_n #задаем позицию по каналам
            print("channel dmglog is - " + str(channel_n))
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmglog].blend_type="LIGHTEN"
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmglog].transform.scale_x=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmglog].transform.scale_y=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmglog].transform.offset_x=-228
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmglog].transform.offset_y=528
        elif str(i).find("dmg") > 1: #dmg
            dmg = strip_name
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmg].channel=channel_n
            print("channel dmg is - " + str(channel_n))
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmg].blend_type="LIGHTEN"
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmg].transform.scale_x=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmg].transform.scale_y=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmg].transform.offset_x=346
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[dmg].transform.offset_y=608
        elif str(i).find("time") > 1: #time
            time = strip_name #добавить поиск необходимого файла по начальному названию
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[time].channel=channel_n
            print("channel time is - " + str(channel_n))
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[time].blend_type="LIGHTEN"
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[time].transform.scale_x=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[time].transform.scale_y=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[time].transform.offset_x=346
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[time].transform.offset_y=689
        elif str(i).find("HP") > 1: #HP
            HP = strip_name #добавить поиск необходимого файла по начальному названию
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[HP].channel=channel_n
            print("channel HP is - " + str(channel_n))
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[HP].transform.rotation=1.570796
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[HP].transform.scale_x=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[HP].transform.scale_y=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[HP].transform.offset_x=-383
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[HP].transform.offset_y=-488
        elif str(i).find("map") > 1: #map
            map = strip_name #добавить поиск необходимого файла по начальному названию
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[map].channel=channel_n
            print("channel map is - " + str(channel_n))
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[map].transform.offset_x=806
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[map].transform.scale_x=1.585
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[map].transform.scale_y=1.585
        elif str(i).find("crites") > 1: #crites
            crites = strip_name #добавить поиск необходимого файла по начальному названию
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].channel=channel_n
            print("channel crites is - " + str(channel_n))
            #bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].blend_type="LIGHTEN"
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].transform.offset_x=-251
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].transform.offset_y=-618
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].transform.scale_x=1
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].transform.scale_y=1
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].color_multiply+=0.2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[crites].blend_type="LIGHTEN"
        elif str(i).find("comand") > 1: #comand
            comand = strip_name #добавить поиск необходимого файла по начальному названию
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[comand].channel=channel_n
            print("channel comand is - " + str(channel_n))
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[comand].transform.offset_x=797
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[comand].transform.scale_x=1
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[comand].transform.scale_y=1
    channel_n+=1
            
bpy.ops.sequencer.select_all(action='SELECT') #select all
#bpy.ops.sequencer.view_all_preview() #preview fit to window
bpy.ops.sequencer.enable_proxies(proxy_25=True, overwrite=True) #select proxy to 25%, owerwrite enable
bpy.ops.sequencer.rebuild_proxy() #rebuild proxy
        

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Готовим список с целевыми элементами
name_of_strip = ""
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: # перебираем всех кто на монтажном столе
    # выдергиваем из элемента списка ('<bpy_struct, SoundSequence("RC1_0001-19690.066") at 0x000001E9AF7BD608>') только название файла/стрипа
    if str(i).find("MovieSequence") > 2: # проверяем что фрагмент соответствует требованиям
        if str(i).find("crites") > 1: #dmglog
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].transform.offset_x=-486
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].transform.offset_y=-432
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].crop.min_x=176 #left
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].crop.max_x=5 #right
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].crop.max_y=3 #top
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].crop.min_y=142 #bottom
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].transform.scale_x=2
            bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].transform.scale_y=2

#пушка
frag_name = "crites_0001-20901.031"
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_x=-139
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_y=-350
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_x=3 #left
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_x=179 #right
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_y=82 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_y=62 #bottom
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.scale_x=2
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.scale_y=2

#мотор
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_x=-255
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_y=-350
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_x=8 #left
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_x=181 #right
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_y=9 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_y=146 #bottom

#мехвод
frag_name = "crites_0001-20901.031"
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_x=-317
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_y=-524
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_x=90 #left
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_x=114 #right
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_y=162 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_y=0 #bottom
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.scale_x=2
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.scale_y=2

#уничтожил
frag_name = "crites_0001-20901.031"
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_x=24
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.offset_y=349
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_x=825 #left
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_x=767 #right
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.max_y=1043 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].crop.min_y=351 #bottom
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.scale_x=2
bpy.data.scenes["Scene"].sequence_editor.sequences_all[frag_name].transform.scale_y=2

#подробный отчет
detail_screen="WorldOfTanks_DJFxIHigEn.png"
bpy.data.scenes["Scene"].sequence_editor.sequences_all[detail_screen].transform.offset_x=662
bpy.data.scenes["Scene"].sequence_editor.sequences_all[detail_screen].transform.offset_y=-551
bpy.data.scenes["Scene"].sequence_editor.sequences_all[detail_screen].transform.scale_x=2.146
bpy.data.scenes["Scene"].sequence_editor.sequences_all[detail_screen].transform.scale_y=2.146
bpy.data.scenes["Scene"].sequence_editor.sequences_all[detail_screen].crop.max_y=69 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[detail_screen].crop.min_y=202 #bottom
#командный результат
commnd_screen="WorldOfTanks_vjFF2gimez.png"
bpy.data.scenes["Scene"].sequence_editor.sequences_all[commnd_screen].transform.offset_x=435
bpy.data.scenes["Scene"].sequence_editor.sequences_all[commnd_screen].transform.offset_y=-539
bpy.data.scenes["Scene"].sequence_editor.sequences_all[commnd_screen].transform.scale_x=2.394
bpy.data.scenes["Scene"].sequence_editor.sequences_all[commnd_screen].transform.scale_y=2.394
bpy.data.scenes["Scene"].sequence_editor.sequences_all[commnd_screen].crop.max_y=85 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[commnd_screen].crop.min_y=417 #bottom
#личный результат
personal_screen="WorldOfTanks_eyWNryd8V7.png"
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].transform.offset_x=-37
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].transform.offset_y=-508
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].transform.scale_x=1.815
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].transform.scale_y=1.815
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].crop.min_x=515 #left
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].crop.max_x=18 #right
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].crop.max_y=118 #top
bpy.data.scenes["Scene"].sequence_editor.sequences_all[personal_screen].crop.min_y=415 #bottom
