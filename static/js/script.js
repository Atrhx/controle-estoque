const modal = document.getElementById("modalCadastro");
const abrirModal = document.getElementById("abrirModal");
const fecharModal = document.getElementById("fecharModal");

abrirModal.addEventListener("click", function () {
    modal.style.display = "flex";
});

fecharModal.addEventListener("click", function () {
    modal.style.display = "none";
});

modal.addEventListener("click", function (evento) {
    if (evento.target === modal) {
        modal.style.display = "none";
    }
});

document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape") {
        modal.style.display = "none";
        modalEditar.style.display = "none";
    }
});

const formulariosRemover = document.querySelectorAll(".form-remover");

formulariosRemover.forEach(function (formulario) {
    formulario.addEventListener("submit", function (evento) {
        const confirmar = confirm("Deseja realmente remover este produto?");

        if (!confirmar) {
            evento.preventDefault();
        }
    });
});

const modalEditar = document.getElementById("modalEditar");
const fecharModalEditar = document.getElementById("fecharModalEditar");

const editarNome = document.getElementById("editarNome");
const editarCodigo = document.getElementById("editarCodigo");
const editarQuantidade = document.getElementById("editarQuantidade");

const formEditar = document.getElementById("formEditar");

const botoesEditar = document.querySelectorAll(".botao-editar");

botoesEditar.forEach(function (botao) {
    botao.addEventListener("click", function () {

        const codigo = botao.dataset.codigo;
        const nome = botao.dataset.nome;
        const quantidade = botao.dataset.quantidade;

        editarNome.value = nome;
        editarCodigo.value = codigo;
        editarQuantidade.value = quantidade;

        formEditar.action = `/editar/${codigo}`;

        modalEditar.style.display = "flex";
    });
});

fecharModalEditar.addEventListener("click", function() {
    modalEditar.style.display = "none";
});

modalEditar.addEventListener("click", function (evento) {
    if (evento.target === modalEditar) {
        modalEditar.style.display = "none";
    }
});