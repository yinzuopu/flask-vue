from app import create_app

app = create_app()
# if __name__ == '__main__':
#     app.run()


'''
在运行flask run命令之前手动执行export FLASK_APP=madblog.py能够解决问题，是因为这个环境变量设置告诉 Flask 在哪个文件中找到应用实例。
Flask 使用 FLASK_APP 环境变量来确定应用的位置。通常，Flask 会尝试自动查找名为 app 或 application 的模块或变量，但如果应用的结构与此不同，或者存在多个应用实例，Flask 就无法准确地找到正确的应用。
当你手动执行 export FLASK_APP=madblog.py 时，你明确地告诉 Flask 在 madblog.py 文件中查找应用实例。这样，当你运行 flask run 命令时，Flask 就知道去哪里找应用，从而能够正确地启动服务器。
总之，手动设置 FLASK_APP 环境变量能够确保 Flask 准确地找到并运行你的应用，尤其是在应用结构不那么标准或存在多个潜在的应用实例时。这也是一种更灵活的方式，允许开发者自定义他们的应用启动方式。
'''