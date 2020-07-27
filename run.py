from flask import Flask, render_template, request
app = Flask(__name__) # Erstellung einer neuen Anwendung. Das __name__ gibt den import Namen an, wo die Anwendung defniert ist.
                      # Flask verwendet den import name um zu wissen wo die Ressourcen sind (templates, instance folder)

@app.route('/') # wenn das '/' ausgeführt wird, wird die def hello ausgeführt.
def hello():
    items =['Apfel', 'Birne', 'Banane']
    return render_template('start.html',name='Max Mustermann', items=items)

@app.route('/test')
def test():
    name= request.args.get('name')
    paragraph='<p>Hallo Welt</p>'
    return render_template('test.html', name=name) # ermöglicht das jetzt, dass der Name aus der URL auch im Browser angezeigt wird.

