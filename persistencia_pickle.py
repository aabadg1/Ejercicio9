import pickle
def store(data,filename):
    pickle.dump(data,open(filename,'wb'))
def retrieve(filename):
    try:
        f_0= open(filename,'rb')
    except:
        print('Error al abrir el archivo', filename)
        return None
    content= pickle.load(f_0)
    f_0.close()
    return content
