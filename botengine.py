import AccountAgent, DBUsers
import constants
import datetime


def init(webdriver):
   constants.init()
   AccountAgent.login(webdriver)


def follow_people(webdriver):
   constants.init()
   AccountAgent.follow_people(webdriver)