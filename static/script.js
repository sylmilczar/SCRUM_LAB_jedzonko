document.addEventListener('DOMContentLoaded', function () {

    let to_color = (document.querySelectorAll('.search_yellow'));
    let searched_str = document.getElementById('searched_phrase');

    searched_str = searched_str.innerText;
    searched_str = searched_str.toLowerCase()

    to_color.forEach(function (find) {
        if (find.innerText.toLowerCase().includes(searched_str)) {
            find.innerHTML = find.innerHTML.toLowerCase().replace(searched_str, `<span style="background-color:yellow">${searched_str}</span>`);
        }
    });


});
