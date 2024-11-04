from flask import Flask, render_template

app =Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_reporte')
def generar_reporte():
    return render_template('generar_reportes.html')

@app.route('/registro_exitoso')
def registro_exitoso():
    return render_template('solicitud_registrada_con_exito.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/generar_reporte')
def nuevo_registro():
    return render_template('generar_reportes.html')

@app.route('/consultar')
def consultar():
    return render_template('consultar.html')

@app.route('/solicitud_en_curso')
def solicitud_en_curso():
    return render_template('solicitud_en_curso.html')

@app.route('/quienes_somos')
def quienes_somos ():
    return render_template('quienes_somos.html')

@app.route('/MOD')
def MOD ():
    return render_template('MOD.html')
