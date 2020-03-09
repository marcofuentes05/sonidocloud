import psycopg2 as bd
import sys
# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton


try: 
    conn = bd.connect(user = 'marco',
                        password = '12345678',
                        host= '127.0.0.1' ,
                        port= '5432',
                        database= 'proyecto' )
    cursor = conn.cursor()
    print ( conn.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    # cursor.execute("INSERT INTO tst(id,nombre, apellido) VALUES (57, \'Jose\', \'Lima\')")
    # conn.commit()

    cursor.execute("SELECT COUNT(*) FROM ARTIST")
    record = cursor.fetchall()

    #print("HAY "+ str(record)+ " ARTISTAS EN LA BASE DE DATOS")

    # 2. Create an instance of QApplication
    app = QApplication(sys.argv) #Aqui tambien puedo poner [], porque no le voy a pasar comandos de CMD

    window = QWidget()
    window.setWindowTitle('Ejemplo de App 01')
    window.setGeometry(100,100,280,280) #(x,y,witdth, height)
    window.move(60,15)
    layout = QVBoxLayout()
    layout.addWidget(QLabel('<h1> Hay '+str(record[0][0])+' artistas en la base de datos</h1>', parent=window))
    layout.addWidget(QPushButton('Hola'))
    lay = QHBoxLayout()
    lay.addWidget(QPushButton('izquierda'))
    lay.addWidget(QPushButton('centro'))
    lay.addWidget(QPushButton('derecha'))
    layout.addLayout(lay)

    window.setLayout(layout)

    #Para ensegnar la ventana
    window.show()
except (Exception) as error :
    print ("ERROR", error)
finally:
    #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
sys.exit(app.exec_())
