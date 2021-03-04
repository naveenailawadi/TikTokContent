// make a function to maxrate a post
function login() {
    var loginTable = $('#loginTable');
    var mainTable = $('#mainTable');

    // send the login confirmation to the function
    eel.login()().then(function (result) {

        // add something to the message board
        displayMessage('Successfully noted your login.');

        // hide and show the correct tables
        loginTable.hide();
        mainTable.show();

    });

    return false;
}

// make a function to maxrate posts in a csv
function getVideoData () {
    // get the post url
    var link = $('#filepath');

    displayMessage('Getting Post Data...');
    // send the post URL to the function
    eel.get_video_data(link.val())().then(function (result) {

        // add something to the message board
        displayMessage('');

        // clear the box
        filepath.val('');

    });

    return false;
}

// make a function to send gems to an account
function createVideo () {
    var filename = $("#filename");
    var caption = $("input[name='caption']:checked");
    var choiceBox = $('#choiceBox');

    displayMessage('Creating Video...');
    // send the post URL to the function
    eel.send_many_gems(filename.val(), caption.val())().then(function (result) {
        // add something to the message board
        var message = 'Created ' + filename.val() + ' with caption ' + caption.val();
        displayMessage(message);

        // clear the radio buttons
        choiceBox.empty();

    });

    return false;
}
