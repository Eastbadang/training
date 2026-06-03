import re, io
import win32com.client as win32
from win32com.client import Dispatch
import inspect

olook = win32.gencache.EnsureDispatch('Outlook.Application')
mapi = olook.GetNamespace("MAPI")

def display_folder(parent, level=-1):
    level += 1
    if hasattr(parent, 'Name'):
        print ("\t" * level) + parent.Name

    if hasattr(parent, 'Items'):
        for item in parent.Items:
            if hasattr(item, 'SentOnBehalfOfName'):
                print ("\t" * (level+1)) + u"보낸사람 : " + item.SentOnBehalfOfName

            if hasattr(item, 'Recipients'):
                recipients = ', '.join([recipent.Name for recipent in item.Recipients])
                print ("\t" * (level+1)) + u"받는사람 : " + recipients

            if hasattr(item, 'To'):
                print ("\t" * (level+1)) + u"To : " + item.To

            print ("\t" * (level+1)) + u"제목 : " + item.Subject + '\n'

    if hasattr(parent, 'Folders'):
        for folder in parent.Folders:
            display_folder(folder, level)

display_folder(mapi)