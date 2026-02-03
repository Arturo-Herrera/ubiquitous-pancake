from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de datos temporal
puntos_usuario = []

@app.route('/')
def index():
    """
    Ruta raíz: Carga la Landing Page (index.html)
    """
    return render_template('index.html')

# --- CORRECCIÓN AQUÍ ---
# Cambiamos la ruta a '/mapa' para que no choque con la de arriba
@app.route('/mapa')
def mapa():
    """
    Ruta del mapa: Carga la aplicación principal (mapa.html)
    """
    return render_template('mapa.html')
# -----------------------

@app.route('/api/guardar', methods=['POST'])
def guardar():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "mensaje": "No se recibieron datos"}), 400
        
        puntos_usuario.append(data)
        print(f"Punto guardado: {data.get('name', 'Sin nombre')}")
        
        return jsonify({
            "status": "success", 
            "mensaje": "Lugar guardado en el diario de ruta",
            "total_puntos": len(puntos_usuario)
        })
    except Exception as e:
        return jsonify({"status": "error", "mensaje": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)