from core.bots import TikTokBot
from core import editor
import constants
import eel
import os

# make a tiktok bot
BOT = TikTokBot()
BOT.driver.get('https://www.tiktok.com/login')

# note that you are NOT logged in
LOGGED_IN = False


# make a function to set the login
@eel.expose
def login():
    global LOGGED_IN
    LOGGED_IN = True


# make a function to get the video data
@eel.expose
def get_video_data(link):
    if not LOGGED_IN:
        return {'success': False, 'message': 'You must be log in to tiktok to use this feature.'}

    video = BOT.get_data(link)

    # limit the amount of comments used
    video.comments = [
        comment.__dict__ for comment in video.comments]

    video.comments = sorted(video.comments, key=lambda k: k['likes'], reverse=True)[
        :constants.COMMENT_LIMIT]

    info = video.__dict__

    info['success'] = True

    return info


# make a function to create the video
@eel.expose
def create_video(filename, text):
    # download the video with the bot (reassign based on where the content was moved)
    filename = BOT.download_video(filename)

    # have a borders output
    borders_file = f"{filename.split('.')[0]}_borders.mp4"

    # add borders with the editor
    editor.add_borders(filename, borders_file)

    # take the borders file and add some text --> add to og filename
    editor.add_text(borders_file, filename, text)

    # delete the old file
    os.remove(borders_file)


# make a function to close the bot
@eel.expose
def close_bot():
    BOT.close(0)
