const select = document.getElementById("qtdcamara");
const container = document.getElementById("camaras-container");
const modelo = document.getElementById("modelo-camara");
const tituloGlobal = document.querySelector(".categoria[hidden]");

select.addEventListener("change", () => {
    // Limpa o container antes de gerar novos campos
    container.innerHTML = "";

    let quantidade = parseInt(select.value);
    if (!quantidade) return;

    // Mostra o título "Informações da Câmara"
    tituloGlobal.hidden = false;

    for (let i = 1; i <= quantidade; i++) {
        // 1. Cria o título individual (Câmara 1, Câmara 2...)
        let tituloCamara = document.createElement("p");
        tituloCamara.textContent = `Câmara ${i}`;
        tituloCamara.style.fontWeight = "bold";
        tituloCamara.style.marginTop = "20px";
        container.appendChild(tituloCamara);

        // 2. Cria o Clone do modelo
        let clone = modelo.cloneNode(true);
        clone.hidden = false;
        clone.removeAttribute("id"); // Remove o ID "modelo-camara" do clone

        // 3. Atualiza IDs, nomes e Labels dentro do clone
        clone.querySelectorAll("input, select").forEach(el => {
            // Pegamos o ID original (ex: "nome-prod1") e limpamos o número do fim
            let baseName = el.id.replace(/\d+$/, ''); 
            
            // Reatribuímos o NAME (essencial para o Flask receber os dados)
            el.name = baseName + "[]"; 
            
            // Criamos um ID único (ex: "nome-prod1", "nome-prod2"...)
            el.id = baseName + i;
            el.required = true;
        });

        clone.querySelectorAll("label").forEach(label => {
            if (label.htmlFor) {
                label.htmlFor = label.htmlFor.replace(/\d+$/, '') + i;
            }
        });

        // 4. Adiciona o clone configurado ao container
        container.appendChild(clone);
    }
});