=======
# NEMO Timezone plugin

# Description
This plugin allows to change the timezone of NEMO for specific users.
This means rules, input and output dates will be assumed in the user's timezone instead of the server's timezone.
This plugin is best suited for 2 or more facilities sharing an instance of NEMO across timezones.

# Usage
Install using `pip install git+https://github.com/usnistgov/NEMO-timezone-plugin` and this git repository.

Add to `MIDDLEWARE`:
`'NEMO_timezone.middleware.UserTimezoneMiddleware',`

Then go to NEMO Detailed Administration and select User Preferences.
Edit or add new preferences and select the appropriate time zone
