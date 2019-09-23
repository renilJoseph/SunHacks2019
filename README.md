# SunHacks2019 (Best Social Cause, Best Data Science Hack, Best MLH(major league hacking) Project)
An App to help people with blindnes.

## Steps to deploy and test app engine.
1. export GOOGLE_APPLICATION_CREDENTIALS='Path to creadentials json from google cloud'
2. Setup project in google Cloud and enable Vision API. 
3. Set up an App engine in google cloud.
4. run command 'gcloud app deploy'. Copy the url(app egnine url) from the printed information.
5. Set 'url' variable inside post.py with copied url in laste step. 
6. Set files variable in post.py to any image path in local.
7. Run python post.py. This step will call app engine running in gcloud and returns as json of type '[{'type':'Renil', 'position: 'Left'},{}]'

## Running android App
1. set url of appengine inside android code to url we got when running 'gcloud app deploy'.
2. Setup android app in Camera2Basicjava into an android phone.
3. Say 'Ok google, Open Iris', this will open the app with camera open.
4. Now walk holding the phone, and it will detect and say what all obstecles or people are present at what direction.
