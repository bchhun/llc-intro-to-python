import csv

with open('./llc-chapters.csv') as chapter_file:
    chapters_data = csv.DictReader(chapter_file)

    # identifier les chapter leads qui sont seul et qui sont en
    # ontario
    for chapter in chapters_data:
        is_in_ontario = chapter.get('Province') == 'ON'
        is_alone = "&" not in chapter.get('Chapter Lead(s)')

        if is_in_ontario and is_alone:
            print(chapter.get('Chapter Lead(s)'))
