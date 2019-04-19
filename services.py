import os


class Course_Services():
    def __init__(self, course_name):
        self.course_name = course_name
        self.basedir_course = os.getcwd() + '/' + self.course_name

    def create_dir(self):
        os.makedirs(self.course_name)

    def create_dir_images(self):
        dir_images = self.basedir_course + '/images/'
        os.makedirs(dir_images)
        pass

    def create_file_notes_md(self):
        if not os.path.exists(self.basedir_course + '/notes.md'):
            with open(self.basedir_course +'/notes.md', mode='w'):
                pass
        else:
            pass