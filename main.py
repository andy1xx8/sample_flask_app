#from website import create_app
from website.app import create_app

app = create_app()

# @app.errorhandler(Exception)
# def handle_error(e):
#     print('!!!!!!!!!!!!!!')
#     print(e)
#     print('!!!!!!!!!!!!!')


# app.register_error_handler(Exception, handle_other_exceptions)

if __name__ == '__main__':
    print('Running on port 8000 <------------')
    app.run(debug=True, port=8000)
