def getLogin(self, userdb, passworddb, host, port, database,username, password):
      try:
          conn = bd.connect(user = 'marco',
                              password = '12345678',
                              host= host ,
                              port= port,
                              database= database )
          cursor = conn.cursor()
          query = "SELECT * FROM user_client WHERE username = \'luisg95\'"
          cursor.execute(query)
          record = cursor.fetchall()
          print(record)
          return self.openHomeAdmin
      except (Exception) as error :
          print ("ERROR", error)
          return print('Error')
      finally:
          #closing database connection.
              if(conn):
                  cursor.close()
                  conn.close()
                  #print("PostgreSQL connection is closed")
