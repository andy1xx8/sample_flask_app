from website.app import create_app

if __name__ == '__main__':
    print('Running on port 8000 <------------')
    app = create_app()
    app.run(debug=True, port=8000)
