# How it Works

First, view the InitialPull instructions. This is a GitHub repo created by @david-crespo.
This will go into facebook and pull all of the photos you are tagged in on facebook into a JSON file
Next, you will need to run the FBDownloader script
Into the FBDownloader function at the bottom, insert the source (which is the path to the JSON file created above) and the location in which you'd like to dump the images
This will take all of the photos, convert them into an actual image and alter the modified date to when the photo was uploaded to facebook, not when you pulled it recently.
