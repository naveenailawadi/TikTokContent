// add function to delete a user
function deleteRecord(element) {
    id = element.id;
    eel.removeUser(id);

    // remove the user from the screen
    element.parentNode.parentNode.parentNode.removeChild(element.parentNode.parentNode);

    // don't reload
    return false;
}

// add a function that renders the video template
function renderAccountTemplate(email, emailPassword, host, port,
                                proxyUsername, proxyPassword, recoveryEmail, userId) {
    // get the template
    var accountTemplate = $('#user-template').html();

    // get the current table of videos
    var accountTable = $('tbody');

    var newData = {
        email: email,
        emailPassword: emailPassword,
        host: host,
        port: port,
        proxyUsername: proxyUsername,
        proxyPassword: proxyPassword,
        recoveryEmail: recoveryEmail,
        id: userId
    };

    // render the template with mustache
    accountTable.append(Mustache.render(accountTemplate, newData));
}


// add a function to add a user
async function addUser() {
    // on save clear all the text boxes and add a new one on the current data
    var email = $('input[name="new-email"]');
    var emailPassword = $('input[name="new-email-password"]');
    var host = $('input[name="new-host"]');
    var port = $('input[name="new-port"]');
    var proxyUsername = $('input[name="new-proxy-username"]');
    var proxyPassword = $('input[name="new-proxy-password"]');
    var recoveryEmail = $('input[name="new-recovery-email"]');

    // add them to the database
    eel.addUser(email.val(), emailPassword.val(), host.val(), port.val(),
        proxyUsername.val(), proxyPassword.val(), recoveryEmail.val())().then(function (result) {
            // get the user id
            var userId = result;

            // render the account template
            renderAccountTemplate(email.val(), emailPassword.val(), host.val(), port.val(),
                                  proxyUsername.val(), proxyPassword.val(), recoveryEmail.val(), userId);


            // remove the previous data
            formSlots = [email, emailPassword, host, port,
                        proxyUsername, proxyPassword, recoveryEmail];

            for ( i = 0; i < formSlots.length; i++) {
                formSlots[i].val('');
            }
        });

    return false;
}


// fill up the table with current video data --> get it first
eel.getAccountsDict()().then(function (result){
    // load the accounts
    var accounts = result.accounts;

    for (var i in accounts) {
        account = accounts[i];

        // add the account via the template
        renderAccountTemplate(account.email, account.password, account.proxy, account.port,
                                account.user, account.passw, account.recovery_mail, account.id);
    }

});
