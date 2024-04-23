const toggleThemeBtns = document.querySelectorAll(".toggle-theme");

const navIconBtn = document.querySelector(".nav-icon");
const nav = document.querySelector(".nav");
const navCloseBtn = document.querySelector(".nav-close-btn");
const overlay = document.querySelector(".overlay");
const cartOpenBtn = document.querySelector(".cart-icon");
const cartCloseBtn = document.querySelector(".cart-close-btn");
const cart = document.querySelector(".cart");
const messeageClose = document.querySelectorAll(".message-close");
const toastMessage = document.querySelectorAll(".toast-message");

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


messeageClose.forEach((btn,i) => {
    btn.addEventListener("click", function(){
        toastMessage[i].style.display = "none";
        
    })
})




function closeNav() {
    nav.classList.remove("right-0");
    nav.classList.add("-right-64");
    if(overlay != null){
    overlay.classList.add("overlay");
    overlay.classList.remove("overlay--visible");
    }
}

function closeCart() {
    cart.classList.remove("left-0");
    cart.classList.add("-left-64");
    if(overlay != null){
    overlay.classList.add("overlay");
    overlay.classList.remove("overlay--visible");
    }
}

navIconBtn.addEventListener("click", () => {
    nav.classList.remove("-right-64");
    nav.classList.add("right-0");
    if(overlay != null){
    overlay.classList.remove("overlay");
    overlay.classList.add("overlay-visible");
    overlay.addEventListener("click", closeNav);
    }
})

cartOpenBtn.addEventListener("click", () => {
    cart.classList.remove("-left-64");
    cart.classList.add("left-0");
    if(overlay != null){
    overlay.classList.remove("overlay");
    overlay.classList.add("overlay-visible");
    overlay.addEventListener("click", closeCart);
    }
})

navCloseBtn.addEventListener("click", closeNav);

cartCloseBtn.addEventListener("click", closeCart);

function cartBoxRefresh(data, urls){
    if(data.item_count == 0){
        let htmlEmptyCartBox = `<div class="text-zinc-700 dark:text-white">سبد خرید خالی است</div>`;
        $('#desktop-cart-box').html(htmlEmptyCartBox);
        $('#mobile-cart-box').html(htmlEmptyCartBox);
        return;
    }
                
    let htmlDesktopCartBox = `<!-- Cart Header -->
                <div class="flex items-center justify-between font-DanaMedium text-xs tracking-tighter">
                    <span class="cart_count text-gray-300">${ data.item_count }</span>
                    <a href="${urls.cart_detail}" class="flex items-center text-orange-300">مشاهده سبد خرید
                        <svg class="w-5 h-5">
                            <use href="#chevron-left">
                            </use>
                        </svg>
                    </a>
                </div>
                <!-- Cart Body -->`;
    let htmlMobileCartBox = `<!-- Cart Body --><div class="child:pb-5 child:mb-5">`;

            
    if(data.cart_ser != null && typeof data.cart_ser[Symbol.iterator] === 'function')
        for(const item of data.cart_ser ){
            htmlDesktopCartBox += `<div
                    class="pb-1 border-b border-b-gray-300 dark:border-white/10 divide-y divide-gray-100 dark:divide-white/10 child:py-5">

                    <div class="flex gap-x-2.5">
                        <img src="${ item.image }" class="w-30 h-30" alt="Product 1">

                        <div class="flex flex-col justify-between">
                            <h4
                                class="font-DanaMedium text-zinc-700 dark:text-white text-base line-clamp-2">
                                ${ item.title }</h4>
                            <div>
                                <span
                    class="text-teal-600 dark:text-emerald-500 font-DanaMedium text-xs tracking-tighter">
                        ${ item.weight } گرمی
                        </span>
                                <div class="text-zinc-700 dark:text-white font-DanaDemiBold">
                                    ${ item.price}
                                    <span class="font-Dana text-sm">تومان</span>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>`;
            htmlMobileCartBox += `
                <div class="flex gap-x-1 border-b border-b-gray-100 dark:border-b-white/10">
                <img src="${ item.image }" class="w-[90px] h-[90px]" alt="Product 1">

                <div class="flex flex-col justify-between gap-y-1.5">
                    <h4 class="font-DanaMedium text-zinc-700 dark:text-white text-sm line-clamp-2">
                        ${ item.title }</h4>
                    <div>
                        <span
                            class="text-teal-600 dark:text-emerald-500 font-DanaMedium text-xs tracking-tighter">
                                ${ item.weight }گرمی
                                </span>
                        <div class="text-zinc-700 dark:text-white font-DanaDemiBold">
                            ${ item.price}
                            <span class="font-Dana text-xs">تومان</span>
                        </div>
                    </div>

                </div>

                </div>`;
        }

                            
    htmlDesktopCartBox += `<!-- Cart Footer -->
        <div class="flex justify-between mt-5">
            <div>
                <span class="font-DanaMedium text-gray-300 text-xs tracking-tighter">مبلغ قابل
                    پرداخت</span>
                <div class="text-zinc-700 dark:text-white font-DanaDemiBold">
                    ${ data.cart_total_price}
                    <span class="font-Dana text-sm">تومان</span>
                </div>
            </div>
            <div>
                <a href="${urls.order_create}"
                    class="flex items-center justify-center w-[144px] h-14 text-white bg-teal-600 dark:bg-emerald-500 dark:hover:bg-emerald-600 hover:bg-teal-700 transition-colors rounded-xl tracking-tighter">ثبت
                    سفارش</a>
            </div>
        </div>`;
    htmlMobileCartBox += `</div><!-- Cart Footer -->
        <div class="flex items-end gap-x-4 mt-auto mb-8">
        <a href="${urls.order_create}"
        class="flex items-center justify-center w-28 h-11 text-white bg-teal-600 dark:bg-emerald-500 dark:hover:bg-emerald-600 hover:bg-teal-700 transition-colors rounded-xl tracking-tighter">ثبت
        سفارش</a>
        <div>
        <span class="font-DanaMedium text-gray-300 text-xs tracking-tighter">مبلغ قابل
            پرداخت</span>
        <div class="text-zinc-700 dark:text-white font-DanaDemiBold">
            ${ data.cart_total_price}
            <span class="font-Dana text-xs">تومان</span>
        </div></div></div>`;
    $('#desktop-cart-box').html(htmlDesktopCartBox);
    $('#mobile-cart-box').html(htmlMobileCartBox);
}