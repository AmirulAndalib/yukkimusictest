# needed for keepalive on repl cz repl will sleep after 15 mins of inactivity even if webserver is added or not...we will also add pinger


from flask import Flask
from threading import Thread



app = Flask('')


@app.route('/')

def home():

    return f"<h1>😎YukkiBot webserver is up and running successfully🔥</h1>"

def run():

  app.run(host='0.0.0.0',port=8080)



def keep_alive():  

    t = Thread(target=run)

    t.start()

keep_alive()