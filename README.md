# SunHacks2019

##Steps to deploy and test app engine.
1. export GOOGLE_APPLICATION_CREDENTIALS='Path to creadentials json from google cloud'
2. Setup project in google Cloud and enable Vision API. 
3. Set up an App engine in google cloud.
4. run command 'gcloud app deploy'. Copy the url(app egnine url) from the printed information.
5. Set 'url' variable inside post.py with copied url in laste step. 
6. Set files variable in post.py to any image path in local.
7. Run python post.py. This step will call app engine running in gcloud and returns as json of type '[{'type':'Renil', 'position: 'Left'},{}]'
