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
        # print(self.coords)
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
        Y = pol.polynomial.polyvander2d(self.coords[:, 0], self.coords[:, 1], [rcoeff, rcoeff])
        v = la.lstsq(Y, self.coords[:, 2], rcond=None)[0]
        Yrange = np.linspace(min(self.coords[:, 0]) * 1.5, max(self.coords[:, 0]) * 1.5, 1000)
        Xrange = np.linspace(min(self.coords[:, 1]) * 1.5, max(self.coords[:, 1]) * 1.5, 1000)
        V = v.reshape(rcoeff + 1, rcoeff + 1)
        self.list_of_c = V
        # print(V)
        x_pow = 0
        y_pow = 0
        for line in V:
            for coeff in line:
                self.func += f"{coeff} * x^{x_pow}y^{y_pow} + "
                y_pow += 1
            x_pow += 1
            y_pow = 0
        self.func = self.func[:-2]
        # print(self.func)
        Z = pol.polynomial.polygrid2d(Xrange, Yrange, V)
        X, Y = np.meshgrid(Xrange, Yrange)
        ax.plot_surface(X, Y, Z, rstride=10, cstride=10)
        fig.savefig('app\\static\\mypng.png')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
