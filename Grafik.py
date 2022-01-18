import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Grafik:
    @staticmethod
    def Ciz(pencere,listx,listy,baslik):
        #Doviz grafik oluşturma bölümü
        figure=Figure(figsize=(20,6)) #en,boy inç tipinde
        g=figure.gca()
        g.plot(listx,listy)
        figure.autofmt_xdate(rotation=45)

        g.set_title(baslik,fontsize=12)
        g.set_xlabel("Günler",fontsize=10)
        g.set_ylabel("Kur",fontsize=10)

        canvas=FigureCanvasTkAgg(figure,master=pencere)
        canvas.get_tk_widget().grid(row=3,column=0,columnspan=10)
        canvas.draw()