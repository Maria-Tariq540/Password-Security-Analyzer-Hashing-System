console.log("Password Security Platform Loaded");

// Simple UI enhancement
document.addEventListener("DOMContentLoaded", function () {

    const inputs = document.querySelectorAll(".custom-input");

    inputs.forEach(input => {

        input.addEventListener("focus", function () {
            this.style.borderColor = "#38bdf8";
            this.style.boxShadow = "0 0 8px #38bdf8";
        });

        input.addEventListener("blur", function () {
            this.style.boxShadow = "none";
        });

    });

});