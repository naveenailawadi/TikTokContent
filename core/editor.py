from constants import DEFAULT_BORDER, DEFAULT_FONT
from moviepy.editor import *


# wrap the editor in a movie object
class Movie:
    def __init__(self, filename):
        # set the filename
        self.filename = filename

    # rewrite the video
    def rewrite(self, new_video):
        new_video.write_videofile(self.filename)

    # make a function to add right and left borders
    def add_rl_borders(self, border=DEFAULT_BORDER):
        # make a video clip
        clip = VideoFileClip('sample.mp4')

        # add the borders
        clip_with_borders = clip.margin(right=border, left=border)

        # rewrite the video
        self.rewrite(clip_with_borders)

    # make a function to add text
    def add_text(self, text, font=DEFAULT_FONT, position=DEFAULT_POSITION):
        # open the video
        video = VideoFileClip(self.filename)

        # make a textclip
        txt_clip = TextClip(text, fontsize=FONT,
                            color='white').with_position('center')

        # combine them
        result = CompositeVideoClip([video, txt_clip])
        self.rewrite(result)
