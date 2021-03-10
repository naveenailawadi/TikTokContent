import constants
from selenium.common.exceptions import NoSuchElementException
import eel


# make a comment class
class Comment:
    def __init__(self, element):
        # use the element to get the text
        self.text = element.find_element_by_xpath(
            './/*//p//span[@class="jsx-1335515755"]').text

        # find the like count
        likes_str = element.find_element_by_xpath(
            './/*//span[@class="jsx-1335515755 count"]').text

        # check for a "k" in the likes string
        if "k" in likes_str.lower():
            # trim it and multiply it
            self.likes = int(likes_str[:-1]) * 1000
        else:
            self.likes = int(likes_str)


# make a video object
class Video:
    def __init__(self, link, driver):
        # make a list and a link
        self.link = link

        # add a driver to use
        self.driver = driver

        # add the caption and comments
        self.get_caption()
        self.scrape_comments()

    # make a function to get tje title
    def get_caption(self):
        # go to the link
        self.driver.get(self.link)

        # scrape the caption
        self.caption = None

        # set the paths to try
        paths = [
            '//h1', '//div[@class="tt-video-meta-caption jsx-1385049866 jsx-531976133"]']

        for path in paths:
            # get the caption via a path
            try:
                self.caption = self.driver.find_element_by_xpath(path).text
                eel.sleep(constants.DEFAULT_WAIT_INCREMENT)

                # break the loop if you find a caption
                break
            except NoSuchElementException:
                pass

    # make a function to pull all the comments
    def scrape_comments(self):
        # get the comment button and click it if available
        try:
            btns = self.driver.find_elements_by_xpath(
                '//div[@class="jsx-1045706868 bar-item-wrapper"]')
            comment_btn = btns[1]

            comment_btn.click()
            eel.sleep(constants.DEFAULT_WAIT_INCREMENT)
        except IndexError:
            # means the user already inputted a link that goes to the comments
            pass

        # get the comments
        comment_elems = self.driver.find_elements_by_xpath(
            '//div[@class="jsx-1335515755 comment-content level-1 comment-pc"]')

        # get them all into comment objects
        self.comments = [Comment(elem) for elem in comment_elems]
