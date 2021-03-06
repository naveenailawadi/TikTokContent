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

// make functions for handling captions

// make a function for clearing options
function clearOptions() {
    var captionSelections = $('#captionOptions');
    var captionRow = $('#chooseCaption');

    // clear and hide the row
    captionSelections.empty();
    captionRow.hide();

}

// make a function to add a caption to the selection list
// pass the string --> able to create an element out of it
function addCaptionOption(caption) {
    // find the row with caption information
    var captionSelections = $('#captionOptions');

    // make the html element
    var captionOption = '<p><button class="btn btn-warning" onclick="fillCaption(this);">' + caption +
    '</button></p>';

    captionSelections.append(captionOption);

}

// make a function to add a caption to the caption textbox
// passing a element --> get the text out of it
function fillCaption(caption) {
    console.log(caption.innerText);
    // add the caption (passed by html) to the caption bar
    var captionBar = $('#caption');

    // set the caption bar data to the caption set
    captionBar.val(caption.innerText);

    return caption;
}


//  make functions to get information from python

// make a function to maxrate posts in a csv
function getVideoData () {
    // get the post url
    var link = $('#postURL');

    displayMessage('Getting Post Data...');

    // send the post URL to the function
    eel.get_video_data(link.val())().then(function (result) {
        console.log(result);

        // use the result to check
        if (!result.success) {
            displayMessage(result.message)

            return false;
        }

        // add the main video caption
        addCaptionOption(result.caption);

        // add the captions based on video data
        for (i = 0; i < result.comments.length; i += 1)
        {
            addCaptionOption(result.comments[i].text)
        }

        // show the caption row
        var captionRow = $('#chooseCaption');
        captionRow.show();

        // add something to the message board
        displayMessage('');

    });

    return false;
}

// make a function to send gems to an account
function createVideo () {
    var fileElem = $("#filename");
    var caption = $('#caption');
    var choiceBox = $('#captionOptions');
    var captionRow = $('#chooseCaption');

    if (fileElem.val().length < 1) {
        displayMessage('Please assign a filename before creating the video');

        return false;
    }

    // set the filename
    var filename = fileElem.val().split('.')[0] + '.mp4';

    displayMessage('Creating Video with filename: ' + filename + '');

    // clear the options
    clearOptions();

    // send the post URL to the function
    eel.create_video(filename, caption.val())().then(function (result) {
        // add something to the message board
        var message = 'Created ' + filename.val() + ' with caption ' + caption.val();
        displayMessage(message);

        // clear the selections
        choiceBox.empty();

        // hide the row
        captionRow.hide();

    });

    return false;
}
