from flask import Flask, render_template, request
porta = 777;
app = Flask (__name__, template_folder='./static')

@app.route('/', methods=['GET', 'POST'])
def home():
       if(request.method == 'GET'):
           return render_template('index.html');
       else:
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'sub'):
               subtracao = int(request.form['num1']) - int(request.form['num2'])
               return '<h1>A subtração entre '+ str(request.form['num1']) + ' e ' + str(request.form['num2']) + ' é: ' + str(subtracao)+'</h1>'
           
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'soma'):
               soma = int(request.form['num1']) + int(request.form['num2'])
               return '<h1>A soma entre '+ str(request.form['num1']) + ' e ' + str(request.form['num2']) + ' é: ' + str(soma)+'</h1>'
           
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'mult'):
               multiplicacao = int(request.form['num1']) * int(request.form['num2'])
               return '<h1>A multiplicação entre '+ str(request.form['num1']) + ' e ' + str(request.form['num2']) + ' é: ' + str(multiplicacao)           
           
           if(request.form['num1'] != "" and request.form['num2'] != "" and request.form['escolha'] == 'div'):
               divisao = int(request.form['num1']) / int(request.form['num2'])
               return '<h1>A divisão entre '+ str(request.form['num1']) + ' e ' + str(request.form['num2']) + ' é: ' + str(divisao)+'</h1>'
           
           else:
               return 'Informe um valor válido!'
@app.errorhandler(404)
def not_found(error):
    return render_template('index.html')

app.run(port=porta, debug=True)