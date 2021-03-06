from core.objects import Video
import constants
from jinja2 import Environment, FileSystemLoader
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import shutil
import requests
import eel


# make a class that can download videos
class TikTokBot:
    def __init__(self, wait_increment=constants.DEFAULT_WAIT_INCREMENT, headless=False):
        # set the wait increment
        self.wait_increment = wait_increment

        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument('--window-size=1420,1080')
            options.add_argument('--headless')

        # create a browser
        self.driver = webdriver.Chrome()

        # create a requests session
        self.session = requests.Session()

    # make a function to get the video data
    def get_data(self, link):
        # just make a video object and it will handle the rest
        video = Video(link, self.driver)

        return video

    # use the link and filepath (home folder designated by another function in the program)

    def download_video(self, filename, link=None, end_directory=constants.DESTINATION_FOLDER):
        # go to the url if it is indicated
        if link:
            self.driver.get(link)

            # wait for it to load
            eel.sleep(self.wait_increment)

        # browser only loads one video (rest are just pictures)
        video_elem = self.driver.find_element_by_xpath('//video')
        source_link = video_elem.get_attribute('src')

        # add the video to a new element (all in javascript --> use jinja)
        output_filepath = self.download(source_link, filename, end_directory)

        return output_filepath

    def hover_click(self, element):
        hover = ActionChains(self.driver).move_to_element(
            element).click()
        hover.perform()

    def download(self, source_link, filename, end_directory=constants.DESTINATION_FOLDER):
        # set the environment with the js
        env = Environment(loader=FileSystemLoader('core'))
        template = env.get_template('download.js')

        # render the script
        script = template.render(
            link=source_link, file=filename)

        # go to the base video link
        self.driver.get(source_link)

        # use the driver to start the download
        self.driver.execute_script(script)

        # allow time for download
        eel.sleep(self.wait_increment * 2)

        # move it from the download folder to the current directory
        shutil.move(f"{constants.DOWNLOAD_FOLDER}/{filename}", end_directory)

        output_filepath = f"{end_directory}/{filename}"

        return output_filepath

    def close(self):
        self.driver.quit()
