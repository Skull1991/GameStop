mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

    //Active Scroll

    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', scrollActive);



    function scrollActive(){

        const scrollY = window.pageYOffset



        sections.forEach(current => {

            const sectionHeight = current.offsetHeight;

            const sectionTop = current.offsetTop - 10;

            sectionId = current.getAttribute('id');



            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {

                document.querySelector('.navbar-nav a[href*=' + sectionId + ']').classList.add('active')

            } else {

                document.querySelector('.navbar-nav a[href*=' + sectionId + ']').classList.remove('active')

            }

        })

    }