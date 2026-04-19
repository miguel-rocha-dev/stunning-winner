import os
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import date
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
import math

#NO FUTURO SERÁ NECESSÁRIO UM MATCH CASE OU IF PARA VERIFICAR SE SÃO 1, 2 OU 3 CÂMARAS E FAZER A FUNÇÃO DE CADA UMA

#criando caminhos para as fontes
diretorio_base = os.path.dirname(os.path.abspath(__file__))
path_regular = os.path.join(diretorio_base, 'font', 'montserrat_reg.ttf')
path_bold = os.path.join(diretorio_base, 'font', 'montserrat_bold.ttf')
path_italico = os.path.join(diretorio_base, 'font', 'montserrat_italic.ttf')
pdfmetrics.registerFont(TTFont('Montserrat-Italico', path_italico))
pdfmetrics.registerFont(TTFont('Montserrat', path_regular))
pdfmetrics.registerFont(TTFont('Montserrat-Bold', path_bold))
data = str(date.today().strftime('%d/%m/%Y'))

#criando caminhos para as imagens
path_onda = os.path.join(diretorio_base, 'static/img', 'onda_indices.png')
path_footer = os.path.join(diretorio_base, 'static/img', 'footer_indice.png')
path_cabecalho_capa = os.path.join(diretorio_base, 'static/img', 'cabecalho_capa.png')
path_logo = os.path.join(diretorio_base, 'static/img', 'logo_glc.png')
path_instagram = os.path.join(diretorio_base, 'static/img', 'instagram_logo.png')
path_whatsapp = os.path.join(diretorio_base, 'static/img', 'whatsapp_logo.png')
path_internet = os.path.join(diretorio_base, 'static/img', 'internet_logo.png')

width, height = A4

def capa(c,nome_cliente):
    #capa
    c.drawImage(path_cabecalho_capa, 0, height - 3.5 * cm, height= 3.5 * cm, width = width, mask='auto')
    c.drawImage(path_logo, 0.4 *cm, height - 1.8 * cm - 0.9 * cm, height= 1.8 * cm, width = 3.6 * cm, mask='auto')
    #texto da parte de cima esquerda
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('Montserrat', 16.1)
    c.drawString(4.5 * cm, height - 0.6 * cm - 16.1, 'PROPOSTA TÉCNICA E')
    c.drawString(4.5 * cm, height - 1.4 * cm - 16.1, 'COMERCIAL:')
    c.setFont('Montserrat-Italico', 11.1)
    c.drawString(4.5 * cm, height - 2.3 * cm - 11.1, nome_cliente)

    #texto da parte de cima direita
    c.setFont('Montserrat-Bold', 8.3)
    c.drawString(18 * cm, height - 0.6 * cm - 8.3, 'N° PROPOSTA:')
    c.drawString(18.6 * cm, height - 1.8 * cm - 8.3, 'DATA:')
    c.setFont('Montserrat', 7.9)
    c.drawString(18.6 * cm, height - 1.1 * cm - 7.9, "00000")
    c.drawString(18.3 * cm, height - 2.3 * cm - 7.9, data)

    #footer
    c.setFillColor(HexColor('#00297c'))
    c.rect(0, 0, width, 1.6 * cm, fill=True, stroke=False)

    #imagens do footer
    c.drawImage(path_instagram, 3.8 * cm, 0.5 * cm, width=0.7 * cm, height=0.7 * cm, mask='auto')
    c.drawImage(path_whatsapp, 8 * cm, 0.5 * cm, width=0.7 * cm, height=0.7 * cm, mask='auto')
    c.drawImage(path_internet, 12.5 * cm, 0.5 * cm, width=0.7 * cm, height=0.7 * cm, mask='auto')

    #textos do footer
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('Montserrat', 8.6)
    c.drawString(4.6 * cm, 0.8 * cm, "glcrefrigeracao")
    c.drawString(8.8 * cm, 0.8 * cm, "+55 85 99139-1800")
    c.drawString(13.3 * cm, 0.8 * cm, "www.glcrefrigeracao.com.br")

def paragrafo(c, tamanho_fonte, largura, altura, x, y, frase):
    estilo = ParagraphStyle(
        name='Estilo_paragrafo',
        fontName='Montserrat',
        fontSize=tamanho_fonte,
        leading= math.ceil(tamanho_fonte * 1.2),  #espaço que vai ter entre as linhas
        alignment=TA_JUSTIFY  #deixa o texto jsutificado
    )

    texto = (
        frase
    )

    p = Paragraph(texto, estilo) #atribui o estilo e o texto à variável p
    largura_limite = largura #largura do campo de texto
    altura_limite = altura #altura do campo de texto
    p.wrap(largura_limite, altura_limite)
    p.drawOn(c, x, y)

def capa_indice(c):
    c.drawImage(path_cabecalho_capa, 0, height - 3.5 * cm, height= 3.5 * cm, width = width, mask='auto')
    c.setFillColor(HexColor('#FFFFFF')) 
    c.setFont('Montserrat-Bold', 29.8)
    c.drawString(2.1 * cm, height - 1.2 * cm - 29.8, 'Índice')
    c.drawImage(path_logo, width - 1 * cm - 3.6 * cm, height - 1.8 * cm - 0.9 * cm, height= 1.8 * cm, width = 3.6 * cm, mask='auto')
    
    #índices
    c.setFillColor(HexColor('#000000'))
    c.setFont('Montserrat-Bold', 16.8)
    c.drawImage("static/img/proposta.png", 2.1 * cm, height - 6.4 * cm - 2.1 * cm, height= 2.1 * cm, width = 2.1 * cm, mask='auto')
    c.drawString(4.6 * cm, height - 7.3 * cm - 16.8, 'PROPOSTA TÉCNICA E COMERCIAL')
    c.drawImage("static/img/materiais.png", 2.1 * cm, height - 9.8 * cm - 2.1 * cm, height= 2.1 * cm, width = 2.1 * cm, mask='auto')
    c.drawString(4.6 * cm, height - 10.5 * cm - 16.8, 'DESCRIÇÃO TÉCNICA E MATERIAIS')
    c.drawImage("static/img/logistica.png", 2.1 * cm, height - 13.1 * cm - 2.1 * cm, height= 2.1 * cm, width = 2.1 * cm, mask='auto')
    c.drawString(4.6 * cm, height - 13.9 * cm - 16.8, 'LOGÍSTICA E GARANTIA')
    c.drawImage("static/img/financeiro.png", 2.1 * cm, height - 16.5 * cm - 2.1 * cm, height= 2.1 * cm, width = 2.1 * cm, mask='auto')
    c.drawString(4.6 * cm, height - 17.2 * cm - 16.8, 'ORÇAMENTO E OBSERVAÇÕES')

    #footer
    c.drawImage(path_footer, 0, -1, width= 21.5 * cm, height = 4.9 * cm, mask= 'auto')
    
def tabelas_cliente(c, x, y, dados_cliente):
    #criando as informações necessárias pra a criação da tabela de CLIENTES'
    col_widths_cliente = [4.2 * cm, 12.5 * cm]
    row_heights_cliente = [1.2 * cm, 1.2 * cm, 1.2 * cm]
    dados_cliente_tabela=[
    ["Cliente", dados_cliente["nome"]],
    ["Endereço", dados_cliente["endereco"]],
    ["CNPJ", dados_cliente["cnpj"]],
    ]
    tabela_cliente = Table(dados_cliente_tabela, colWidths=col_widths_cliente, rowHeights=row_heights_cliente)
    style = TableStyle([
        #fundo
        ('BACKGROUND', (0,0), (-1,-1), HexColor("#2e6193")),

        #borda
        ('GRID', (0,0), (-1,-1), 1, HexColor("#ffffff")),

        #texto
        ('TEXTCOLOR', (0,0), (-1,-1), HexColor("#ffffff")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'), #alinha horizontalmente
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), #alinha verticalmente
        ('FONTNAME', (0,0), (0,-1), 'Montserrat-Bold'),
        ('FONTNAME', (1,0), (0,-1), 'Montserrat'),
        ('FONTSIZE', (0,0), (-1,-1), 11),

    ])
    tabela_cliente.setStyle(style)
    tabela_cliente.wrapOn(c, width, height)
    tabela_cliente.drawOn(c, x, y)

def tabelas_camara(c, x, y, dados):
    #criando as informações necessárias pra a criação da tabela de CAMARAS
    col_widths_camara = [3.5 * cm, 3.2 * cm, 2.6 * cm, 3.3 * cm, 3.8 * cm]
    row_heights_camara = [1.6 * cm, 1.2 * cm, 1.2 * cm, 1.2 * cm, 1.2 * cm, 1.2 * cm]

    dados_camara = [
        ["INFORMAÇÕES DA CÂMARA", "", "", "", ""],
        ["MEDIDAS EXTERNAS", "", "", "ISOLAMENTO TÉRMICO", ""],
        ["COMPRIMENTO", "LARGURA", "ALTURA", "TIPO", "ESPESSURA"],
        [f"{dados['comprimento']}m", f"{dados['largura']}m", f"{dados['altura']}m", dados["tipo_isolamento"], dados["espessura"]],
        ["PRODUTO", "MOV. DIÁRIA", "OPERAÇÃO", "TEMP ENTRADA", "TEMP SAÍDA"],
        [dados["tipo_produto"], f"{dados['mov_diaria']}h", f"{dados['tempo_operacao']}h", f"{dados["temp_entrada"]}°C", f"{dados["temp_saida"]}°C"]
    ]
    tabela_camara = Table(dados_camara, colWidths=col_widths_camara, rowHeights=row_heights_camara)
    style = TableStyle([
    #mesclagens
    ('SPAN', (0,0), (-1,0)), # SPAN serve para mesclar células. sintaxe: ('SPAN', (coluna,linha), (coluna,linha)) <- a , serve como um sinal de +
    ('SPAN', (0,1), (2,1)),
    ('SPAN', (3,1), (4,1)),

    #fundos
    ('BACKGROUND', (0,0), (-1,0), HexColor("#00297c")),
    ('BACKGROUND', (0,1), (-1,1), HexColor("#00569e")),
    ('BACKGROUND', (0,2), (-1,-1), HexColor("#2e6193")),

    #texto
    ('TEXTCOLOR', (0,0), (-1,-1), HexColor("#ffffff")),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

    #fonte 
    ('FONTNAME', (0,0), (-1,-1), 'Montserrat-Bold'),

    ('FONTSIZE', (0,0), (-1,-1), 8.3),

    #bordas
    ('GRID', (0,0), (-1,-1), 1, HexColor("#ffffff")),

    # Padding fino (mais fiel)
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ])

    tabela_camara.setStyle(style)

    tabela_camara.wrapOn(c, width, height)
    tabela_camara.drawOn(c, x, y)

def tabela_material(c, x, y, titulo2, camaras): #o titulo é isolante ou materiais
    #criando as metragens necessárias pra fazer a tabela de materiais
    col_widths_material = [13 * cm, 3.8 * cm]
    row_heights_material = [1.3 * cm, 1.3 * cm, 1.3 * cm, 1.3 * cm]
    style = TableStyle([
        #colocando cor na tabela
        ('BACKGROUND', (0,0), (-1,0), HexColor("#00297c")),
        ('BACKGROUND', (0,1), (-1,-1), HexColor("#2e6193")),
        #colocando divisoria da tabela
        ('GRID', (0, 0), (-1, -1), 1, HexColor("#FFFFFF")),
        #texto
        ('TEXTCOLOR', (0, 0), (-1, -1), HexColor("#fffbfb")),
        ('FONTNAME', (0, 0), (-1, -1), 'Montserrat-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12.3),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'), #alinha horizontalmente
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), #alinha verticalmente
    ])
    
    if titulo2 == "isolante":
        paineis_formatados = [f"{c['tipo_isolamento']} {c['espessura']}" for c in camaras]
        texto_paineis = ", ".join(set(paineis_formatados))
        #juntando os títulos
        style.add('SPAN', (0,0), (-1,0)) 
        style.add('SPAN', (0,1), (-1,1))
        style.add('SPAN', (0,2), (-1,2))
        style.add('SPAN', (0,3), (-1,3))

        
        lista_pisos = []
        for camara in camaras:
            if camara['tipo_produto'] == "Congelado":
                lista_pisos.append("E.P.S 200mm")
            else:
                lista_pisos.append("E.P.S 100mm")
        dados_material = [
            ["MATERIAIS ISOLANTES TÉRMICOS", ""],
            [f"Painéis de {texto_paineis}", ""],
            [f"Piso {', '.join(set(lista_pisos))}", ""],
            ["Cantoneiras de acabamento externo e interno", ""]
        ]
        tabela_material = Table(dados_material, colWidths=col_widths_material, rowHeights=row_heights_material)
            
        tabela_material.setStyle(style)
        tabela_material.wrapOn(c, width, height)
        tabela_material.drawOn(c, x, y)
    else:
        total_condensadoras = sum(int(camara['qtd_unidade_condensadora']) for camara in camaras)
        total_portas = sum(int(camara['qtd_portas']) for camara in camaras)
        total_evaporadores = sum(int(camara['qtd_evaporadores']) for camara in camaras)
        tipo_porta = [f"{camara['tipo_porta']}" for camara in camaras]
        texto_porta = ", ".join(set(tipo_porta))
        dados_material = [
                ["MAQUINÁRIOS E PORTAS", "QUANTIDADE"],
                ["Unidade Condensadora", f"{total_condensadoras}"],
                ["Evaporadores", f"{total_evaporadores}"],
                [f"Portas {texto_porta}", f"{total_portas}"],
            ]
        tabela_material = Table(dados_material, colWidths=col_widths_material, rowHeights=row_heights_material)
        tabela_material.setStyle(style)
        tabela_material.wrapOn(c, width, height)
        tabela_material.drawOn(c, x, y)
    

def cabecalho_indice(c, path_imagem_indice, texto1_indice, texto2_indice):
    #coloca o retangulo azul
    c.setFillColor(HexColor('#00297c'))
    c.rect(0, height - 4.8 * cm, width, 4.8 * cm, fill=True, stroke=False)

    #aqui é a imagem do index
    c.drawImage(path_imagem_indice, 1.3 * cm, height - 3.1 * cm - 0.9 *cm, width=3 * cm, height=3.1 * cm, mask='auto')
    
    #aqui é onde fica a onda da parte da direita
    
    c.drawImage(path_onda, 16 * cm, height - 4.8 * cm, width=5 * cm, height=4.8 * cm, mask='auto')
    
    #iniciando rotação da onda da parte inferior esquerda
    c.saveState() #salva o pdf como está antes da rotação
    c.translate(0, height - 2.8 * cm) #colocou como o nova coordenada o ponto superior esquerdo da imagem da onda
    c.rotate(180) # gira 180 graus
    #aqui é onde fica a onda da parte da inferior esquerda
    c.drawImage(path_onda, -2.1 * cm, -0.1 * cm, width=2.1 * cm, height=2.1 * cm, mask='auto')  
    
    c.restoreState()#volta para o padrão, agora a coordenada volta a ser o ponto inferior esquerdo da página
    
    #aqui vai começar a escrever o texto
    c.setFillColor(HexColor('#FFFFFF')) #define a cor que vai ser o texto
    c.setFont('Montserrat-Bold', 21.7) #define a fonte e o tamanho
    c.drawString(5 * cm, height - 1.3 * cm - 21.7, texto1_indice) #texto1
    c.drawString(5 * cm, height - 2.3 * cm - 21.7, texto2_indice) #texto2
    
    #colocar o footer
    c.drawImage(path_footer, 0, -1, width= 21.5 * cm, height = 4.9 * cm, mask= 'auto')

def criar_proposta2camara(nome_arquivo, dados, dados_cliente):
    nome_cliente = dados_cliente["nome"]
    endereco_cliente = dados_cliente["endereco"]
    cnpj_cliente = dados_cliente["cnpj"]
    camaras = []
    nome =[]

    for i in range(len(dados["nome_produto"])):
        camara = {
            "tipo_produto": dados["tipo_produto"][i],
            "mov_diaria": dados["mov_diaria"][i],
            "tempo_operacao": dados["tempo_operacao"][i],
            "comprimento": dados["comprimento"][i],
            "largura": dados["largura"][i],
            "altura": dados["altura"][i],
            "tipo_isolamento": dados["tipo_isolamento"][i],
            "espessura": dados["espessura"][i],
            "temp_entrada": dados["temp_entrada"][i],
            "temp_saida": dados["temp_saida"][i],
            "qtd_evaporadores": dados["qtd_evaporadores"][i],
            "qtd_portas": dados["qtd_portas"][i],
            "qtd_unidade_condensadora": dados["qtd_unidade_condensadora"][i],
            "tipo_porta": dados["tipo_porta"][i],
        }
        camaras.append(camara)
        nome_prod ={
            "nome_produto": dados["nome_produto"][i],
        }
        nome.append(nome_prod)
    primeiro_tipo_produto = camaras[0]["tipo_produto"]
    primeiro_nome_produto = nome[0]["nome_produto"]
    c = canvas.Canvas(nome_arquivo, pagesize=A4)

    capa(c, nome_cliente)#pag 1 (capa)

    c.showPage() # separa a página uma da outra
    capa_indice(c) # pag 2 (capa indice)

    c.showPage()
    cabecalho_indice(c, "static/img/proposta.png", "PROPOSTA TÉCNICA", "E COMERCIAL" ) #página 3
    c.setFillColor(HexColor('#000000'))
    c.setFont('Montserrat-Bold', 18.9)
    c.drawString(2 * cm, height - 6.1 * cm - 18.9, "1. DADOS DO CLIENTE")
    c.drawString(2 * cm, 12 *cm, "2. DADOS DA CÂMARA")
    tabelas_cliente(c, 2*cm, height - 7.3 * cm - 3.7 * cm, dados_cliente)
    
    if(len(camaras) == 1):
        texto1 = f"""
        Conforme solicitado, apresentamos a proposta técnica para a câmara frigorífica 
        destinada ao armazenamento de <font name='Montserrat-Bold'>{primeiro_nome_produto}</font> do tipo <font name='Montserrat-Bold'>{primeiro_tipo_produto}</font>, 
        priorizando a eficiência energética e a perfeita conservação da sua carga. 
        Seguem ao decorrer da proposta os detalhamentos.
        """
        paragrafo(c, 12.9, 16.7 * cm, 3.7 * cm, 1.9 * cm, height - 12*cm - 3.7 *cm, texto1)
    if(len(camaras) == 2):
        segundo_nome_produto = nome[1]["nome_produto"]
        segundo_tipo_produto = camaras[1]["tipo_produto"]
        texto2 =  f"""
        Conforme solicitado, apresentamos a proposta técnica para duas câmaras frigoríficas. 
        Uma destinada ao armazenamento de <font name='Montserrat-Bold'>{primeiro_nome_produto}</font> do tipo <font name='Montserrat-Bold'>{primeiro_tipo_produto}</font> 
        e outra câmara destinada ao armazenamento de <font name='Montserrat-Bold'>{segundo_nome_produto}</font> 
        do tipo <font name='Montserrat-Bold'>{segundo_tipo_produto}</font>. 
        Priorizando a eficiência energética e a perfeita conservação da sua carga. 
        Seguem ao decorrer da proposta os detalhamentos.
        """
        paragrafo(c, 12.9, 16.7 * cm, 3.7 * cm, 1.9 * cm, height - 12*cm - 3.7 *cm, texto2)
    if(len(camaras)== 3):
        segundo_nome_produto = nome[1]["nome_produto"]
        segundo_tipo_produto = camaras[1]["tipo_produto"]
        terceiro_nome_produto = nome[2]["nome_produto"]
        terceiro_tipo_produto = camaras[2]["tipo_produto"]
        texto3 =  f"""
        Conforme solicitado, apresentamos a proposta técnica para três câmaras frigoríficas. 
        Uma destinada ao armazenamento de <font name='Montserrat-Bold'>{primeiro_nome_produto}</font> do tipo <font name='Montserrat-Bold'>{primeiro_tipo_produto}</font>, 
	    outra câmara destinada ao armazenamento de <font name='Montserrat-Bold'>{segundo_nome_produto}</font> 
        do tipo <font name='Montserrat-Bold'>{segundo_tipo_produto}</font> e a última para armazenamento de <font name='Montserrat-Bold'>{terceiro_nome_produto}</font> 
	    do tipo <font name='Montserrat-Bold'>{terceiro_tipo_produto}</font>. 
        Priorizando a eficiência energética e a perfeita conservação da sua carga. 
        Seguem ao decorrer da proposta os detalhamentos.
        """
        paragrafo(c, 12.9, 16.7 * cm, 3.7 * cm, 1.9 * cm, height - 12*cm - 3.7 *cm, texto3)
    tabelas_camara(c, 2 *cm, 3.6 * cm, camaras[0]) # primeira cãmara


    c.showPage() #separa a página uma da outra
    if(len(camaras) == 2):
        cabecalho_indice(c, "static/img/proposta.png", "PROPOSTA TÉCNICA", "E COMERCIAL" )
    
        tabelas_camara(c, 2 *cm, height - 6.1 * cm - 8 * cm, camaras[1])
        c.showPage()
    if(len(camaras) == 3):
        cabecalho_indice(c, "static/img/proposta.png", "PROPOSTA TÉCNICA", "E COMERCIAL" )
    
        tabelas_camara(c, 2 *cm, height - 6.1 * cm - 8 * cm, camaras[1])
        tabelas_camara(c, 2 *cm, height - 15.2 * cm - 8 * cm, camaras[2])
        c.showPage()
        

    cabecalho_indice(c, "static/img/materiais.png", "DESCRIÇÃO TÉCNICA", "E MATERIAIS" ) # página 4
    c.setFillColor(HexColor('#000000'))
    c.setFont('Montserrat-Bold', 18.9)
    c.drawString(2 * cm, height - 6.1 * cm - 18.9, "2. MATERIAIS UTILIZADOS")
    c.setFont('Montserrat-Bold', 13.8)
    c.drawString(2 * cm, height - 13.8 - 8.1 * cm, "2.1 MÁQUINAS E PORTAS")
    c.drawString(2 * cm, height - 16.7 * cm - 13.8, "2.2 MATERIAL DE ISOLAMENTO TÉRMICO")
    tabela_material(c, 2 * cm, height - 9.1 * cm - 5.3 * cm, "maquinário", camaras)
    tabela_material(c, 2 * cm, height - 17.8 * cm - 5.3 * cm, "isolante", camaras)
    c.showPage()
    cabecalho_indice(c, "static/img/materiais.png", "DESCRIÇÃO TÉCNICA", "E MATERIAIS" )
    c.setFillColor(HexColor('#000000'))
    c.setFont('Montserrat-Bold', 17.8)
    c.drawString(2.1 * cm, height - 17.8 - 6 * cm, "2.2.1 PISO E.P.S")
    c.drawString(2.1 * cm, height - 17.8 - 17 * cm, "2.2.1 PAINEL P.I.R")
    piso_eps = """
        Solução versátil, excelente para câmaras de resfriados e áreas de climatização controlada. 
        Composto por núcleo de Poliestireno Expandido (E.P.S.) de alta densidade e revestimento em aço galvanizado. 
        Espessura ideal para manutenção de temperaturas positivas e áreas de processamento. 
        Além de contar com superfícies lisas e laváveis, atendendo às normas sanitárias vigentes.
    """
    painel_pir = """
        Solução versátil, excelente para câmaras de resfriados e áreas de climatização controlada. 
        Composto por núcleo de Poliestireno Expandido (E.P.S.) de alta densidade e revestimento em aço galvanizado. 
        Espessura ideal para manutenção de temperaturas positivas e áreas de processamento. 
        Além de contar com superfícies lisas e laváveis, atendendo às normas sanitárias vigentes.
    """
    paragrafo(c, 12.9, 16.9 * cm, 3.7 * cm, 2.1 * cm, height - 7.4 * cm - 3.7 * cm, piso_eps)
    

    #começar a criar a página de explicação do material
    
    #cria o pdf e salva
    c.save()
    print(f"PDF gerado com ReportLab: {nome_arquivo}")
    
if __name__ == "__main__":
    print("Execute via Flask")