# set the download folder (where browser downloads usually go) to allow python to move stuff
DOWNLOAD_FOLDER = '/Users/naveenailawadi/Downloads'
DESTINATION_FOLDER = '/Users/naveenailawadi/Desktop/GitHub/TikTokContent/content'

# set the amount of comments to output
COMMENT_LIMIT = 3

# set how long to wait when loading a page (depends on internet connection)
DEFAULT_WAIT_INCREMENT = 3

# set values of the border
DEFAULT_RBORDER = 110
DEFAULT_LBORDER = 110
DEFAULT_TBORDER = 60
DEFAULT_BBORDER = 60


# set amount to trim text overflow (can be important when adding horizontal padding)
HCROP = 45
VCROP = 0

# align the text
DEFAULT_ALIGN = 'East'

# color is a mix of rgb
DEFAULT_BORDER_COLOR = (255, 255, 255)

# font stuff

# set the fontsize
DEFAULT_FONTSIZE = 20

# set the values of the position (where the text starts)
'''
Examples
--------
>>> clip.with_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.with_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.with_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.with_position(lambda t: ('center', 50+t) )
'''
DEFAULT_POSITION = (45, -550)


# see docs folder for complex options
DEFAULT_COLOR = 'black'
DEFAULT_FONT = 'Times-Roman'
