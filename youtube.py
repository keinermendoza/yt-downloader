from utils import download_video


def main():
    """ "
    downloads a video from youtube in mp4 format,
    optionally cuts portions of the video

    url: valid url from your videos on youtube
    cuts: [optional] portions of video you want to keep
    title: [optional] name for the file
    """

    # EDIT THIS FOR DOWNLOAD YOUR VIDEOS
    videos_to_download = [
        {
            "url": "https://www.youtube.com/watch?v=video-to-download",
            "cuts": [
                ("01:29:00", "01:30:15"),
                ("02:39:00", "02:40:15"),
            ],
            "title": "test video title",
        },
    ]

    for video in videos_to_download:
        download_video(**video)


if __name__ == "__main__":
    main()
