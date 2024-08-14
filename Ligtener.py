pathtodir = "E:\ОБС\Записи\Борщ невидимка\\" #input("Path to work dir: ") #
bpy.data.scenes["Scene"].render.filepath=pathtodir+"RC1_" #задаем путь в рабочий каталог и название файла "RC1_"

#def make_lighten():
all_strip = []
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: # добавляем в список все имеющиеся на монтажном столе элементы
    all_strip.append(str(i)[28:str(i).find('")')])

all_strip

# Готовим список с целевыми элементами
target = "MovieSequence" #
name_of_strip = ""
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: # перебираем всех кто на монтажном столе
    strip_name = str(i)[28:str(i).find('")')] # выдергиваем из элемента списка ('<bpy_struct, SoundSequence("RC1_0001-19690.066") at 0x000001E9AF7BD608>') только название файла/стрипа
    if str(i).find(target) > 2: # проверяем что фрагмент соответствует требованиям
        if str(i).find("mkv") > 1: # проверяем наличие расширения
            name_of_strip = strip_name
    break

name_of_strip

for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all:
    strip_name = str(i)[28:str(i).find('")')] # выдергиваем из элемента списка ('<bpy_struct, SoundSequence("RC1_0001-19690.066") at 0x000001E9AF7BD608>') только название
    #print(strip_name + " before = " + str(bpy.data.scenes["Scene"].sequence_editor.sequences_all[strip_name].frame_start))
    bpy.data.scenes["Scene"].sequence_editor.sequences_all[strip_name].frame_start=0 #задаем начальную позицию для выделенного элемента
    #print(strip_name + " Changed = " + str(bpy.data.scenes["Scene"].sequence_editor.sequences_all[strip_name].frame_start))

#bpy.ops.sequencer.select_all()
bpy.ops.sequencer.set_range_to_strips() #выравниваем количество кадров по элементу
bpy.ops.sequencer.rendersize()
bpy.ops.render.opengl(animation=True, sequencer=True) #рендер облегченного файла

"""
endof = bpy.data.scenes["Scene"].sequence_editor.sequences_all[name_of_strip].frame_final_duration #определяем конечный кадр элемента
RC1 = "RC1_0001-"+str(endof)+".mp4"
"""