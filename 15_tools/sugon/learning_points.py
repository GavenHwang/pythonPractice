# -*- coding:utf-8 -*-
import os
from datetime import datetime
import maskpass
from loguru import logger
from requests import request
from time import sleep


def set_logger():
    t = datetime.strftime(datetime.now(), "%Y%m%d")
    LOG_PATH = os.path.join(os.path.dirname(__file__), "learning_points%s.log" % t)
    logger.add(LOG_PATH, level="DEBUG", rotation="10MB", retention="10 days", encoding="utf-8", enqueue=True,
               backtrace=True, diagnose=True)


set_logger()


class LearningPoints:
    host = "https://learn.sugon.com"

    def __init__(self, username, password):
        token = request(
            method="POST",
            url=self.host + "/api/auth/getToken",
            data={'username': username, 'password': password}
        ).json().get("data")
        self.headers = {"Token": token, 'Content-Type': 'application/json'}

    def page_list(self):
        """获取课程列表"""
        page_list = request(
            method="POST",
            url=self.host + "/api/course/pageList",
            json={"pageNum": 1, "pageSize": 999999, "onStateStatus": 0, "searchMode": "NEW", "index": True},
            headers=self.headers
        ).json().get("data", {}).get("records", [])
        return page_list

    def save_course(self, course_id, course_name):
        """匿名评论课程：赞"""
        res_json = request(
            method="POST",
            url=self.host + "/api/course/comment/saveCourse",
            json={"thirdId": course_id, "type": "FORUM", "commentId": None, "content": "赞",
                  "anonymous": 1, "firstCommentId": None, "replyObjectItcode": None, "replyObjectName": None,
                  "replyObjectAvatar": None, "thirdPartName": course_name},
            headers=self.headers
        ).json()
        return res_json.get("msg")

    def save_like(self, course_id, course_name):
        """点赞课程，先取消点赞，再重新点赞"""
        unlike = request(
            method="POST",
            url=self.host + "/api/course/userscore/saveUnLike",
            json={"score": 1, "thirdPartId": course_id, "thirdPartName": course_name, "typeCode": "LIKE"},
            headers=self.headers
        ).json()
        unlike_msg = unlike.get("msg")
        like = request(
            method="POST",
            url=self.host + "/api/course/userscore/saveLike",
            json={"score": 1, "thirdPartId": course_id, "thirdPartName": course_name, "typeCode": "LIKE"},
            headers=self.headers
        ).json()
        return like.get("msg")

    def learn_state(self, course_id):
        res_json = request(
            method="GET",
            url=self.host + "/api/course/usercourse/getByCourseId/" + course_id,
            headers=self.headers
        ).json()
        return res_json.get("data", {}).get("learnState")

    def already_score(self, course_id):
        res_json = request(
            method="GET",
            url=self.host + "/api/course/getByIdDetailNoDirectory/" + course_id,
            headers=self.headers
        ).json()
        return res_json.get("data", {}).get("userScore", {}).get("alreadyScore")

    def resource_id(self, course_id):
        """获取课程视频资源id"""
        res_json = request(
            method="GET",
            url=self.host + "/api/course/getByIdDetailNoDirectory/" + course_id,
            headers=self.headers
        ).json()
        course_resource_list = res_json.get("data", {}).get("courseResourceList", [])
        return course_resource_list and course_resource_list[0]["id"]

    def add_learn(self, course_id):
        """添加课程到我的学习"""
        res_json = request(
            method="POST",
            url=self.host + "/api/course/usercourse/addLearnState",
            json={"courseId": course_id, "courseResourceId": self.resource_id(course_id), "learnState": 1},
            headers=self.headers
        ).json()
        return res_json.get("msg")

    def save_course_score(self, course_id, course_name):
        """评分课程"""
        res_json = request(
            method="POST",
            url=self.host + "/api/course/userscore/saveCourseScore",
            json={"score": 5, "thirdPartId": course_id, "thirdPartName": course_name, "typeCode": "COURSE"},
            headers=self.headers
        ).json()
        return res_json.get("msg")

    def get_by_login_itcode(self):
        res_json = request(
            method="GET",
            url=self.host + "/api/system/user/getByLoginItcode",
            headers=self.headers
        ).json()
        return res_json.get("subi")

    def acquire_points(self):
        shubi_before = self.get_by_login_itcode()
        logger.info("您当前拥有%s个曙币!" % shubi_before)
        page_list = learning_points.page_list()
        page_list.reverse()
        result1 = result2 = result3 = None
        for course in page_list:
            course_id, course_name = course["id"], course["courseName"]
            learn_state = learning_points.learn_state(course_id)
            already_score = learning_points.already_score(course_id)
            # 评分课程得1分
            if result1 is None and already_score is not True:
                if learn_state == 0:
                    result = self.add_learn(course_id)
                    logger.info('添加"%s"课程' % course_name, result)
                if result1 is None:
                    result1 = self.save_course_score(course_id, course_name)
                    logger.info('评分"%s"课程' % course_name, result1)
                    if not result1 or not result2 or not result3:
                        logger.info("等待30秒，操作太快，不给币！")
                        sleep(30)
            # 评论课程得1分
            if result2 is None:
                result2 = self.save_course(course_id, course_name)
                logger.info('评论"%s"课程' % course_name, result2)
                if not result1 or not result2 or not result3:
                    logger.info("等待30秒，操作太快，不给币！")
                    sleep(30)
            # 点赞课程的1分
            if result3 is None:
                result3 = self.save_like(course_id, course_name)
                logger.info('点赞"%s"' % course_name, result3)
                if not result1 or not result2 or not result3:
                    logger.info("等待30秒，操作太快，不给币！")
                    sleep(30)
            if result1 and result2 and result3:
                break
        shubi_now = self.get_by_login_itcode()
        logger.info("您现在拥有%s个曙币!" % shubi_now)


if __name__ == '__main__':
    username = input("请输入用户名：")
    password = maskpass.askpass(prompt="请输入密码:", mask="*")
    learning_points = LearningPoints(username, password)
    learning_points.acquire_points()
