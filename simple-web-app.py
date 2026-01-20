def lambda_handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My AWS Lambda Web App</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding-top: 80px;
            }
            .box {
                background: #1e293b;
                padding: 30px;
                border-radius: 12px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 AWS Lambda Web App Running!</h1>
            <p>Built by Mr. Paul</p>
            <p>Cloud Training Demo Project</p>
        </div>
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html_content
    }
