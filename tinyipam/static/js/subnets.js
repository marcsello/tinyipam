$( document ).ready(function() {
    let searchParams = new URLSearchParams(window.location.search)

    if (searchParams.get("action") === "new") {
        $('#newSubnetDialog').modal()
    }

});