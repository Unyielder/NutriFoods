function handleCheck() {
        var checkbox_macros = document.getElementById("macrosCheck");
        var checkbox_vitamins = document.getElementById("vitaminsCheck");
        var checkbox_minerals = document.getElementById("mineralsCheck");
        var checkbox_aminos = document.getElementById("aminosCheck");
        var checkbox_surgars = document.getElementById("surgarsCheck");
        var checkbox_steroids = document.getElementById("steroidsCheck");
        var checkbox_misc = document.getElementById("miscCheck");

        var macros_text = document.getElementById("macros");
        var vitamins_text = document.getElementById("vitamins");
        var minerals_text = document.getElementById("minerals");
        var aminos_text = document.getElementById("aminos");
        var surgars_text = document.getElementById("surgars");
        var steroids_text = document.getElementById("steroids");
        var misc_text = document.getElementById("misc");

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

        if(checkbox_aminos.checked == true) {
            aminos_text.style.display = "block";
        } else {
            aminos_text.style.display = "none";
        }

        if(checkbox_surgars.checked == true) {
            surgars_text.style.display = "block";
        } else {
            surgars_text.style.display = "none";
        }

        if(checkbox_steroids.checked == true) {
            steroids_text.style.display = "block";
        } else {
            steroids_text.style.display = "none";
        }

        if(checkbox_misc.checked == true) {
            misc_text.style.display = "block";
        } else {
            misc_text.style.display = "none";
        }
    }