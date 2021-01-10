# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dbiz_theme"
app_title = "Dbiz Theme"
app_publisher = "Clapton Orioste"
app_description = "Theme for DBiz"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "corioste@bai.ph"
app_license = "MIT"

# Includes in <head>
# ------------------

app_include_css = [
    "/assets/dbiz_theme/css/bdtheme.css",
    "/assets/dbiz_theme/css/skin-blue.css",
    "/assets/dbiz_theme/css/custom.css",
    "/assets/dbiz_theme/css/temp.css",
]
app_include_js = [
    "/assets/dbiz_theme/js/bdtheme.js",
    "/assets/dbiz_theme/js/custom.js",
    "/assets/js/dbiz_theme-template.min.js",
]


# include js, css files in header of desk.html
# app_include_css = "/assets/dbiz_theme/css/dbiz_theme.css"
# app_include_js = "/assets/dbiz_theme/js/dbiz_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/dbiz_theme/css/dbiz_theme.css"
# web_include_js = "/assets/dbiz_theme/js/dbiz_theme.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dbiz_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dbiz_theme.install.before_install"
# after_install = "dbiz_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dbiz_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dbiz_theme.tasks.all"
# 	],
# 	"daily": [
# 		"dbiz_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"dbiz_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dbiz_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dbiz_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dbiz_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dbiz_theme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dbiz_theme.task.get_dashboard_data"
# }
