# Делаем красивую картинку. перебором находим видео дорожки. Проверяем что они не относятся к дорожкам дополнительных элементов и поднимаем цвет и яркость
added_elements = ["crites","dmg","time","HP","map","comand","dmglog",]
for i in bpy.data.scenes['Scene'].sequence_editor.sequences_all: # перебираем всех кто на монтажном столе.
    if str(i).find("MovieSequence") > 2:
        if str(i).find("MovieSequence") > 2:
            if str(i).find("crites") > 1 or str(i).find("dmg") > 1 or str(i).find("time") > 1 or str(i).find("HP") > 1 or str(i).find("map") > 1 or str(i).find("comand") > 1 or str(i).find("dmglog") > 1: #переделать!! Вроди есть возможность в ифе испольховать цикл в котором перебирать элементы из списка. Возможно фантазия :).
                continue
            else:
                bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].color_saturation+=0.2
                bpy.data.scenes["Scene"].sequence_editor.sequences_all[str(i)[28:str(i).find('")')]].color_multiply+=0.2
                