from flask import Flask, jsonify
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

app = Flask(__name__)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-origin', '*')

    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
    
    return response
print("--- QUANTUM WEB SERVER STARTING ---")

def generate_quantum_key():
    qc = QuantumCircuit(8, 8)

    qc.h(range(8)) 
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.cx(3, 4)
    qc.cx(4, 5)
    qc.cx(5, 6)
    qc.cx(6, 7)
    qc.measure(range(8), range(8))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts(qc)

    return list(counts.keys())[0]
@app.route('/get-key', methods=['GET'])
def get_key():
    print("Request Recieved: Generating Key...")
    secret_key = generate_quantum_key()
    return jsonify({'quantum_key': secret_key, 'status': 'secure'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)