document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".number-code");

    inputs.forEach((input, index) => {
        input.addEventListener("input", (e) => {
            const value = e.target.value;
            if (!/^\d$/.test(value)) {
                e.target.value = "";
                return;
            }

            if (value.length === 1 && index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        });

        input.addEventListener("keydown", (e) => {
            if (e.key === "Backspace" && !e.target.value && index > 0) {
                inputs[index - 1].focus();
            }
        });

        input.addEventListener("paste", (e) => {
            e.preventDefault();
            const paste = (e.clipboardData || window.clipboardData).getData("text").replace(/\D/g, "").slice(0, 6);
            paste.split("").forEach((char, i) => {
                if (inputs[i]) {
                    inputs[i].value = char;
                }
            });
            const lastFilled = inputs[Math.min(paste.length, inputs.length) - 1];
            if (lastFilled) lastFilled.focus();
        });
    });
});