
function showNav(mobileNav) {
    mobileNav.classList.add('mobileExtraNavAForward');
    mobileNav.classList.remove('hideNav');
    mobileNav.classList.add('showNav');
    setTimeout(()=>{
        mobileNav.classList.remove('mobileExtraNavAForward');
    }, 500);
}

function hideNav(mobileNav) {
    mobileNav.classList.add('mobileExtraNavABackward');
    mobileNav.classList.remove('showNav');
    mobileNav.classList.add('hideNav');
    setTimeout(()=>{
        mobileNav.classList.remove('mobileExtraNavABackward');
    }, 500);
}

function expandNavForMobile() {
    const mobileNav = document.getElementById('mobileExtraNav');
    const classList = Array.from(mobileNav.classList);
    classList.find(item => item === 'hideNav') !== undefined ? showNav(mobileNav) : hideNav(mobileNav);
}