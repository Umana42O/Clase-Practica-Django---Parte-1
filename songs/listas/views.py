from django.shortcuts import render

class cancion():
    def __init__(self, name, descripcion):
        self.name = name
        self.descripcion = descripcion
c1 = cancion("Take My Breath - TheWeeknd", "La mejor cancion de TheWeeknd")
canciones = [c1]


# Create your views here.
def index(request):
    names = []
    for i in canciones:
        names.append(i.name)
    if len(canciones) == 0:
        context = {
        "names":names,
        "vacio": True
        }
    else:
        context = {
        "names":names,
        "vacio": False
        }
    return render(request, 'listas/contenido1.html',context)

def descripcion(request,name):
    pass
    

