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