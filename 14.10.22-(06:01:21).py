import os,subprocess
info = os.popen('adb shell dumpsys battery').read().split()
final = info[-9]+" percent "+["charging","not charging"][any([info[5],info[8],info[11]])]
print(final)

#google_speech \"$(python3 \'14.10.22-(06:01:21).py\')\"
