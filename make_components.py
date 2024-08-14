"""
В переменную pathtodir задаем путь в дирректорию с файлом
Открываем Блендер и кидаем файл на монтажный стол
"""
import datetime
start=datetime.datetime.now().strftime("%H:%M:%S")


pathtodir = "K:\БЛЕНДЕР\Борщ невидимка\\"
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: #перебираем содержимое объекта Scene.
    strip_name = str(i)[28:str(i).find('")')] # выдергиваем из элемента списка ('<bpy_struct, SoundSequence("RC1_0000-19690.066") at 0x000001E9AF7BD608>') только название.
    bpy.data.scenes["Scene"].sequence_editor.sequences_all[strip_name].frame_start=0 #задаем начальную позицию для выбранного элемента.

target = "MovieSequence" #задаем тип объекта. Есть вариант "SoundSequence".
name_of_strip = ""
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: # перебираем всех кто на монтажном столе.
    strip_name = str(i)[28:str(i).find('")')] # выдергиваем из элемента списка ('<bpy_struct, SoundSequence("RC1_0000-19690.066") at 0x000001E9AF7BD608>') только название файла/стрипа.
    if str(i).find(target) > 2: # проверяем что фрагмент соответствует требованиям.
        if str(i).find("mkv") > 1: # проверяем наличие расширения. По умолчанию с ОБС получаем "MKV".
            name_of_strip = strip_name
    break

name_of_strip
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].frame_start=0
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip[:-3]+"001"].frame_start=0
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].channel=2
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip[:-3]+"001"].channel=1

# Linux
# pathtodir = "/media/goward/640/БЛЕНДЕР/"+pathtodir+"/"
# windows
bpy.data.scenes["Scene"].frame_end = bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].frame_final_duration - 1 #задаем номер финального кадра равный последнему кадру файла
bpy.ops.sequencer.rendersize() 
bpy.ops.sequencer.select_all()
#значения указаны для разрешения 2540х1420
#dmglog
start=datetime.datetime.now().strftime("%H:%M:%S")
bpy.data.scenes["Scene"].render.resolution_x=170
bpy.data.scenes["Scene"].render.resolution_y=134
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=941
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=629
bpy.data.scenes["Scene"].render.filepath=pathtodir+"dmglog_"
bpy.ops.render.opengl(animation=True, sequencer=True)
finish=datetime.datetime.now().strftime("%H:%M:%S")
print("Start - dmglog "+start)
print("Finish - dmglog "+finish)

#dmg
start=datetime.datetime.now().strftime("%H:%M:%S")
bpy.data.scenes["Scene"].render.resolution_x=54
bpy.data.scenes["Scene"].render.resolution_y=58
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=1000
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=517
bpy.data.scenes["Scene"].render.filepath=pathtodir+"dmg_"
bpy.ops.render.opengl(animation=True, sequencer=True)
finish=datetime.datetime.now().strftime("%H:%M:%S")
print("Start - dmg "+start)
print("Finish - dmg "+finish)

#time
start=datetime.datetime.now().strftime("%H:%M:%S")
bpy.data.scenes["Scene"].render.resolution_x=44
bpy.data.scenes["Scene"].render.resolution_y=16
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=-1225
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=-695
bpy.data.scenes["Scene"].render.filepath=pathtodir+"time_"
bpy.ops.render.opengl(animation=True, sequencer=True)
finish=datetime.datetime.now().strftime("%H:%M:%S")
print("Start - time "+start)
print("Finish - time "+finish)

#HP
start=datetime.datetime.now().strftime("%H:%M:%S")
bpy.data.scenes["Scene"].render.resolution_x=222
bpy.data.scenes["Scene"].render.resolution_y=18
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=1148
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=510
bpy.data.scenes["Scene"].render.filepath=pathtodir+"HP_"
bpy.ops.render.opengl(animation=True, sequencer=True)
finish=datetime.datetime.now().strftime("%H:%M:%S")
print("Start - HP "+start)
print("Finish - HP "+finish)

#crites
start=datetime.datetime.now().strftime("%H:%M:%S")
bpy.data.scenes["Scene"].render.resolution_x=228
bpy.data.scenes["Scene"].render.resolution_y=186
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=1156
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=615
bpy.data.scenes["Scene"].render.filepath=pathtodir+"crites_"
bpy.ops.render.opengl(animation=True, sequencer=True)
finish=datetime.datetime.now().strftime("%H:%M:%S")
print("Start - crites "+start)
print("Finish - crites "+finish)

#RC
bpy.data.scenes["Scene"].render.resolution_x=798
bpy.data.scenes["Scene"].render.resolution_y=1420
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=0
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=0
bpy.data.scenes["Scene"].render.filepath=pathtodir+"RC_"


fimish=datetime.datetime.now().strftime("%H:%M:%S")
print("Start all - "+start)
print("Finish all - "+finish)

#команда противника
"""
bpy.data.scenes["Scene"].render.resolution_x=232
bpy.data.scenes["Scene"].render.resolution_y=374
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=-1139
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=-458
bpy.data.scenes["Scene"].render.filepath=pathtodir+"comand_"
bpy.ops.render.opengl(animation=True, sequencer=True)
"""

#map
"""
bpy.data.scenes["Scene"].render.resolution_x=504
bpy.data.scenes["Scene"].render.resolution_y=506
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=-1018
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=457
bpy.data.scenes["Scene"].render.filepath=pathtodir+"map_"
bpy.ops.render.opengl(animation=True, sequencer=True)
"""


#killers
"""
bpy.data.scenes["Scene"].render.resolution_x=504
bpy.data.scenes["Scene"].render.resolution_y=104
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=-1010
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=150
bpy.data.scenes["Scene"].render.filepath=pathtodir+"KILLS_"
bpy.ops.render.opengl(animation=True, sequencer=True)
"""

#союзники
"""
bpy.data.scenes["Scene"].render.resolution_x=235
bpy.data.scenes["Scene"].render.resolution_y=374
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_x=1153
bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].transform.offset_y=-458
bpy.data.scenes["Scene"].render.filepath=pathtodir+"soyouzniki_"
bpy.ops.render.opengl(animation=True, sequencer=True)
"""