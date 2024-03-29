function sendMail(contactForm) {
    console.log("sending...");
    emailjs.send("gmail", "portfolio-template", {
            "to_name": "Luke",
            "from_name": contactForm.name.value,
            "from_number": contactForm.contactnumber.value,
            "from_email": contactForm.emailaddress.value,
            "message_content": contactForm.messagecontent.value
    })
    .then(
        function (response) {
            console.log("SUCCESS!", response);
            location.reload();
            console.log('Resetting form...');
            console.log('Form reset complete!');
        },
        function (error) {
            console.log("Failed...", error);
        },
    );
    return false;
}

function resetForm() {
    document.getElementById("contact-form").reset;
    console.log('Resetting form...');
    console.log('Form reset complete!');
}
