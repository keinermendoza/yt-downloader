# Download Videos From Youtube
This is a short script to download videos from YouTube using pytube. Optionally, you can edit them immediately afterward using moviepy.

## Virtual Enviorment

Create a virtual environment and install the dependencies. You can do this using pip, for example:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Select Your Videos

Edit the variable **videos_to_download**. The only required key is **url**.

```python
videos_to_download = [
    {
        "url": "https://www.youtube.com/watch?v=my-first-video",    
    },
    {
        "url": "https://www.youtube.com/watch?v=my-second-video",
    },
]
```

But you can also provide a name and a tuple with clip times if you want to edit them.

```python
videos_to_download = [
    {
        "url": "https://www.youtube.com/watch?v=my-first-video",    
        "cuts": [("01:29:00", "01:30:15")]
    },
]
```

## Run The Script

```shell
python3 youtube.py 
```