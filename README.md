=======
# NEMO Timezone plugin

# Description
This plugin allows to change the timezone of NEMO for specific users.
This means rules, input and output dates will be assumed in the user's timezone instead of the server's timezone.
This plugin is best suited for 2 or more facilities sharing an instance of NEMO across timezones.

# Installation
Install using `pip install git+https://github.com/usnistgov/NEMO-timezone-plugin@1.3.0`

Then in your `settings.py`:

* Add to `INSTALLED_APPS` (before `'NEMO'`):

`'NEMO_timezone',`

* Add to `MIDDLEWARE`:

`'NEMO_timezone.middleware.UserTimezoneMiddleware',`

# Usage

Go to NEMO -> Detailed Administration and select User Preferences.
Edit or add new preferences and select the appropriate timezone.

# Option

Note: Enable this option at your own risk. Users could potentially switch timezones back and forth to get around policy rules.

To allow users to change their own timezone in user preferences, set the following in `settings.py`:

```python
USER_PREFERENCES_TZ_ENABLED = True
```
