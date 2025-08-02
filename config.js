// Configuration settings
const SUPPORT_EMAIL = "dkglobaltech@gmail.com";
const LICENSED = true;
const COMPANY_NAME = "Precious Hands";

// Prevent use if not licensed
if (!LICENSED) {
    alert("This system is not licensed. Please contact " + SUPPORT_EMAIL);
    window.location.href = "mailto:" + SUPPORT_EMAIL;
}