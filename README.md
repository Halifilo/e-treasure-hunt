**IMPORTANT - PLEASE NOTE**

**It is your responsibility to ensure that any accounts and credentials used by
this app are set up with adequate security measures and usage caps, such that if
they are compromised, no charges or problems will arise.**

You can check where a given credential is used by searching the code for the
name of the environment variable that holds it (see Setup below).

Due to the the terms of certain dependencies, this application may **not** be
used to generate revenue.

---

# Deploying the app

You can either deploy this app hosted (on Heroku) or locally.

Either way you will need:

- A Dropbox account, with an app set up with read/write permission to a specific
  folder to hold the level images, and a corresponding OAuth key
- If you are using Google Maps: a Google Cloud account with Places and Maps
  JavaScript APIs enabled, and API key
  - NOTE: this API key is passed to clients, so you must ensure you have
    appropriate usage limits configured to avoid being charged if it is
    mis-used.
    You may also wish to employ additional security measures e.g.
    configuring an allowed redirect URI.

## How to deploy using Heroku

### Prerequisites

- Heroku account
- Heroku CLI installed

### Setup

- Create your Heroku app
- Set the `DJ_KEY` environment variable to a secret string
- Set the `DB_TOKEN` environment variable to your DropBox OAuth token
- If you are using Google Maps: Set the `GM_API_KEY` environment variable to your
  Google API key
- Set the `APP_URL` environment variable to the root domain for your app (e.g.
  example.com)
- Add a Heroku Postgres add-on to your app

### Deploy

- Deploy the app to Heroku
- Use the CLI to run `heroku run -a <app_name> python manage.py createsuperuser`
  and set up an admin user

## How to deploy locally

To save on dependency-chasing, a Dockerfile is provided.
Build the image:
```
docker build --tag e-treasure-hunt .
```

Collect static files (you should re-run this if you change the templates):
```
docker run \
  --user "$EUID":"${GROUPS[0]}" \
  --rm \
  --mount type=bind,source=$PWD,target=/usr/src/app \
  e-treasure-hunt collectstatic
```

Run database migrations and create the admin user:
```
docker run \
  --user "$EUID":"${GROUPS[0]}" \
  --rm \
  --mount type=bind,source=$PWD,target=/usr/src/app \
  e-treasure-hunt migrate

docker run \
  --user "$EUID":"${GROUPS[0]}" \
  --interactive \
  --tty \
  --rm \
  --mount type=bind,source=$PWD,target=/usr/src/app \
  e-treasure-hunt createsuperuser
```

Create a file `settings.env` containing your Dropbox token and (if you are using
Google Maps) your Google Maps API key:
```
DB_TOKEN=db_token
GM_API_KEY=api_key
```

With this setup done you can run the app as below, and should find it in your
browser at <https://localhost:80>.

```
docker run \
  --user "$EUID":"${GROUPS[0]}" \
  --rm \
  --mount type=bind,source=$PWD,target=/usr/src/app \
  --env-file settings.env \
  --publish 80:8000 \
  e-treasure-hunt
```

# Initiating the app

## Admin initiation

- Navigate to <domain>/admin
- Create an AppSetting object - tick "active"; if you are NOT using Google Maps,
  tick "use alternate map"

## Create levels

- You can use the content of `dummy_files.zip` as a template
- `about.json` contains the name and location for the level (the name is displayed
  on the _next_ level page, so can be the location) - tolerance is in meters
- `blurb.txt` contains the description for the level (displayed on the next level
  page)
- `clue.png` is the first image - the dummy file contains a background
- `hint1.png`-`hint4.png` are the hints, in order

## Level upload

- Navigate to <domain>/mgmt
- Upload a dummy level 0 using the dummy level files - replace blurb.txt and the
  level name in about.json with text for the start of the hunt
- Upload levels 1-N of the hunt
- Upload a dummy level N+1 using the dummy level files - replace clue with an
  image for the final page
- Navigate to <domain>/home and check your level(s) display correctly

## Create users

- Add a User object via <domain>/admin
- Pass the username and password to the teams and they can begin the hunt!
