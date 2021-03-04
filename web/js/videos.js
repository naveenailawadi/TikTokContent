// add function to delete a video
function deleteRecord(element) {
    id = element.id;
    eel.removeVideo(id);

    // remove the video from the screen
    element.parentNode.parentNode.parentNode.removeChild(element.parentNode.parentNode);

    // don't reload
    return false;
}

// add a function that renders the video template
function renderVideoTemplate(title, channel, comment, videoId) {
    // get the template
    var videoTemplate = $('#video-template').html();

    // get the current table of videos
    var videoTable = $('tbody');

    var newData = {
        title: title,
        channel: channel,
        comment: comment,
        id: videoId
    };

    // render the template with mustache
    videoTable.append(Mustache.render(videoTemplate, newData));


}


// add a function to add a video
async function addVideo() {
    // on save clear all the text boxes and add a new one on the current data
    var title = $('input[name="new-title"]');
    var channel = $('input[name="new-channel"]');
    var comment = $('input[name="new-comment"]');

    // add them to the database
    eel.addVideo(title.val(), channel.val(), comment.val())().then(function (result){
        var videoId = result;

        // render the video template
        renderVideoTemplate(title.val(), channel.val(), comment.val(), videoId);

        // remove the previous data
        formSlots = [title, channel, comment];

        for ( i = 0; i < formSlots.length; i++) {
            formSlots[i].val('');
        }
    });

    // render the video template
    renderVideoTemplate(title.val(), channel.val(), comment.val(), videoId);


    // remove the previous data
    formSlots = [title, channel, comment];

    for ( i = 0; i < formSlots.length; i++) {
        formSlots[i].val('');
    }

    return false;
}


// fill up the table with current video data --> get it first
eel.getVideosDict()().then(function (result){
    // load the videos
    var videos = result.videos;

    for (var i in videos) {
        video = videos[i];

        // add the video via the template
        renderVideoTemplate(video.title, video.creator, video.comment, video.id);
    }

});
