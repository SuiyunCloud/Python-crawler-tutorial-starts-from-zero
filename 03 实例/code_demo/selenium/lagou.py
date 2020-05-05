# -*- coding: utf-8 -*-
from selenium import webdriver
import json
import time
import sys
import io

search_word = 'python'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class foxdriver:
    def __enter__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


class Lagou:
    def __init__(self):
        with foxdriver() as driver:
            self.driver = driver
            self.run()

    def run(self):
        driver = self.driver
        rst = self.get_all_job_list(driver)
        rst = self.get_all_job_detail(rst)
        self.output(rst)

    def get_all_job_list(self, driver):
        driver.get("https://www.lagou.com/beijing/")
        driver.find_element_by_id("search_input").click()
        driver.find_element_by_id("search_input").clear()
        driver.find_element_by_id("search_input").send_keys(search_word)
        driver.find_element_by_id("search_button").click()
        driver.find_element_by_xpath("//div[8]/div/div[2]").click()
        total_page = int(
            driver.find_elements_by_css_selector('.pager_container span')[
                -2].text)
        rsts = []
        for index in range(total_page - 1):
            rsts.extend(self.get_data_from_one_page())
            time.sleep(5)
            driver.find_elements_by_css_selector('.pager_container span')[
                -1].click()
            print('done for page', str(index))
        result = {'web': 'lagou', 'items': rsts}
        return result

    def get_all_job_detail(self, jobs):
        for job in jobs['items']:
            url = job.get('url')
            self.driver.get(url)
            job_detail = self.driver.find_element_by_class_name('job-detail').text
            job['detail'] = job_detail
            time.sleep(5)
        return jobs

    def get_data_from_one_page(self):
        driver = self.driver
        jobs = driver.find_elements_by_css_selector(
            '.s_position_list .con_list_item')
        rst = []
        for job in jobs:
            rst.append({
                'job_name': job.get_attribute('data-positionname'),
                'salary': job.get_attribute('data-salary'),
                'company': job.get_attribute('data-company'),
                'url': job.find_element_by_css_selector(
                    '.position_link').get_attribute('href'),
                'publish_time': job.find_element_by_css_selector(
                    '.format-time').text,
                'key': [span.text for span in job.find_elements_by_css_selector(
                    '.list_item_bot .li_b_l span')]
            })
        return rst

    @staticmethod
    def output(result):
        with open('first_run.json', 'a') as fp:
            fp.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    Lagou()
