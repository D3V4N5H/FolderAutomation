import os,re,shutil
os.chdir('/Users/devanshtrivedi/Desktop')
matcher = re.compile(r'py(\w+\s\w+)+',re.I)

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if (matcher.match(name)):
            print(name)
            print('Move '+name+' to "Py notes" folder? (y/n)')
            reply=input()
            if reply.lower()=="y":
                shutil.move(
                    os.path.join(root,name),
                    os.path.join(root,'Py notes'))
            else:
                continue

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if(name.endswith('.py')):
           print('Move')
           print(name)
           print('to "my Py" folder? (y/n)')
           reply=input()
           if reply.lower()=="y":
               shutil.move(
                   os.path.join(root,name),
                   os.path.join(root,'my Py')
               )
           else:
               continue
