# Download instagram profile picture

import instaloader

insta=instaloader.Instaloader()

name=input("Enter the username : ")

insta.download_profile(name, profile_pic_only=True)




