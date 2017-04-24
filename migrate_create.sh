#!/usr/bin/evn bash

pw_migrate create --database $DATABASE_URL --directory full_async_web_app_example/migrations --auto full_async_web_app_example.app.models $@
