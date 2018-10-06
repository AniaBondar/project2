document.addEventListener('DOMContentLoaded', () => {

    if (localStorage.getItem('display_name'))
        window.location = "/channels";

    document.querySelector('#form').onsubmit = () => {



    };

});
