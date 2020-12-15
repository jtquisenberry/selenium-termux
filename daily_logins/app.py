import os
import logging
import uuid
from webdriver_screenshot import WebDriverScreenshot

if __name__ == '__main__':

    #screenshot_file = "{}-{}".format(''.join(filter(str.isalpha, os.environ['URL'])), str(uuid.uuid4()))
    driver = WebDriverScreenshot()


    #driver.save_screenshot(os.environ['URL'], '/tmp/{}-fixed.png'.format(screenshot_file), height=1024)
    driver.save_screenshot('linux_abc.png', height=1024)


    #driver.save_screenshot(os.environ['URL'], '/tmp/{}-full.png'.format(screenshot_file))

    driver.close()

    '''
    if all (k in os.environ for k in ('BUCKET','DESTPATH')):
        ## Upload generated screenshot files to S3 bucket.
        s3.upload_file('/tmp/{}-fixed.png'.format(screenshot_file), 
                    os.environ['BUCKET'], 
                    '{}/{}-fixed.png'.format(os.environ['DESTPATH'], screenshot_file))
        s3.upload_file('/tmp/{}-full.png'.format(screenshot_file), 
                    os.environ['BUCKET'], 
                    '{}/{}-full.png'.format(os.environ['DESTPATH'], screenshot_file))
    '''