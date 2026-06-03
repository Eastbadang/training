import sys
sys.path.append(r"<PATH_TO_CST_AMD64>/python_cst_libraries")

from win32com import client

oCSTApp = client.Dispatch("CSTStudio.Application")

# Open the project file and add a parameter
mws = oCSTApp.OpenFile(r"C:/Works/PycharmProjects/PY38/CST/CST_JOBS/A11_COIL.cst")
#mws.StoreParameter('my_tst_param',10.012)
#mws.Rebuild()

# Save the project copy
#end = len(full_cst_prj_file_name)
#cst_prj_copy_file_name = full_cst_prj_file_name[0:end-4] + '_copy_python.cst'
#mws.SaveAs(cst_prj_copy_file_name,'True')

print("HELLO")



# Quit CST
oCSTApp.Quit
#cst.Quit()