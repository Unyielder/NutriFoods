function handleCheck() {
        var checkbox_macros = document.getElementById("macrosCheck");
        var checkbox_vitamins = document.getElementById("vitaminsCheck");
        var checkbox_minerals = document.getElementById("mineralsCheck");

        var macros_text = document.getElementsById("macros");
        var vitamins_text = document.getElementsById("vitamins");
        var minerals_text = document.getElementsById("minerals");

        if(checkbox_macros.checked == true) {
            macros_text.style.display = "block";
        } else {
            macros_text.style.display = "none";
        }

        if(checkbox_vitamins.checked == true) {
            vitamins_text.style.display = "block";
        } else {
            vitamins_text.style.display = "none";
        }

        if(checkbox_minerals.checked == true) {
            minerals_text.style.display = "block";
        } else {
            minerals_text.style.display = "none";
        }
    }