var input = document.getElementById("searchInput");
var tableBody = document.getElementById("customerTableBody");
var staffViewBtn = document.getElementById("toggle-staff-view");

input.addEventListener("keyup", function () {
    var query = input.value.toLowerCase();

    var rows = tableBody.getElementsByTagName("tr");
    for (var i = 0; i < rows.length; i++) {
        row = rows[i]
        if (row.innerText.toLowerCase().includes(query)) {
            row.style.display = ""
        } else {
            row.style.display = "none"
        }
    }

});