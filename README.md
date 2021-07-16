# Mubert

## What is Mubert
Mubert is an app for [Android](https://play.google.com/store/apps/details?id=com.jellyworkz.mubert) and for [iOS](https://apps.apple.com/app/apple-store/id1154429580) for AI Music.

## How I did it
I simply caught the traffic with [MITM-Proxy](https://mitmproxy.org/) and analyzed it.


## How Mubert works
At first, the app generates an unique ID (The cookie called `mat_id` or `mat` ) and does a request to `https://api-app.mubert.com/v2/AppGetPages` to get the available streams and backgrounds from **Giphy** (Yes you're rigth, from **Giphy**). in this JSON-file is everything you need:
- The audio-Links
- The background-links
- The Genres

Then you can access these urls with your `mat_id` and your `mat`-cookies and the user-agent `MubertAndroid`.
That's it.

