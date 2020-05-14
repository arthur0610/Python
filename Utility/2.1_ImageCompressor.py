from PIL import Image as IMG
from tkinter import *
from tkinter.filedialog import *

# to store the file names
src = {
    'path':[]
}

def compressor_app():
    app = Tk()
    Label(app, text='Image Compressor tool').pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='Open', command=getDataFromUI).pack()
    Button(app, text='Compress', command=compress).pack()
    app.geometry('300x400')

    return app

def getDataFromUI():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    src['path'] = f_names
    if src['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])

def compress():
    for f_path in src['path']:
        output = 'OUTPUT/'
        name = f_path.split('/')[-1]
        image = IMG.open(f_path)
        image.save(output+'c_'+name, quality=60)



app = compressor_app()
app.mainloop()








# from PIL import Image
# path = 'INPUT/warcraft_icon1.png'
# output = 'OUTPUT/C_warcraft_icon1.png'
# image = Image.open(path)
# image.save(output, quality=60)

