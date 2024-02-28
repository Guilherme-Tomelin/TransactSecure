document.addEventListener("DOMContentLoaded", function() {
    var fileDrag = document.getElementById("file-drag");
    var fileUpload = document.getElementById("file-upload");

    fileDrag.addEventListener("dragover", function(event) {
        event.preventDefault();
        event.stopPropagation();
        fileDrag.classList.add("drag-over");
    });

    fileDrag.addEventListener("dragleave", function(event) {
        event.preventDefault();
        event.stopPropagation();
        fileDrag.classList.remove("drag-over");
    });

    fileDrag.addEventListener("drop", function(event) {
        event.preventDefault();
        event.stopPropagation();
        fileDrag.classList.remove("drag-over");
        var files = event.dataTransfer.files;
        fileUpload.files = files;
        if (files.length > 0) {
            fileDrag.textContent = files[0].name;
        }
    });

    fileUpload.addEventListener("change", function(event) {
        if (fileUpload.files.length > 0) {
            fileDrag.textContent = fileUpload.files[0].name;
        }
    });

});
