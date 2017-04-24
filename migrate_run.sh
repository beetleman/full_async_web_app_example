#!/usr/bin/evn bash

pw_migrate migrate --database $DATABASE_URL --directory full_async_web_app_example/migrations $@
