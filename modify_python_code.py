#!/usr/bin/python
import os

#source_file_path = 'C:/Users/SzoFiel/Desktop/打包自动化/test_play.bat'
#target_file_path = 'C:/Users/SzoFiel/Desktop/打包自动化/test_play.bat'
#,encoding='utf-8'
def change_char_in_file(source_file_path,target_file_path,source_char,target_char):
        fo_source = open(source_file_path, 'r',encoding='utf-8')
        text = fo_source.read()
        new_text = text.replace(source_char,target_char)
        fo_source.close()

        if os.path.exists(target_file_path):
            os.remove(target_file_path+"_原文.txt")
            os.rename(target_file_path,target_file_path+"_原文.txt")

        fo_target = open(target_file_path,'w',encoding='utf-8')
        fo_target.write(new_text)
        fo_target.flush()
        fo_target.close()


#change_char_in_file( 'C:/Users/SzoFiel/Desktop/打包自动化/test_play.bat','C:/Users/SzoFiel/Desktop/打包自动化/test_play.bat','\\','/')
#change_char_in_file( 'C:/Users/SzoFiel/Desktop/打包自动化/test_play.bat','C:/Users/SzoFiel/Desktop/打包自动化/test_play.bat','/','\\')

#change_char_in_file( 'C:/Users/SzoFiel/Desktop/打包自动化/commond_test.txt','C:/Users/SzoFiel/Desktop/打包自动化/commond_test.txt','\\','/')
#change_char_in_file( 'C:/Users/SzoFiel/Desktop/打包自动化/commond_test.txt','C:/Users/SzoFiel/Desktop/打包自动化/commond_test.txt','/','\\')

#change_char_in_file('C:/Users/SzoFiel/Desktop/打包自动化/TestPython.py','C:/Users/SzoFiel/Desktop/打包自动化/TestPython.py','\\','/')
#change_char_in_file('C:/Users/SzoFiel/Desktop/打包自动化/package_test.py','C:/Users/SzoFiel/Desktop/打包自动化/package_test.py','\\','/')

change_char_in_file("F:\workspace\ORG_GameMaker\Documents\共享文档\橙光引擎II\说明文档\package_config.txt","F:\workspace\ORG_GameMaker\Documents\共享文档\橙光引擎II\说明文档\package_config.txt",'\\','/')

#change_char_in_file('C:/Users/SzoFiel/Desktop/打包自动化/config.py','C:/Users/SzoFiel/Desktop/打包自动化/config.py','\\','/')