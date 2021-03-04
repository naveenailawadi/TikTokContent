if __name__ == '__main__':
    from core import functions
    import eel

    eel.init('web')

    eel.start('templates/main.html', jinja_templates='templates')
