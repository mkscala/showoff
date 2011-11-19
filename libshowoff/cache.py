import os, Image
from image import get_edit_or_original

def clear_cache(app, album, filename, size):
    path_to_file = os.path.join(app.config['CACHE_DIR'], str(album), str(size), os.path.basename(filename))
    if os.path.exists(path_to_file):
        os.unlink(path_to_file)

def update_cache(app, album, filename, size):
    adir = os.path.join(app.config['CACHE_DIR'], album)
    if not os.path.exists(adir):
        os.mkdir(adir)
    tdir = os.path.join(adir, str(int(size)))
    if not os.path.exists(tdir):
        os.mkdir(tdir)

    img = Image.open(os.path.join(get_edit_or_original(app, album, filename), filename))
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(os.path.join(tdir, os.path.basename(filename)), "JPEG")

