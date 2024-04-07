const toggleThemeBtns = document.querySelectorAll(".toggle-theme");

const navIconBtn = document.querySelector(".nav-icon");
const nav = document.querySelector(".nav");
const navCloseBtn = document.querySelector(".nav-close-btn");
const overlay = document.querySelector(".overlay");
const cartOpenBtn = document.querySelector(".cart-icon");
const cartCloseBtn = document.querySelector(".cart-close-btn");
const cart = document.querySelector(".cart");
console.log(overlay)

toggleThemeBtns.forEach(btn => {
    btn.addEventListener("click", function(){

        if (localStorage.theme === "dark"){
            document.documentElement.classList.remove("dark");
            localStorage.theme = "light";
        } else {
            document.documentElement.classList.add("dark");
            localStorage.setItem("theme" , "dark");
        }
    })
})






function closeNav() {
    nav.classList.remove("right-0");
    nav.classList.add("-right-64");
    overlay.classList.add("overlay");
    overlay.classList.remove("overlay--visible");
    
}

function closeCart() {
    cart.classList.remove("left-0");
    cart.classList.add("-left-64");
    overlay.classList.add("overlay");
    overlay.classList.remove("overlay--visible");
    
}

navIconBtn.addEventListener("click", () => {
    nav.classList.remove("-right-64");
    nav.classList.add("right-0");
    overlay.classList.remove("overlay");
    overlay.classList.add("overlay-visible");
    overlay.addEventListener("click", closeNav);

})

cartOpenBtn.addEventListener("click", () => {
    cart.classList.remove("-left-64");
    cart.classList.add("left-0");
    overlay.classList.remove("overlay");
    overlay.classList.add("overlay-visible");
    overlay.addEventListener("click", closeCart);

})

navCloseBtn.addEventListener("click", closeNav);

cartCloseBtn.addEventListener("click", closeCart);

