from hsaudiotag import auto

def get_tags_info(audio_file):
    myfile = auto.File(audio_file)
    title=myfile.title
    duration=(float(myfile.duration))/60

    return {'title':title,'duration':duration}



