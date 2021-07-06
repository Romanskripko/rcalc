import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.polynomial as pol
from app import app


class Calculations:
    def __init__(self, excel_table):
        self.coords = excel_table.to_numpy()
        self.labels = excel_table.columns.values
        self.list_of_c = []
        self.func = 'z = '
        self.graph = ''

    def squaretype(self, rcoeff):
        fig = plt.figure()
        print(self.coords)
        # эта часть строит в 3д точки, координаты которых берет из массива. X Label можно заменить на название оси
        ax = plt.axes(projection='3d')
        ax.scatter(self.coords[:, 0], self.coords[:, 1], self.coords[:, 2], marker='^', c='#e31700')
        if self.labels is None:
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        else:
            ax.set_xlabel(self.labels[0])
            ax.set_ylabel(self.labels[1])
            ax.set_zlabel(self.labels[2])
        # эта часть считает коэффициенты полинома. Максимальные степени x и y записаны в [2, 2].
        Y = pol.polynomial.polyvander2d(self.coords[:, 0], self.coords[:, 1], [rcoeff, rcoeff])
        v = la.lstsq(Y, self.coords[:, 2], rcond=None)[0]
        # print(v)
        # v содержит все посчитанные коэффициенты
        Yrange = np.linspace(min(self.coords[:, 0]) * 1.5, max(self.coords[:, 0]) * 1.5, 1000)
        Xrange = np.linspace(min(self.coords[:, 1]) * 1.5, max(self.coords[:, 1]) * 1.5, 1000)
        # V - преобразование набора коэффициентов в матрицу. Форма матрицы для степеней [2, 2] имеет вид 3х3, для других
        # значений степеней форма будет меняться
        V = v.reshape(rcoeff + 1, rcoeff + 1)
        self.list_of_c = V
        # вывод полученной матрицы с коэффициентами
        print(V)
        x_pow = 0
        y_pow = 0
        for line in V:
            for coeff in line:
                self.func += f"{coeff} * x^{x_pow}y^{y_pow} + "
                y_pow += 1
            x_pow += 1
            y_pow = 0
        # строится поверхность
        self.func = self.func[:-2]
        print(self.func)
        Z = pol.polynomial.polygrid2d(Xrange, Yrange, V)
        X, Y = np.meshgrid(Xrange, Yrange)
        ax.plot_surface(X, Y, Z, rstride=10, cstride=10)
        # self.graph = mpld3.fig_to_html(fig)
        # mpld3.show()
        # plt.show()
        # output = io.BytesIO()
        # FigureCanvasAgg(fig).print_png(output)
        # return output.getvalue()
        fig.savefig('app\\static\\mypng.png')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
