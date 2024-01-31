import os
from pytube import YouTube
import moviepy.editor as mvpy
from slugify import slugify


def download_video(url, cuts=None, title=None):
    yt = YouTube(url)
    if not title:
        title = yt.title
    title = slugify(title)
    fulltitle = title + ".mp4"

    video = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
        .download(fulltitle, max_retries=2)
    )
    if cuts:
        edit_video(title, video, cuts)


def edit_video(title, fulltitle, cuts):
    newtitle = title + "-edited.mp4"
    with mvpy.VideoFileClip(fulltitle) as video:
        clips = []
        for cut in cuts:
            clip = video.subclip(cut[0], cut[1])
            clips.append(clip)

        final_clip = mvpy.concatenate_videoclips(clips)
        final_clip.write_videofile(newtitle)
        os.remove(fulltitle)
