import constants
from moviepy.editor import *


# rewrite the video
def rewrite(new_video, new_filepath):
    new_video.write_videofile(new_filepath)


# make a function to add right and left borders
def add_borders(infile, outfile, rborder=constants.DEFAULT_RBORDER, lborder=constants.DEFAULT_LBORDER,
                tborder=constants.DEFAULT_TBORDER, bborder=constants.DEFAULT_BBORDER,
                border_color=constants.DEFAULT_BORDER_COLOR):

    # make a video clip
    clip = VideoFileClip(infile)

    # add the borders
    clip_with_borders = clip.margin(
        right=rborder, left=lborder, top=tborder, bottom=bborder, color=border_color)

    # rewrite the video
    rewrite(clip_with_borders, outfile)


# make a function to add text
def add_text(infile, outfile, text, fontsize=constants.DEFAULT_FONTSIZE,
             color=constants.DEFAULT_COLOR, font=constants.DEFAULT_FONT, pos=constants.DEFAULT_POSITION):
    # open the video
    video = VideoFileClip(infile)

    # make a textclip
    txt_clip = TextClip(text, fontsize=fontsize,
                        color=color, font=font).set_duration(video.duration).set_pos(pos)

    # combine them
    result = CompositeVideoClip([video, txt_clip])
    rewrite(result, outfile)
