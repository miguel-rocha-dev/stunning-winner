from flask import Flask, request, render_template,send_file

from gerador_pdf3 import criar_proposta2camara

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/adicionar_cliente")
def adicionar_cliente():
    return render_template("adicionar_cliente.html")

@app.route("/remover_cliente")
def remover_cliente():
    return render_template("remover_cliente.html")

@app.route("/elaborar_proposta")
def elaborar_proposta():
    return render_template("elaborar_proposta.html")

@app.route("/orcamento")
def orcamento():
    return render_template("orcamento.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

@app.route("/adicionar_empresa")
def adicionar_empresa():
    return render_template("adicionar_empresa.html")

@app.route("/alterar_empresa")
def alterar_empresa():
    return render_template("alterar_empresa.html")

@app.route("/remover_empresa")
def remover_empresa():
    return render_template("remover_empresa.html")

@app.route("/proposta", methods=["POST"])
def proposta():
    nome_cliente = request.form.get("cliente")
    dados = {
        "nome_produto": request.form.getlist("nome-prod[]"),
        "tipo_produto": request.form.getlist("tipo-prod[]"),
        "comprimento": request.form.getlist("comprimento[]"),
        "largura": request.form.getlist("largura[]"),
        "altura": request.form.getlist("altura[]"),
        "tipo_isolamento": request.form.getlist("tipo-isolamento[]"),
        "espessura": request.form.getlist("espessura-isolamento[]"),
        "temp_entrada": request.form.getlist("temp-entrada[]"),
        "temp_saida": request.form.getlist("temp-saida[]"),
        "tempo_operacao": request.form.getlist("operacao[]"),
        "mov_diaria": request.form.getlist("mov-diaria[]"),
        "qtd_evaporadores": request.form.getlist("qtd-evaporadores[]"),
        "qtd_portas": request.form.getlist("qtd-portas[]"),
        "qtd_unidade_condensadora": request.form.getlist("qtd-unidcondensadora[]"),
        "tipo_porta": request.form.getlist("tipo-porta[]"),
    }

    dados_cliente = {
        "nome": request.form.get("cliente"),
        "endereco": request.form.get("endereco"),
        "cnpj": request.form.get("cnpj")
    }


    
    criar_proposta2camara(f"{nome_cliente}.pdf", dados, dados_cliente)

    return send_file(f"{nome_cliente}.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)