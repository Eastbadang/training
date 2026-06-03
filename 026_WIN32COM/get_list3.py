# import your library
import pythoncom

# must be 0
context = pythoncom.CreateBindCtx(0)

#Get Running Object Table
running_coms = pythoncom.GetRunningObjectTable()

#help(running_coms)

# Creates an enumerator that can list all the monikiers in our table
monikiers = running_coms.EnumRunning()

# Loop through all the monikies
for monikier in monikiers:
    print('-'*100)

    # print the display name
    print(monikier.GetDisplayName(context, monikier))

    # print the hash
    print(monikier.Hash())

    # Is System Moniker
    print(monikier.IsSystemMoniker())

# help(monikier)

#import win32com.client
#vs = win32com.client.gencache.EnsureDispatch('{00024500-0000-0000-C000-000000000046}')
#help(vs)

