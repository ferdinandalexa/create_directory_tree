import click

from services import Course_Services

@click.command()
@click.argument(
    'course_name',
    type=str)
def cli(course_name):
    """ Create the course tree directory """
    course = Course_Services(course_name)
    course.create_dir()
    course.create_dir_images()
    course.create_file_notes_md()