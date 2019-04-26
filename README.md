# Firmware Release Server

[![Sponsor](https://img.shields.io/badge/Sponsor-jaaga_labs-red.svg?style=for-the-badge)](https://www.jaaga.in/labs)

A firmware release management service for IOT devices and friends.

Originally developed for use with [Joovv](https://joovv.com/).

## Why?

This makes OTA updates a pleasure. 

Your hardware engineer now has a proper place to upload their releases, 
and your app can determine whether an update is required or not, by making trivial API calls.

## What?

Underneath is an extremely simple django application that allows uploading firmware images using the admin panel

![image](https://user-images.githubusercontent.com/19492893/56775972-4852c100-67e7-11e9-8ee7-f4ce84870662.png)


And makes the releases accesbile to devices by simple APIs

`GET http://<domain>/api/latest-after/0.3.5/`

```json
{
    "version": "1.0.0",
    "firmware_bin": "http://<domain>/media/firmware_uploads/1.0.0/firmware_1w0H51u.bin",
    "bootloader_bin": "http://<domain>/media/firmware_uploads/1.0.0/bootloader.bin",
    "partitions_bin": "http://<domain>/media/firmware_uploads/1.0.0/partitions.bin",
    "comments": "fixed the timestamp issues",
    "uploaded_at": "2019-04-25T23:45:16.777279Z"
}
```

`GET http://<domain>/api/latest/` also works.


## Deployment

This project ships out of the box for deploying to [caprover](https://caprover.com/).

- Install caprover
- Create a new app. Make sure to turn on "Has Persistent Data"
- Add persistent directory. 

![image](https://user-images.githubusercontent.com/19492893/56776137-2b6abd80-67e8-11e9-8315-563b7047e707.png)

- Add env vars

![image](https://user-images.githubusercontent.com/19492893/56776153-3c1b3380-67e8-11e9-8ece-c04f89ad04e1.png)


You should be good to go now!
