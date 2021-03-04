// make a function to maxrate a post
function createAccounts () {
    // get the post url
    var exportFile = $('#exportFile');
    var amount = $('#amount');

    displayMessage('Creating accounts...');
    // send the post URL to the function
    eel.create_accounts(amount.val(), exportFile.val())().then(function (result) {
        // add something to the message board
        displayMessage(result);

        // clear the box
        exportFile.val('');
        amount.val('');

    });

    return false;
}
